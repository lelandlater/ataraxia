import logging
from cassandra.cluster import Cluster, Session
from cassandra.query import ordered_dict_factory
from .errors import *

log = logging.getLogger('cueapi.database')

class CueAPIDatabase(object):
    """
    Database abstraction.
    """

    def __init__(self, host=None):
        if host is not None:
            self.host=host
        else:
            self.host='127.0.0.1'
        cluster = Cluster([host])
        self._set_session(cluster.connect())
        return 0

    def _set_session(self, new_sesh):
        """
        Connect a session to a db backend.
        The session object is set in ./__init__.py, in create_app().
        """
        log.warn('Atempting to reset the session.')
        if isinstance(new_sesh, Session):
            self.session = new_sesh
            return 0
        else:
            raise CannotConnectToBackendError

    def _get_session(self):
        """
        Return the session object.
        """
        return self.session

    def _retrieve_prepared_statement(self, statement):
        """
        Retrieve a prepared statement.
        err: 172
        """
        if statement not in self.prepared_statements:
            raise StatementNotPreparedError("Did not pre-prepare statement for execution.")
        return self.prepared_statements[statement]

    def _disconnect_session(self):
        """
        End the session.
        """
        self.session.close()
        return 0

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
                private boolean,
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
                cid UUID,
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
        Statements used more than once.
        """
        log.info('Preparing statements.')
        create_event=self.session.prepare("INSERT INTO events (evid, host) VALUES (?, ?)")
        create_cue=self.session.prepare("INSERT INTO cues (cid, evid) VALUES (?, ?)")
        get_user_by_suri=self.session.prepare("SELECT (uid, suri, name, active) FROM users_by_suri WHERE suri=?")
        get_user_by_uid=self.session.prepare("SELECT (uid, suri, name, active) FROM users_by_uid WHERE uid=?")
        get_event_by_evid=session.prepare("SELECT (evid, host, name, cid, np, attendees, private) FROM events WHERE evid=?")
        get_cid_by_evid=session.prepare("SELECT (cid) FROM events WHERE evid=?")
        get_curr_track_by_evid=session.prepare("SELECT (curr_track) FROM events WHERE evid=?")
        get_next_track_by_cid=session.prepare("SELECT (next) FROM cues WHERE cid=?")
        log.info('Prepared the statements.')
        stmts = {
            'create_event': create_event,
            'create_cue': create_cue,
            'get_user_by_suri': get_user_by_suri,
            'get_user_by_uid': get_user_by_uid,
            'get_event_by_evid': get_event_by_evid,
            'get_cid_by_evid': get_cid_by_evid,
            'get_curr_track_by_evid': get_curr_track_by_evid,
            'get_next_track_by_cid': get_next_track_by_cid, 
        }
        self.prepared_statements = stmts
        
    def _populate_with_test_data(self):
        """Populates the database with fudged data. Use in demo or testing."""
        log.warn('Populating the database with test data.')
        
        pass

    def _populate_with_demo_data(self):
        log.warn('Populating the database with demo data.')


    def _run_query(self, statement):
        """Execute non-prepared query."""
        log.debug('Executing a non-prepared query:\n{0}'.format(statement))
        try:
            self.session.execute(statement)
            return 0
        except BadQueryError as e:
            log.error("Bad query against Cassandra!")
            exit(e)

