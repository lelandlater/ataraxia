from flask.sessions import SessionMixin
class CueAPIDatabase:

    class CueAPISession(dict, SessionMixin)
    session = None

    def setupdb(session):
        session.execute("""
            CREATE KEYSPACE IF NOT EXISTS v0
            WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 }'
        """)
        session.execute("""
            CREATE_TABLE IF NOT EXISTS v0.users_by_uid (
                uid UUID,
                suri text,
                active boolean,
                name text,
                PRIMARY_KEY (uid)
            )
        """)
        session.execute("""
            CREATE_TABLE IF NOT EXISTS v0.users_by_suri (
                uid UUID,
                suri text,
                active boolean,
                name text,
                joined_at datetime
                PRIMARY_KEY (suri)
            )
        """)
        session.execute("""
            CREATE_TABLE IF NOT EXISTS v0.events (
                evid UUID,
                host map<UUID, text>,,
                name text,
                cid UUID,
                pin int,
                np text,
                attendees list<map<UUID, text>>,
                created_at datetime,
                ended_at datetime,
                last_active timeuuid,
                PRIMARY_KEY (evid)
            )
        """)
        session.execute("""
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
        return session

    def populatedb(session):
        # add users
        # add events
        # TODO write this for testing
        return True