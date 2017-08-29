import abc
import arrow
from cue import _check_suri_format, CueAPIResourceCreationError
from marshmallow import Schema, fields

def _setup_db(sesh):
    # check if db configured already
    sesh.row_factory=ordered_dict_factory
    # create keyspace 
    sesh.execute(
        '''
        CREATE KEYSPACE IF NOT EXISTS v0
        WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 }'
    ''')
    sesh.execute('USE v0')
    # create tables
    sesh.execute(
        '''
        CREATE_TABLE users_by_suri (
            (suri text, (uid uuid, active boolean)) PRIMARY_KEY,
            name text
        )
    ''')
    sesh.execute(
        '''
        CREATE_TABLE users_by_uid (
            (uid uuid, (suri text, active boolean)) PRIMARY_KEY,
            name text
        )
    ''')
   sesh.execute(
       '''
       CREATE_TABLE events_by_evid (
            evid uuid PRIMARY_KEY,
            host text,
            pin int
        )
    ''')
   sesh.execute(
        '''
        CREATE_TABLE cues_by_evid (
            (evid uuid, (cid uuid, next text)) PRIMARY_KEY,
            on_deck text,
            active boolean  
        )
    ''')
   return sesh
   # this is enough to PoC for API now

class BaseUser(object):
    __metaclass__ = abc.ABCMeta

    evid=None
    host=False
    def __init__(self, suri, uid, uname):
        self.suri=suri
        self.uid=uid
        self.uname=uname
        self._active=False
        self._host=False
        _num_users++
        self._joined_at=arrow.now()

    def __repr__(self):
        return '<User(uid={self.uid!r},suri={self.suri!r})>'.format(self=self)

class Host(BaseUser):
    
    # pass in OBJECTS not IDs dummy!
    def __init__(self, ev, u, save_to_playlist=False):
        self.event=ev
        self.event_name=ev.name
        self.user=u

class Event(object):
    '''
    How to generate unique event IDs?

    # need more methods to describe state: "is active" or "is configured" etc...
    '''
    def __init__(self, evid, name, host, save_to_playlist=False):
        self.evid=evid
        self.name=name
        if _check_suri_format(host) != 0:
            raise 
        self.host=host # TODO verify host is valid suri
        self.create_at=arrow.now()
        self.last_active=arrow.now()
        self.played=[]

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
        self.now_playing=None
        self.next=None
        self.queue=None # TODO experiment with data structures to maintain list of Tracks

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