import abc
import arrow
import collections
from typing import Tuple, List
from cue import _check_suri_format, CueAPIResourceCreationError
from marshmallow import Schema, fields

Traq = collections.namedtuple('Traq', ['suri', 'P'])
DynaQ = List[Traq]

class BaseUser(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, suri, uid, name):
        self.suri=suri
        self.uid=uid
        self.name=name

    @abstractmethod
    def is_active(self):
        return False

    @abstractmethod
    def is_host(self):
        return False

    def __repr__(self):
        return '<User(suri={self.suri!r},uid={self.uid!r})>'.format(self=self)

class Host(BaseUser):
    
    def __init__(self, user, event):
        super(Host, self).__init__(user.suri, user.uid, user.name)
        self.event=event

    def is_active(self):
        return True

    def is_host(self):
        return False

class Attendee(BaseUser):
    
    def __init__(self, user, event):
        super(Attendee, self).__init__(user.suri, user.uid, user.name)
        self.event=event

    def is_active(self):
        return True

    def is_host(self):
        return False


class Inactive(BaseUser):

    def __init__(self, user):
        super(Inactive, self).__init__(user.suri, user.uid, user.name)

    def is_active(self):
        return False


class Event(object):
    
    def __init__(self, evid, name, host):
        self.evid=evid
        self.name=name
        self.host=host # TODO verify host is valid suri

    def _check_activity(self):
        return

    def __repr__(self):
        return '<Event(evid={self.evid})>'.format(self=self)

    def __deinit__(self):
        '''
        When the event is deleted (by user or time )
        '''
        pass

class Cue(object):
    
    def __init__(self, cid, evid):
        self.cid=cid
        self.evid=evid
        self.next=None
        self.queue=None # TODO experiment with data structures to maintain list of Tracks

def _setup_db(sesh):
    # check if db configured already
    sesh.row_factory=ordered_dict_factory
    # create keyspace 
    sesh.execute("""
        CREATE KEYSPACE IF NOT EXISTS v0
        WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 }'
    """)
    # create tables
    '''
    EVENTUAL OPTIMIZATION
    sesh.execute("""
        CREATE_TABLE IF NOT EXISTS v0.users_by_suri (
            (suri text, (uid uuid, active boolean)) PRIMARY_KEY,
            name text
        )
    """)
    sesh.execute("""
        CREATE_TABLE IF NOT EXISTS v0.users_by_uid (
            (uid uuid, (suri text, active boolean)) PRIMARY_KEY,
            name text
        )
    """)
    '''
    sesh.execute("""
        CREATE_TABLE IF NOT EXISTS v0.users (
            uid uuid PRIMARY_KEY,
            suri text,
            active boolean,
            name text
        )
    """)
    sesh.execute("""
       CREATE_TABLE IF NOT EXISTS v0.events (
            evid uuid PRIMARY_KEY,
            host tuple<uuid, text>,
            cid uuid,
            pin int,
            np text,
            attendees list<tuple<uuid, text>>,
            created_at datetime,
            ended_at datetime
        )
    """)
    sesh.execute("""
        CREATE_TABLE IF NOT EXISTS v0.cues (
            cid uuid PRIMARY_KEY,
            evid uuid,
            on_deck text,
            queue list<tuple<text, double>>
        )
    """)
    create_event=sesh.prepare("INSERT INTO v0.events (evid, host) VALUES (?, ?)")
    create_cue=sesh.prepare("INSERT INTO v0.cues (cid, evid) VALUES (?, ?)")
    
    prepared_stmts = {}

    return sesh, prepared_stmts

class UserSchema(Schema):
    uid=fields.Int()
    suri=fields.Str()
    name=fields.Str()
    active=fields.Bool()
    host=fields.Bool()
    evid=fields.Int()

class EventSchema(Schema):
    evid=fields.Int()
    host=fields.Str()
    pin=fields.Int()

class CueSchema(Schema):
    cid=fields.Int()
    playing=fields.Str()
    next=fields.Str()
    seed=fields.Str()

class TrackSchema(Schema):
    tid=fields.Int()
    cue=fields.Int()
    index=fields.Float()
    
class ResponseSchema(Schema):
    code=fields.Int()
    message=fields.Str()