import logging
from api.v0.decorators import api
from api.v0 import db
from cassandra.cqlengine import columns as cql
from cassandra.cqlengine import connection
from cassandra.cqlengine.models import Model
from flask_restful import Resource, fields

log = logging.getLogger('cue-api.event')
connection.setup(['cassandra']), 'v0', protocol_version=3)

class EventModel(Model):
    """
    Cassandra data model for event table.

    Each event has exactly one host and exactly one cue.
    Each each event has a set of users (attendees) unique amongst all users.
    This model interfaces with the Cassandra session by creating objects in Python.
    """
    evid = cql.UUID(primary_key=True, required=True, default=uuid.uuid4)
    host = cql.UUID(required=True)
    name = cql.Text()
    cid = cql.UUID(required=True)
    pin = cql.Integer()
    np = cql.Text()
    attendees = cql.Set(value_type=cql.UUID(), required=True)
    created_at = cql.DateTime(required=True),
    ended_at = cql.DateTime()
    last_active = cql.TimeUUID(required=True)

class CueUserDataField(fields.Raw):
    """Represents a Cue user as Flask-Restful field."""
    def format(self, uid, suri):
        return "({0}, {1})".format(sui, uid)

class EventData(object):
    """Returned event data from query."""
    event_data_fields = {
        'evid': fields.String,
        'host': CueUserDataField(),
        'name': fields.String,
        'cid': fields.String,
        'np': fields.String,
        'attendees': fields.List(CueUserDataField()),
        'private': fields.Boolean,
        'pin': fields.String,
        'created_at': fields.String,
        'last_active': fields.String
    }

def _retrieve_event_with_evid(evid):
    return -1

def _add_user_to_event(evid, uid):
    pass

def _remove_user_from_event(evid):
    pass

def _end_event(evid):
    pass

class EventAPI(Resource):
    """
    From Flask-Restful, a REST API for event table.
    """
    decorators=[api]

    def get(self, evid):
        """
        Retrieve an event with evid

        """
        pass

    def put(self, evid):
        pass

    def options(self, evid):
        pass
