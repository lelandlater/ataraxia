import os, time, logging, yaml, sys
import logging.config
from api.v0 import create_app
from api.v0.models.user import User
from api.v0.models.event import Event
from api.v0.models.cue import Cue
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from config import cfg

log = logging.getLogger(__name__)
app = create_app(cfg)

# add Flask-Script, management functions here ## Saturday Dec. 9?
# or FlaskCLI ?

def main():
    try:
        with open(app.conf['CUEAPI_LOG_CONFIGURATION_PATH'], 'rt') as f:
            config = yaml.safe_load(f.read())
            log.debug("lo")
        logging.config.dictConfig(config)
    except:
        logging.basicConfig(level=logging.INFO)
    connection.setup(['cassandra'], 'v0', protocol_version=3)
    log.debug("beginning to sync tables")
    sync_table(User)
    log.debug("synced Users table")
    sync_table(Event)
    log.debug("synced Events table")
    sync_table(Cue)
    log.debug("synced Cues table")
    log.debug("starting the app")
    app.run(port=10101, debug=True, use_reloader=False)
    log.debug("app started")

if __name__=="__main__":
    main()