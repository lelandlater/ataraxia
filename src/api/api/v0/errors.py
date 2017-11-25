import logging

__author__ = 'gh()st'

log = logging.getLogger('cueapi')
"""
Cue API error codes
-------------------
0   success
70  generic creation error
35  
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
        log.error("internal error recorded")

class CueAPIRequestError(Error):
    def __init__(self, message, code=255):
        super(Error, self).__init__(message)
        self.code=code
        log.error("error with requested resource")

class CueAPIResourceCreationError(Error):
    def __init__(self, message, code=70):
        super(Error, self).__init__(message)
        self.code=code
        log.error("error creating a resource, probably with a POST request")

class CueAPIResourceRetrievalError(Error):
    def __init__(self, message, code=35):
        super(Error, self).__init__(message)
        self.code=code
        log.error("error retrieiving a resource, probably with a GET request")