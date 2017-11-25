import collections
import typing
import logging, json

import api.v0.util

from api.v0.decorators import api
from api.v0.errors import CueAPIResourceRetrievalError, \
                          CueAPIResourceCreationError, \
                          CueAPIRequestError
from cassandra.cqlengine import columns, connection
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.query import DoesNotExist, \
                                      MultipleObjectsReturned, \
                                      LWTException
from flask import make_response
from flask_restful import Resource, fields, marshal

log = logging.getLogger('cue-api.cue')
connection.setup(['cassandra'], 'v0', protocol_version=3)

Traq = collections.namedtuple('Traq', ['suri', 'P']) #DO
DynaQ = typing.List[Traq]

class Cue(Model):
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

def _retrieve_cue(cid):
    """
    :param uuid, a Cue cue id
    :return cqlengine.models.Model or None
    """
    if not util.validate_uuid(cid):
        log.error("{} is not a valid uuid".format(cid))
        raise CueAPIResourceRetrievalError("invalid uuid called on /cue")
    return json.loads({'cue': "this is a cue"})

def _create_cue(evid):
    """
    :param uuid, a Cue event id 
    :return cqlengine.models.Model or None
    """
    if not util.validate_uuid(evid):
        raise CueAPIResourceCreationError("invalid uuid called on /event")
    try:
        Cue.if_not_exists().create

def _update_cue(cid):
    """
    :param uuid, a Cue cue id
    :return cqlengine.models.Model or None
    """
    pass

class CueAPI(Resource):
    """
    From Flask-Restful, a REST API for cue table.
    This table will be really active, at peak app usage.
    """
    decorators=[api]

    def get(self, cid):
        return json.loads('{"Hello."}')

    def post(self, **kwargs):
        """
        Create a new cue
        """
        pass

    def put(self, cid, **kwargs):
        pass

    def options(self):
        """
        Describe API fucntionality
        """
        r = make_response()
        r.headers['Allow'] = "['GET', 'POST', 'PUT', 'OPTIONS']"
        return r