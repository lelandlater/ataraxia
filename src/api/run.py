import cue
import json
import logging
from flask import Flask
from flask_restful import Api
from cassandra.cluster import Cluster
from cassandra.query import ordered_dict_factory

log = logging.getLogger()
log.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

app = Flask(__name__) # or app = Flask(name=u'cue-api')
api = Api(app)
cluster = Cluster(['cassandra']) # see docker-compose link
session = cluster.connect()

from cue.models import _setup_db
session=_setup_db(session)

# create API
api.add_resource(User, '/user/<int:uid>', '/user/<int:suri>')
api.add_resource(Event, '/event/<int:evid>')
api.add_resource(Events, '/events')
api.add_resource(Cue, '/cue')
api.add_resource(Track, '/track')



if __name__=="__main__":
    app.run(port=10101, debug=True, use_reloader=False)    
