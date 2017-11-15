import collections
import typing
import logging
from api.v0.decorators import api
from cassandra.cqlengine import columns as cql
from cassandra.cqlengine import connection
from cassandra.cqlengine.models import Model
from flask_restful import Resource, fields

log = logging.getLogger('cue-api.cue')
connection.setup(['db'], "cqlengine", protocol_version=3)

class CueModel(Model):
    """
    Each event has one and only one cue.
    This model interfaces with the Cassandra session.
    """
    cid = cql.UUID(primary_key=True, required=True, default=uuid.uuid4)
    evid = cql.UUID(required=True),
    next = cql.Text()
    nextnext = cql.Text()
    queue = cql.List(value_type=cql.Map(key_type=cql.Text(),value_type=cql.Double()), required=True)
    calibrated = cql.Boolean()

class CueDataFields:
    """Fields representing formatted output data from flask-restful 'Resource'."""
    cue_data_fields = {
        'cid': fields.String,
        'evid': fields.String,
        'next': fields.String,
        'nextnext': fields.String,
        'private': fields.Boolean,
        'np': fields.String
    }

"""
Cue management functions.
"""

class CueAPI(Resource):
    """
    From Flask-Restful, a REST API for cue table.
    This table will be really active, at peak app usage.
    """
    decorators=[api]

    def get(self, cid):
        return '{"Hello."}'

    def put(self, cid):
        pass

    def options(self):
        pass


Traq = collections.namedtuple('Traq', ['suri', 'P'])
DynaQ = typing.List[Traq]