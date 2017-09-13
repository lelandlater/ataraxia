import abc
import arrow
import collections
import re
from typing import Tuple, List
from marshmallow import Schema, fields

Traq = collections.namedtuple('Traq', ['suri', 'P'])
DynaQ = List[Traq]

class BaseUser(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, suri, uid, name, auth=None):
        self.suri=suri
        self.uid=uid
        self.name=name
        self.auth=auth

    @abc.abstractmethod
    def is_active(self):
        return False

    @abc.abstractmethod
    def is_host(self):
        return False

    def __repr__(self):
        return '<User(suri={self.suri},uid={self.uid})>'.format(self=self)

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
        return '<Event(evid={self.evid},name)>'.format(self=self)

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

def _validate_suri(suri):
    res=re.search('[a-z0-9][a-z0-9-]{0,31}:', suri) # TODO run tests on this regex for Spotidy URNs
    if res:
        return True
    return False

class UserSchema(Schema):
    uid=fields.Int(dump_only=True)
    suri=fields.Str()
    name=fields.Str()
    active=fields.Bool()
    host=fields.Bool()
    evid=fields.Int(dump_only=True)

class EventSchema(Schema):
    evid=fields.Int(dump_only=True)
    host=fields.Str()
    pin=fields.Int()

class CueSchema(Schema):
    cid=fields.Int(dump_only=True)
    playing=fields.Str()
    next=fields.Str()
    seed=fields.Str()

class TrackSchema(Schema):
    tid=fields.Int(dump_only=True)
    cue=fields.Int()
    index=fields.Float()
    
class ResponseSchema(Schema):
    code=fields.Int()
    message=fields.Str()