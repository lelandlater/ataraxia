from cassandra.cluster import Cluster, Session
from cassandra.query import ordered_dict_factory
from . import log
from .errors import CannotConnectToBackendError
    
class CueAPIDatabase:

    def __init__(self, endpt=None):
        if endpt is not None:
            self.endpt=endpt
        else:
            self.endpt='0.0.0.0'
        cluster = Cluster([endpt])
        _set_session(cluster.connect())

    def _set_session(self, new_sesh):
        """
        Connect a session to a db backend.
        The session object is set in ./__init__.py, in create_app().
        """
        log.warn('Atempting to reset the session.')
        if isinstance(new_sesh, Session):
            # other checks ? ie part of same cluster ?
            self.session = new_sesh
        else:
            raise CannotConnectToBackendError

    def _get_session(self):
        """
        Return the session object.
        """
        return self.session

    def _disconnect_session(self):
        """
        End the session.
        """
        self.session.close()
        return True

    def _setupdb(self):
        """
        Create tables, if they do not exist, and they should not. 
        """
        self.session.row_factory = ordered_dict_factory
        self.session.execute("""
            CREATE KEYSPACE IF NOT EXISTS v0
            WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 }'
        """)
        log.info('Created v0 keyspace.')
        self.session.execute("""
            CREATE_TABLE IF NOT EXISTS v0.users_by_uid (
                uid UUID,
                suri varchar,
                active boolean,
                name text,
                PRIMARY_KEY (uid)
            )
        """)
        log.info('Created v0.users_by_uid table.')
        self.session.execute("""
            CREATE_TABLE IF NOT EXISTS v0.users_by_suri (
                uid UUID,
                suri varchar,
                active boolean,
                name text,
                joined_at datetime
                PRIMARY_KEY (suri)
            )
        """)
        log.info('Created v0.users_by_suri table.')
        self.session.execute("""
            CREATE_TABLE IF NOT EXISTS v0.events (
                evid UUID,
                host map<UUID, varchar>,,
                name text,
                cid UUID,
                pin int,
                np text,
                attendees list<map<UUID, varchar>>,
                created_at datetime,
                ended_at datetime,
                last_active timeuuid,
                PRIMARY_KEY (evid)
            )
        """)
        log.info('Created v0.events table.')
        self.session.execute("""
            CREATE_TABLE IF NOT EXISTS v0.cues (
                cid UUID ,
                evid UUID,
                next text,
                nextnext text,
                queue list<map<text, double>>,
                calibrated boolean,
                PRIMARY_KEY (cid)
            )
        """)
        log.info('Created v0.cues table.')
        log.info('v0 keyspace and cue tables created.')

    def _prepare_statements(self):
        """
        If you use a statement more than once, prepare it.
        """
        # can I do this in a better way?
        log.info('Preparing statements.')
        create_event=self.session.prepare("INSERT INTO events (evid, host) VALUES (?, ?)")
        create_cue=self.session.prepare("INSERT INTO cues (cid, evid) VALUES (?, ?)")
        get_user_by_suri=self.session.prepare("SELECT * FROM users_by_suri WHERE suri=?")
        get_user_by_uid=self.session.prepare("SELECT * FROM users_by_uid WHERE uid=?")
        get_events=self.session.prepare("SELECT (evid, name, created_at) FROM events")
        get_event_by_evid=session.prepare("SELECT * FROM events WHERE evid=?")
        get_cid_by_evid=session.prepare("SELECT (cid) FROM events WHERE evid=?")
        get_curr_track_by_evid=session.prepare("SELECT (curr_track) FROM events WHERE evid=?")
        get_next_track_by_cid=session.prepare("SELECT (next) FROM cues WHERE cid=?")
        log.info('Prepared the statements.')
        stmts = {
            'create_event': create_event,
            'create_cue': create_cue,
            'get_user_by_suri': get_user_by_suri,
            'get_user_by_uid': get_user_by_uid,
            'get_events': get_events,
            'get_event_by_evid': get_event_by_evid,
            'get_cid_by_evid': get_cid_by_evid,
            'get_curr_track_by_evid': get_curr_track_by_evid,
            'get_next_track_by_cid': get_next_track_by_cid, 
        }
        self.prepared_statements = stmts
        
    '''Testing functions, ie used in tests.'''
    def _populatedb(session):
        # add users
        # add events
        # TODO write this for testing
        return True

db = CueAPIDatabase() # app.config['CASSANDRA_HOST'] # PYTHON where can I app so session object is accessible 
    