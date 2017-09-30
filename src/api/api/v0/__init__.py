import os
import logging
from flask import Flask, Blueprint
from cassandra.cluster import Cluster
from cassandra.query import ordered_dict_factory

log = logging.getLogger('cueapi')
log.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

def create_app(cfg=None):
    app = Flask(__name__)
    #print("cfg is --> {}".format(cfg))
    if cfg is not None:
        app.config.from_object(cfg)
    var=app.config['CASSANDRA_HOST']
    #print("app.config is --> {}".format(var))
    cluster = Cluster([app.config['CASSANDRA_HOST']])

    ### START DB SETUP
    log.info('beginning db setup...')
    session = cluster.connect()
    session.row_factory = ordered_dict_factory

    from models.database import CueAPIDatabase as db

    log.debug('Creating database tables...')
    session=db.setupdb(session)
    log.debug('Database tables created.')
    if app.config['TESTING']:
        log.debug('TESTING is True -- populating the database with demo data...')
        session=db.populatedb(session)
        log.debug('Populated the database.')
    log.info('db setup complete.')
    ### END DB SETUP

    ### ROUTING
    from .endpoints import v0
    app.register_blueprint(v0)

    # make some sort of dictionary with this ?
    _create_event=session.prepare("INSERT INTO events (evid, host) VALUES (?, ?)")
    _create_cue=session.prepare("INSERT INTO cues (cid, evid) VALUES (?, ?)")
    _get_user_by_suri=session.prepare("SELECT * FROM users_by_suri WHERE suri=?")
    _get_user_by_uid=session.prepare("SELECT * FROM users_by_uid WHERE uid=?")
    _get_events=session.prepare("SELECT (evid, name, created_at) FROM events")
    _get_event_by_evid=session.prepare("SELECT * FROM events WHERE evid=?")
    _get_cid_by_evid=session.prepare("SELECT (cid) FROM events WHERE evid=?")
    _get_curr_track_by_evid=session.prepare("SELECT (curr_track) FROM events WHERE evid=?")
    _get_next_track_by_cid=session.prepare("SELECT (next) FROM cues WHERE cid=?")

    return app