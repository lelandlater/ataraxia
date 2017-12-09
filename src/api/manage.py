import os, time, logging, yaml, sys
import logging.config
from api.v0 import create_app
from api.v0.models.user import User
from api.v0.models.event import Event
from api.v0.models.cue import Cue
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from config import cfg

def _setup_log(path='config/log.cueapi.yml'):
    """Configure the logger.
    """
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)

app = create_app(cfg)

# add Flask-Script, management functions here ## Saturday Dec. 9?

def main():
    _setup_logger()
    connection.setup(['cassandra'], 'v0', protocol_version=3)
    sync_table(User)
    sync_table(Event)
    sync_table(Cue)
    log.info("Got to here...")
    app.run(port=10101, debug=True, use_reloader=False)

if __name__=="__main__":
    main()