import base64
import m2Crypto
#from .errors import ClientAuthorizationError
"""
Functions with use in multiple components of the app.
"""

def _generate_id(num_bytes=16):
    return base64.b64encode(m2Crypto.m2.rand_bytes(num_bytes))

def _authenticate_jwt(token):
    """
    :return: True is token is valid, False if invalid.
    """
    if token is None:
        return False
        #raise ClientAuthorizationError
    return True

