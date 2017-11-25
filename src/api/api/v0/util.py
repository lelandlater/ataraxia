import base64, re
#import m2crypto
import uuid

from flask_restful import fields

"""
Utility methods and classes shared APIs.
"""

class CueUser(fields.Raw):
    """Represents a Cue user as Flask-Restful field."""
    #DO
    def format(self, uid, suri):
        return "({0}, {1})".format(sui, uid)
        
def generate_uuid(num_bytes=16):
    #return base64.b64encode(m2crypto.m2.rand_bytes(num_bytes))
    return uuid.uuid4()

def validate_uuid(str):
    m=re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
    r=m.match(str)
    return bool(r)

def validate_suri(str):
    #DO
    pass
