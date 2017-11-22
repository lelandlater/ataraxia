import logging
import re, json
from api.v0.decorators import api
from api.v0 import db
from api.v0.util import validate_uuid
from api.v0.errors import UserDoesNotExist, CueAPIResourceRetrievalError
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.query import DoesNotExist, MultipleObjectsReturned
from cassandra.cqlengine.models import Model
from flask import make_response
from flask_restful import fields, Resource

log = logging.getLogger('cue-api.user')
connection.setup(['cassandra'], 'v0', protocol_version=3)

class UserBySuri(Model):
     """Cassandra data model for user table with Spotify URI as partition key."""
     suri = columns.Text(primary_key=True)
     uid = columns.UUID()
     active = columns.Boolean()
     name = columns.Text()
     joined_at = columns.DateTime()

class UserByUid(Model):
    """Cassandra data model for user table with Cue user id as primary key."""
    uid = columns.UUID(primary_key=True)
    suri = columns.Text()
    active = columns.Boolean()
    name = columns.Text()
    joined_at = columns.DateTime()

class UserDataFields:
    """Fields representing formatted output data from flask-restful 'Resource'."""
    user_data_fields = {
        'uid': fields.String, 
        'suri': fields.String, 
        'name': fields.String, 
        'active': fields.Boolean
    }
def _valid_suri_regex(suri):
    """
    Validate the Spotify unique identifier as belonging to a user.

    :return: boolean TODO what is a valid suri? check spotify
    """
    res=re.match('[a-z0-9][a-z0-9-]{0,31}:', suri)
    #IMPLEMENT
    if res:
      return True
    return False

def _valid_uid_regex(uid):
    """
    Ensure uid is valid regex.

    :return: bool
    """
    return util.validate_uuid(uid)

def _user_exists_with_suri(suri):
    if not _valid_suri_regex(suri):
        raise CueAPIResourceRetrievalError("Improperly formatted uid called on /user")
    if _retrieve_user_with_suri(suri) is None:
        raise UserDoesNotExist("No")
    return True

def _retrieve_all_users():
    return UserByUid.ob

def _retrieve_user_with_uid(uid):
    return -1

def _retrieve_user_with_suri(suri):
    """
    :cql SELECT * FROM user_by_suri WHERE suri = ? values (suri) or something...
    :param suri, a Spotify user resource identifier
    :return user, returned as a cqlengine Model
    """
    try:
        user = UserBySuri.get(suri=suri)
    except DoesNotExist as e:
        log.info("user with suri {} does not exist".format(suri))
        log.error(e)
        user = None
    except MultipleObjectsReturned as e:
        log.info("more than one user exists with suri {}".format(suri))
        log.error(e)
        user = None
    return user

class UserAPI(Resource):
    """
    From Flask-Restful, a REST API for user table.
    """
    decorators=[api]

    def get(self, uid):
        """
        :param uid, a CueUser uuid
        :return JSON response
        """
        # marshall incoming data...
        log.debug('Retrieving a user with uid {0}'.format(uid))
        user = _retrieve_user_with_uid(uid)
        if user is None:
            raise CueAPIResourceRetrievalError("Could not retrieve /user with uid ".format(uid))
        # marshal user
        return json.loads(user)

     def put(self, uid):
         pass

     def options(self):
         pass