import collections
from cassandra.cqlengine.columns import Boolean, Double, Text, \
    Tuple, List, UUID
from typing import Tuple, List # MyPy?

class Cue:
    """Respresentations and utilities of a Cue cue, the foundational 
    datastructure of the Cue app.
    """
    def __init__(self):
        print("A new cue was created.")

    class Cue(Model):
        """
        Each event has one and only one cue.
        This model interfaces with the Cassandra session.
        """
        cid = UUID(primary_key=True, required=True)
        evid = UUID(required=True),
        next = Text()
        nextnext = Text()
        queue = List(value_type=Map(key_type=UUID(),value_type=Double()))
        calibrated = Boolean()

    class CueDataFields(object):
        """Fields representing formatted output data from flask-restful 'Resource'."""
    Traq = collections.namedtuple('Traq', ['suri', 'P'])
    DynaQ = List[Traq]