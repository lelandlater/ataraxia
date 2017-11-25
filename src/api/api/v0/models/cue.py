import collections
import typing
import logging
from api.v0.decorators import api
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.models import Model
from flask_restful import Resource, fields

log = logging.getLogger('cue-api.cue')
connection.setup(['cassandra'], 'v0', protocol_version=3)

Traq = collections.namedtuple('Traq', ['suri', 'P']) # add more variable
DynaQ = typing.List[Traq]

class CueModel(Model):
    """
    Each event has one and only one cue.
    This model interfaces with the Cassandra session.
    """
    cid = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    evid = columns.UUID(required=True),
    next = columns.Text()
    nextnext = columns.Text()
    queue = columns.List(value_type=columns.Map(key_type=columns.Text(),value_type=columns.Double()), required=True)
    calibrated = columns.Boolean()

class Queue(fields.Raw):
    """Ordered list of upcoming sets."""
    def format(self, dynaq):
        """
        :param DynaQ
        :return formatted DynaQ
        """
        res={}
        for traq in dynaq:
            res.update(traq[0], traq[1])
        return res

class CueDataFields:
    """Fields representing formatted output data from flask-restful 'Resource'."""
    cue_data_fields = {
        'cid': fields.String,
        'evid': fields.String,
        'next': fields.String,
        'nextnext': fields.String,
        'private': fields.Boolean,
        'np': fields.String,
        'queue': Queue
    }

"""Cue API functions."""

def _retrieve_cue(cid):
    pass

def _update_cue(cid):
    """
    Alter values of a Cue with application logic.
    An empty string sets value to null; None leaves field unchanged.

    Fields that cannot be altered:
    - evid (cid associated at event creation)
    - created
    """
    pass

class CueAPI(Resource):
    """
    From Flask-Restful, a REST API for cue table.
    This table will be really active, at peak app usage.
    """
    decorators=[api]

    @marshal_with
    def get(self, cid):
        return '{"Hello."}'

    def put(self, cid):
        pass

    def options(self):
        pass
