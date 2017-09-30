import collections
from cassandra.cqlengine.columns import Boolean, Double, Text, \
    Tuple, List, UUID
from marshmallow import Schema, fields
from typing import Tuple, List
from .decorators import api, auth

# models
class Cue(Model):
    """
    Each event has one and only one cue.
    This model interfaces with the Cassandra session.
    """
    cid = UUID(primary_key=True, required=True)
    evid = UUID(required=True),
    next = Text()
    nextnext = Text()
    queue = List(value_type=Map(key_type=UUID(),value_type=Double())
    calibrated = Boolean()

# helper functions


# python objects for logic

Traq = collections.namedtuple('Traq', ['suri', 'P'])
DynaQ = List[Traq]

class CueSchema(Schema):
    cid=fields.Int(dump_only=True)
    playing=fields.Str()
    next=fields.Str()
    seed=fields.Str()

