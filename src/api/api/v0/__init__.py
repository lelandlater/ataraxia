import os
import logging
from flask import Flask
from flask_restful import Api

log = logging.getLogger('cueapi')

def create_app(cfg=None):
    app = Flask(__name__)
    if cfg is not None:
        app.config.from_object(cfg)
    log.info('Beginning db setup...')
    from .database import CueAPIDatabase
    log.debug('Creating database tables...')
    _setupdb()
    log.debug('Database tables created.')
    log.debug('Preparing statements...')
    db._prepare_statements()
    log.debug('Prepared statements.')
    if app.config['TESTING']:
        log.debug('TESTING is True -- populating the database with demo data...')
        db._populatedb()
        log.debug('Populated the database.')
    log.info('db setup complete.')

    log.debug('Registering routes...')
    from .endpoints import v0
    api = Api(v0)
    from models import user, event, cue
    api.add_resource(user.CueUser, '/users', '/users/<uuid:uid>')
    api.add_resource(event.CueEvent, '/events', '/events/<uuid:evid>')
    api.add_resource(cue.Cue, '/cues', '/cues/<uuid:cid>')
    app.register_blueprint(v0)
    log.debug('Routes registered.')
    log.info('create_app() complete.') 
    return app

"""
QUESTION

implementing the app factory, and adding Celery

"""
