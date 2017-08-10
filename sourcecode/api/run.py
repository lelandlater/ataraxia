import json
import logging
from flask import Flask
from flask_restful import Api
from marshmallow import Marshmallow
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from resources import User, Event, Events, Cue, Track

log = logging.getLogger()
log.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

app = Flask(__name__)
api = Api(app)
ma = Marshmallow(app)
cluster = Cluster(['0.0.0.0'])
session = cluster.connect()
session.execute(
    '''
    CREATE KEYSPACE IF NOT EXISTS users
    WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}'
    ''')
session.execute('''
    CREATE KEYSPACE IF NOT EXISTS events
    WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}'
    ''')
session.execute('''
    CREATE KEYSPACE IF NOT EXISTS cues
    WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}'
    ''')
session.execute('''
    CREATE KEYSPACE IF NOT EXISTS tracks
    WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}'
    ''')
# QUESTION: relationship between many keyspaces and tabels at this point?
sesssion.execute('USE users')
session.execute(
    '''
    CREATE_TABLE users_by_suri (
        suri text PRIMARY_KEY,
        uid int,
        name text,
        active boolean
    )
    ''')
session.execute(
    '''
    CREATE_TABLE users_by_uid (
        uid int PRIMARY_KEY,
        suri text,
        name text,
        active boolean
    )
    ''')
session.execute('USE events')
session.execute(
    '''
    CREATE_TABLE events_by_host (
        host text PRIMARY_KEY,
        name text,
        evid int,
        cueid int,
        created_at int,
        last_active int,
        curr_track text
    )
    ''')
# event search bar listing
# QUESTION: make writes less expensive by add partition key?
session.execute(
    '''
    CREATE_TABLE events_by_last_active (
        last_active int PRIMARY_KEY,
        host text,
        name text,
        evid uuid,
        cueid uuid,
        created_at timeuuid,
        curr_track text
    )
    ''')
# event search bar querying
session.execute(
    '''
    CREATE_TABLE events_by_name (
       name text PRIMARY_KEY,
       host text,
       curr_track text,
       created_at timeuuid,
       last_active int,
       cueid uuid,
       evid uuid
    )
    ''')
# ...
session.execute('USE cues')
session.execute(
    '''
    CREATE_TABLE cues_by_cueid (
        cueid uuid PRIMARY_KEY,
        next_track text,
        cued uuid  
    )
    ''')
session.execute('USE tracks')
session.execute(
    '''
    CREATE_TABLE tracks_by_cueid (
       cueid uuid PRIMARY_KEY,
       track text,
       rank float
    )
    ''')


# create API
api.add_resource(User, '/user/<int:uid>', '/user/<int:suri>')
api.add_resource(Event, '/event/<int:evid>')
api.add_resource(Events, '/events')
api.add_resource(Cue, '/cue')
api.add_resource(Track, '/track')

session=''

if __name__=="__main__":
    app.run(port=10101, debug=True, use_reloader=False)
    _populate_with_sample_data()    
