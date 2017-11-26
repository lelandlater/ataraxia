import logging
from api.v0 import create_app
from api.v0.models.user import User
from api.v0.models.event import Event
from api.v0.models.cue import Cue
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from config import config

log = logging.getLogger('cueapi')
log.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

app = create_app(config.DevelopmentConfig)

# add Flask-Script, management functions here

if __name__=="__main__":
    connection.setup([app.config["CASSANDRA_HOST"]], "cqlengine", protocol_version=3)
    sync_table(User)
    sync_table(Event)
    sync_table(Cue)
    app.run(port=10101, debug=True, use_reloader=False)
