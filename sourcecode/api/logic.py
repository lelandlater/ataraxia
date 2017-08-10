import arrow
import json
import random
from run import session
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement
"""
Application logic for Cue AKA "the guts" of the weighted playlist.

Cue API error codes
-------------------
0   success
10  invalid authorization
14 user does not exist
...
255 generic error
"""
# prepare statements for lower CPU utilization

class CueAPIRequestError(Exception):
    def __init__(self, message, code=255):
        super(Error, self).__init__(message)
        self.code=code

def _create_new_user(suri):
    # check if user with same Spotify URI exists
    try:
        user=session.execute("") # CQL
    if user is not None:
        data=json.dumps(
            {'timestamp':arrow.timestamp(),
             'uid':user.uid,           
             'name':user.name,
             'active':user.active}
        )
    session.execute("") # CQL, add user to u table
    return 0

# enforce uniqueness in the result set for 
# - get_user_by_ui()
# - get_user_by_suri()
# - get_

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

