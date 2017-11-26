import os
import logging
from flask import Flask
from flask_restful import Api

log = logging.getLogger('cueapi.init')

def create_app(cfg=None):
    app = Flask(__name__)

    if cfg is not None:
        app.config.from_object(cfg)

    log.debug('Registering routes...')
    from .endpoints import v0
    app.register_blueprint(v0)
    log.info('Routes registered.')

    log.info('Beginning db setup...')
    if app.config["TESTING"]:
        pass
    if app.config["DEMO"]:
        pass
    log.debug('Creating database tables...')
    log.debug('Database tables created.')
    log.debug('Preparing statements...')
    log.debug('Prepared statements.')
    if app.config['TESTING']:
        log.debug('TESTING is True -- populating the database with demo data...')
        log.debug('Populated the database.')
    log.info('db setup complete.')

    
    log.info('create_app() complete.') 
    return app

