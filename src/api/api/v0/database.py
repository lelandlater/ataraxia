import logging
from api.v0.models.user import UserBySuriModel, UserByUidModel
from api.v0.models.event import EventModel
from api.v0.models.cue import CueModel
from cassandra.cqlengine.management import sync_table
from .errors import *

log = logging.getLogger('cueapi.database')
connection.setup(['cassandra'], 'v0', protocol_version=3)

class CueAPIDatabase(object):
    """
    Database abstraction.
    """

    def __init__(self):
        pass

    def _setupdb(self):
        """
        Create tables, if they do not exist, and they should not. 
        """
        log.info('Created v0.cues table')
        log.info('v0 keyspace and cue tables created')
        

    def _populate_with_test_data(self):
        """Populates the database with edge case data. Use in testing."""
        log.warn('Populating the database with test data')
        
        pass

    def _populate_with_demo_data(self):
        """Populates the database with fudged data. Use in development."""
        log.warn('Populating the database with demo data')

        pass

    def _sync_table(self, tablename):
        return sync_table(tablename)
