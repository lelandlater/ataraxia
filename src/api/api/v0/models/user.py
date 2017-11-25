import logging, re, json, time
from api.v0.decorators import api
from api.v0 import db
from api.v0.util import validate_uuid
from api.v0.errors import CueAPIResourceRetrievalError
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.query import DoesNotExist, MultipleObjectsReturned
from cassandra.cqlengine.models import Model
from flask import make_response
from flask_restful import fields, Resource, marshal_with

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

def _user_exists_with_suri(suri):
    """
    :param suri, a Spotify user resource identifier
    :return boolean
    """
    if not _valid_suri_regex(suri):
        raise CueAPIResourceRetrievalError("Invalid URI called on /user")

def _retrieve_user_with_uid(uid):
    """
    :cql #DO
    :param uid, a Cue user id
    :return user, returned as a cqlengine Model (None if not found)
    """
    if not util.validate_uuid(uid):
        raise CueAPIResourceRetrievalError("Invalid UUID called on /user")
    try:
        user = UserByUid.get(uid=uid)
    except DoesNotExist as e:
        log.info("user with suri {} does not exist".format(suri))
        log.error(e)
        user = None
    except MultipleObjectsReturned as e:
        log.info("more than one user exists with suri {}".format(suri))
        log.error(e)
        user = None
    return user

def _retrieve_user_with_suri(suri):
    """
    :cql SELECT * FROM user_by_suri WHERE suri = ? values (suri) or something...
    :param suri, a Spotify user resource identifier
    :return user, returned as a cqlengine Model (None if not found)
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

    @marshal_with(UserDataFields.user_data_fields)
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

    def post(self):
        """

        """
        pass

    def put(self, uid):
        """
        - check if user exists
        - if so, alter the data fields as described in request.data
        - if not, and the requesite 
        """

    def options(self):
        pass