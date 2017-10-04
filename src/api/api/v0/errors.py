from . import log
"""
Application logic for Cue AKA "the guts" of the weighted playlist.

Cue API error codes
-------------------
0   success
10  invalid authorization
14  user does not exist
32  already exists
33  user already exists
41  could not create JWT
50  did not authorize JWT
...
156 Can't connect to the backend
...
255 generic error
"""

class Error(Exception):
    def __init__(self, message):
        super(Exception, self).__init__()
        self.message=message

class CueAPIRequestError(Error):
    def __init__(self, message, code=255):
        super(Error, self).__init__(message)
        self.code=code

class CueAPIResourceCreationError(Error):   # <-- I am badly recycling code here; how do I fix it?
    def __init__(self, message, code=32):
        super(Error, self).__init__(message)
        self.code=code

class JWTCreationError(Error):
    def __init__(self, message, code=41):
        super(Error, self).__init__(message)
        self.code=code

class ClientAuthorizationError(Error):
    def __init__(self, message, code=50):
        super(Error, self).__init__(message)
        self.code=code

class CannotConnectToBackendError(Error):
    def __init__(self, message="Cannot connect to the database endpoint. Check CueAPIDatabase.session in database.py", code=156):
        super(Error, self).__init__(message)
        self.code=code