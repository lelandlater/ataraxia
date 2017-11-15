import base64
#import m2crypto
import uuid

"""
Functions with use in multiple components of the app.
"""

def generate_id(num_bytes=16):
    #return base64.b64encode(m2crypto.m2.rand_bytes(num_bytes))
    return uuid.uuid4()

def validate_uuid(str):
    m=re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
    r=m.match(str)
    return bool(r)


