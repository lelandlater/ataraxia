from functools import wraps
from flask import g, request, make_response
from .errors import ClientAuthorizationError
from .util import _authenticate_jwt

def api(f):
    """
    Adds response headers to endpoints.
    """
    def decorator(f):
        @wraps(f):
        def endpt(*args,**kwargs):
            resp = make_response(f(*args,**kwargs))
            resp.headers['Content-Type'] = 'application/json'
            resp.headers['Content-Length'] = sys.getsizeof(resp)
            return resp
        return endpt
    return decorator

def auth(f):
    """
    JWT validation.
    """
    def decorator(f):
        @wraps(f):
        def authorize(*args,**kwargs):
            try:
                token=request.values.get('jwt')
                if _validate_jwt(token):
                    return f(*args,**kwargs)
            except ClientAuthorizationError as e:
                log.error('JSON Web Token is not valid. Check token or authorizer function in decorators.py')
                resp = make_response(e, 403)
                resp.headers['Content-Type'] = 'application/json'
                resp.headers['Content-Length'] = sys.getsizeof(resp)
                return resp
            return resp
        return authorize
    return decorator

