from cassandra.cqlengine.columns import Boolean, UUID, Map, \
    DateTime, TimeUUID, Integer
from cassandra.cqlengine.models import Model
from marshmallow import Schema, fields

class Event(Model):
    """
    Each event has exactly one host and exactly one cue.
    Each each event has a set of users (attendees) unique amongst all users.
    This model interfaces with the Cassandra session.
    """
    evid = UUID(primary_key=True, required=True)
    host = Map(key_type=UUID(),value_type=Text()), required=True)
    name = Text()
    cid = UUID(required=True)
    pin = Integer()
    np = Text()
    attendees = Setz(value_type=Map(key_type=UUID(),value_type=Text()), required=True)
    created_at = DateTime(required=True),
    ended_at = DateTime
    last_active = TimeUUID(required=True)

class EventSchema(Schema):
    evid=fields.Int(dump_only=True)
    host=fields.Str()
    pin=fields.Int()