from functools import wraps
from flask import g, request, make_response
from werkzeug.exceptions import HTTPException

def api(f):
    """
    Adds response headers to endpoints.
    """
    @wraps(f)
    def endpt(*args,**kwargs):
        resp = make_response(f(*args,**kwargs))
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Content-Length'] = sys.getsizeof(resp)
        return resp
    return endpt
"""
def auth(f):
    '''
    JWT validation.
    '''
    def decorator(f):
        @wraps(f)
        def authorize(*args,**kwargs):
            try:
                token=request.values.get('jwt')
                if _validate_jwt(token):
                    return f(*args,**kwargs)
            except Exception as e:
                log.error('JSON Web Token is not valid. Check token or authorizer function in decorators.py')
                resp = make_response(e, 403)
                resp.headers['Content-Type'] = 'application/json'
                resp.headers['Content-Length'] = sys.getsizeof(resp)
                return resp
            return resp
        return authorize
    return decorator

def admin(f):
    '''
    Admin-only data.
    '''
    def decorator(f):
        @wraps(f)
        def admin(*args,**kwargs):
            try:
                #IMPLEMENT
                print("This should be admin-only.")
                return f(*args,**kwargs)
            except HTTPException as e:
                pass
            return
        return admin
    return decorator
"""
