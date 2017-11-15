import os
import logging
from flask import Flask
from flask_restful import Api
from api.v0.database import CueAPIDatabase

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
    db = CueAPIDatabase(app.config['CASSANDRA_HOST'])
    if app.config["TESTING"]:
        db._populate_with_test_data()
    if app.config["DEMO"]:
        db._populate_with_demo_data()
    log.debug('Creating database tables...')
    log.debug('Database tables created.')
    log.debug('Preparing statements...')
    #db._prepare_statements()
    log.debug('Prepared statements.')
    if app.config['TESTING']:
        log.debug('TESTING is True -- populating the database with demo data...')
        db._populatedb()
        log.debug('Populated the database.')
    log.info('db setup complete.')

    
    log.info('create_app() complete.') 
    return app

