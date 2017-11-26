import logging

from api.v0.decorators import api
from api.v0.util import generate_uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.models import Model

from flask import make_response
from flask_restful import Resource, fields, marshal

log = logging.getLogger('cue-api.event')
connection.setup(['cassandra'], 'v0', protocol_version=3)

class Event(Model):
    """
    Each event has exactly one host and exactly one cue.
    Each each event has a set of users (attendees) unique amongst all users.
    """
    evid = columns.UUID(primary_key=True, required=True, default=generate_uuid())
    host = columns.UUID(required=True)
    name = columns.Text()
    cid = columns.UUID(required=True)
    secured = columns.Boolean(required=True)
    pin = columns.Integer()
    np = columns.Text()
    attendees = columns.Set(value_type=columns.UUID(), required=True)
    created_at = columns.DateTime(required=True)
    ended_at = columns.DateTime()
    last_active = columns.TimeUUID(required=True)

event_fields = {
    'evid': fields.String,
    'host': util.CueUser(),
    'name': fields.String,
    'cid': fields.String,
    'np': fields.String,
    'attendees': fields.List(CueUserDataField()),
    'private': fields.Boolean,
    'pin': fields.String,
    'created_at': fields.String,
    'last_active': fields.String
}

def _retrieve_event(evid):
    """
    :param uuid, a Cue event id
    :return cqlengine.models.Model or None
    """
    if not util.validate_uuid(evid):
        raise CueAPIRetrievalError("invalid uuid called on /event")
    try:
        event = Event.get(evid=evid)
    except DoesNotExist as e:
        log.info("event with evid {} does not exist".format(evid))
        log.error(e)
        event = None
    except MultipleObjectsReturned as e:
        log.info("more than one event exists with evid {}".format(evid))
        log.error(e)
        event = None
    return event

def _create_event(name, secured=False):
    """
    :return cqlengine.models.Model or None
    """
    evid = util.generate_uuid()
    now = time.time()
    pass

def _update_event(evid):
    """
    :param uuid, a Cue event id
    :return cqlengine.models.Model or None
    """
    return -1

class EventAPI(Resource):
    """
    From Flask-Restful, a REST API for event table.
    """
    decorators=[api]

    def get(self, evid):
        """
        Retrieve an event with evid
        :param
        """
        return marshal(event, event_fields)

    def post(self):
        """
        Create a new even
        :param string, and event id
        :return cqlengine.models.Model or None
        """
        log.debug("creating a new event @ {}".format(time.time()))
        event = _create_event()

    def put(self, evid):
        pass

    def options(self, evid):
        """
        Describe API functionality
        """
        r = make_response()
        r.headers['Allow'] = "['GET', 'POST', 'PUT', 'OPTIONS']"
        return r