import cue
import json
import logging
from flask import Flask
from flask_restful import Api
from cassandra.cluster import Cluster
from cassandra.query import ordered_dict_factory

log = logging.getLogger('cue-api-log')
log.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

app = Flask(__name__)
api = Api(app)
cluster = Cluster(['cassandra']) # see docker-compose link
# celery / Redis container connect
# worker = celery.init_app(app) ...
# start HTTP2 connection to t

### START DB SETUP
session = cluster.connect()
session.row_factory=ordered_dict_factory
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
        PRIMARY_KEY (uid, (suri, active))
        )
""")
session.execute("""
    CREATE_TABLE IF NOT EXISTS v0.users_by_suri (
        uid UUID,
        suri text,
        active boolean,
        name text,
        PRIMARY_KEY (suri, (uid, active))
    )
""")
session.execute("""
    CREATE_TABLE IF NOT EXISTS v0.events (
        evid UUID PRIMARY_KEY,
        host tuple<UUID, text>,,
        name text,
        cid UUID,
        pin int,
        np text,
        attendees list<tuple<UUID, text>>,
        created_at datetime,
        ended_at datetime
    )
""")
session.execute("""
    CREATE_TABLE IF NOT EXISTS v0.cues (
        cid UUID PRIMARY_KEY,
        evid UUID,
        next text,
        nextnext text,
        queue list<tuple<text, double>>,
        calibrated boolean
    )
""")
session.execute("USE v0")
### END DB SETUP

api.add_resource(Users, '/users/<str:uid>', '/users/<str:suri>')
api.add_resource(Event, '/events', '/events/<str:evid>')
api.add_resource(Cue, '/cues/<str:cid>')


if __name__=="__main__":
    app.run(port=10101, debug=True, use_reloader=False)
