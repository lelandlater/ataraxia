from cassandra.cqlengine.columns import Text, Boolean, UUID, \
    DateTime
from cassandra.cqlengine.models import Model
from flask-restful import Resource
from ..database import db
from ..decorators import 
from ..errors import CueAPIResourceCreationError

class CueUser:
    """Representations and utlities of a Cue user."""
    
    class UserBySuriModel(Model):
        """Cassandra data model for user table with Spotify URI as partition key."""
        suri = Text(primary_key=True)
        uid = UUID()
        active = Boolean()
        name = Text()
        joined_at = DateTime()

    class UserByUidModel(Model):
        """Cassandra data model for user table with Cue user id as primary key."""
        uid = UUID(primary_key=True)
        suri = Text()
        active = Boolean()
        name = Text()
        joined_at = DateTime()

    class UserDataFields(object):
         """Fields representing formatted output data from flask-restful 'Resource'."""
        user_data_fields = {
            'uid' = fields.String,
            'suri'= fields.String,
            'name' = fields.String,
            'active' = fields.Boolean
        }

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

    def _validate_suri(suri):
        """
        Validate the Spotify unique identifier as belonging to a user.

        :return boolean TODO what is a valid suri? check spotify
        """
        res=re.match('[a-z0-9][a-z0-9-]{0,31}:', suri)
        ### IMPLEMENT
        if res:
            return True
        return False

    def _user_exists_with_suri(suri):
        #IMPLEMENT
        return False

    def _user_exists_with_uid(uid):
        # IMPLEMENT
        return False

    def _get_all_users():
        pass

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

    class UserAPI(Resource):
        """flask-restful resource: HTTP methods interacting with backend.

        AKA "The Python API"

        """
        decorators=[decorators.api,decorators.auth]

        def get(self):
            """
            Return all Cue users.
            """
            resp.set_data(_get_all_users())


        def get(self, inp):
            """
            :param: user UUID
            """
            resp = make_response(_get_user_by_uid(uid))
            return resp

