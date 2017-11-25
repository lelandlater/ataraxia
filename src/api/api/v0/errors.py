import logging

__author__ = 'gh()st'

log = logging.getLogger('cueapi')
"""
Cue API error codes
-------------------
0   success
10  invalid authorization
14  user does not exist
70  generic creation error
33  user already exists
34  user does not exist
35  
41  could not create JWT
50  did not authorize JWT
...
156 Can't connect to the backend
171 Bad query error
...
255 generic error
"""

class Error(Exception):
    def __init__(self, message):
        super(Exception, self).__init__()
        self.message=message

class InternalError(Error):
    def __init__(self, message):
        super(Error, self).__init__(message)
        log.error("Internal error recorded. Error the code you wrote code.")

class CueAPIRequestError(Error):
    def __init__(self, message, code=255):
        super(Error, self).__init__(message)
        self.code=code

class CueAPIResourceCreationError(Error):
    def __init__(self, message, code=70):
        super(Error, self).__init__(message)
        self.code=code
        log.error("Error creating a resource, probably with a POST request.")

class UserAlreadyExists(Error):
    def __init__(self, message, code=33):
        super(Error, self).__init__(message)
        self.code=code

class CueAPIResourceRetrievalError(Error):
    def __init__(self, message, code=35):
        super(Error, self).__init__(message)
        self.code=code
        log.error("Error retrieiving a resource, probably with a GET request.")

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

class BadQueryError(InternalError):
    def __init__(self, message, code=171):
        super(Error, self).__init__(message)
        self.code=code

class StatementNotPreparedError(InternalError):
    def __init__(self, message, code=172):
        super(Error, self).__init__(message)
        self.code = code
        log.error("Error: query statement not prepared on Cassandra db object.")
