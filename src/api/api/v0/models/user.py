from cassandra.cqlengine.columns import Text, Boolean, UUID, \
    DateTime
from cassandra.cqlengine.models import Model
from marshmallow import Schema, fields
from .. import session #????
from ..errors import CueAPIResourceCreationError

# models
class UserBySuri(Model):
    suri = Text(primary_key=True)
    uid = UUID()
    active = Boolean()
    name = Text()
    joined_at = DateTime()

class UserByUid(Model):
    uid = UUID(primary_key=True)
    suri = Text()
    active = Boolean()
    name = Text()
    joined_at = DateTime()

# helper functions
def _generate_auth_token(uid):
    """
    Generate an auth token for use with JWT.
    source: https://realpython.com/blog/python/token-based-authentication-with-flask/

    :return string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': uid
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except JWTCreationError as e:
        return e

def _valid_suri(suri):
    """
    Validate the Spotify unique identifier as belonging to a user.

    :return boolean TODO what is a valid suri? check spotify
    """
    res=re.match('[a-z0-9][a-z0-9-]{0,31}:', suri) # TODO implement this <---
    if res:
        return True
    return False

def _user_exists_with_suri(suri):
    # IMPLEMENT
    return False

def _user_exists_with_uid(uid):
    # IMPLEMENT
    return False

# logic methods
"""
def _create_user(suri):
    s_user=session.execute("SELECT * FROM users_by_suri WHERE suri={}".format(suri)
    if s_user is not None: # null or None? type returned by CQL miss on SELECT
        raise CueAPIResourceCreationError("A user with this suri already exists.")
    chk_unique=session.execute("SELECT * FROM users_by_uid WHERE uid={}".format(uid))
    uid=generate_id()
    while chk_unique != None:
        uid=generate_id()
        unq=session.execute("SELECT * FROM users WHERE uid={}".format(uid))
    name='' # Spotify curl based on user
    session.execute("INSERT INTO users_by_suri (suri, uid, name) VALUES ({0}, {1}, {2})".format(suri, uid, name))
    return 0
"""

# formatting
class UserSchema(Schema):
    uid=fields.Int(dump_only=True)
    suri=fields.Str()
    name=fields.Str()
    active=fields.Bool()
    host=fields.Bool()
    evid=fields.Int(dump_only=True)
