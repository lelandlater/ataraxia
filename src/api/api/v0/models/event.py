from cassandra.cqlengine.columns import Boolean, UUID, Map, \
    DateTime, TimeUUID, Integer
from cassandra.cqlengine.models import Model
from ..util import CueUser

class CueEvent:
    """Respresentations and utilities of a Cue event."""

    class CueUserDataField(fields.Raw):
        """Represents a Cue user as Flask-Restful field."""
        def format(self, uid, suri):
            return "({0}, {1})".format(sui, uid)

    class EventData(object):
    """Returned event data from query."""
    event_data_fields = {
        'evid' = fields.String,
        'host' = CueUser(),
        'name' = fields.String,
        'cid' = fields.String,
        'np' = fields.String,
        'attendees' = fields.List(CueUserDataField()),
        'private' = fields.Boolean
    }

    class EventModel(Model):
        """
        Cassandra data model for event table.

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
        attendees = Set(value_type=Map(key_type=UUID(),value_type=Text()), required=True)
        created_at = DateTime(required=True),
        ended_at = DateTime
        last_active = TimeUUID(required=True)


