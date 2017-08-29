import arrow
import base64, M2Crypto
import json
import random
#from run import session
from models import User, Event, Cue, Track
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

def _create_user(suri):
    # check if user with same Spotify URI exists
    s_user=session.execute('SELECT * FROM users_by_suri WHERE suri={}'.format(suri))
    if s_user is not None:
        raise CueAPIResourceCreationError
    if s_user is None:
        uid=generate_id()
        unq=session.execute('SELECT * FROM users WHERE uid={}'.format(uid))
        while unq != None:
            uid=generate_id()
            unq=session.execute('SELECT * FROM users WHERE uid={}'.format(uid))
        session.execute('INSERT INTO ')
    return 0

'''
how many prebuilt reads is too many?
'''

def _create_event(name):
    pass

# enforce uniqueness in the result set for 
# - get_user_by_ui()
# - get_user_by_suri()
# - get_next_track()

def _get_user_by_uid(uid):
    # check uid within known bounds
    session.execute('KEYSPACE user')
    session.execute('')

def _get_user_by_suri(suri):
    query=SimpleStatement('SELECT * from users where suri=%s', consistencyconsistency_level=ConsistencyLevel.ONE)
    raise CueAPIRequestError('Failed to get user by suri.', 14)


def _get_event_by_evid(evid):
    session.execute('')

def _check_suri_format(inp):
    """
    @param inp, a Spotify resource identifier
    ---
    
    return False
    """
    return 0

def _add_user_to_event(uid, evid):

