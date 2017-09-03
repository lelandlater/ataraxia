import arrow
import base64, M2Crypto
import json
import random
import typing
from models import Host, Attendee, Inactive, Event, Cue, Track
from . import session
from cassandra import ConsistencyLevel
"""
Application logic for Cue AKA "the guts" of the weighted playlist.

Cue API error codes
-------------------
0   success
10  invalid authorization
14  user does not exist
32  already exists
33  user already exists
...
255 generic error
"""
# prepare statements for lower CPU utilization
# how do I get the session object into ./resources.py ?
class Error(Exception):
    def __init__(self, message):
        super(Exception, self).__init__()
        self.message=message

class CueAPIRequestError(Error):
    def __init__(self, message, code=255):
        super(Error, self).__init__(message)
        self.code=code

class CueAPIResourceCreationError(Error):
    def __init__(self, message, code=32):
        super(Error, self).__init__(message)
        self.code=code

def generate_id(num_bytes=16):
    return base64.b64encode(m2Crypto.m2.rand_bytes(num_bytes))

def _create_user(suri) -> int:
    s_user=session.execute("SELECT * FROM users_by_suri WHERE suri={}".format(suri)
    if s_user is not None: # null or None? type returned by CQL miss on SELECT
        raise CueAPIResourceCreationError
    uid=generate_id()
    chk_unique=session.execute("SELECT * FROM users_by_uid WHERE uid={}".format(uid))
    while chk_unique != None:
        uid=generate_id()
        unq=session.execute("SELECT * FROM users WHERE uid={}".format(uid))
    name='' # Spotify curl based on user
    session.execute("INSERT INTO users_by_suri (suri, uid, name) VALUES ({0}, {1}, {2})".format(suri, uid, name))
    session.execute
    return 0

'''
how many prebuilt reads is too many?
'''

def _create_event(name):
    pass

# enforce uniqueness in the result set for 
# - get_user_by_ui()
# - get_user_by_suri()
# - get_next_track_from_cue()

def _get_all_users():
    users=session.execute("SELECT * FROM users")
    return users

def _get_user(uid):
    session.execute('')

def _get_event_by_evid(evid):
    session.execute('')

def _check_suri_format(inp):
    """
    @param inp, a Spotify resource identifier
    ---
    
    return False
    """
    return 0

def _add_user_to_event(uid, suri, evid):
        session.execute("UPDATE v0.events SET attendees = attendees + [({}, {})] WHERE evid={}".format(uid, suri, evid)
