import logging
import json
import requests

import api.v0.util

from api.v0.decorators import api
from api.v0.errors import CueAPIResourceRetrievalError, \
                          CueAPIResourceCreationError, \
                          CueAPIRequestError
from cassandra.cqlengine import columns, connection
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.query import DoesNotExist, \
                                      MultipleObjectsReturned, \
                                      LWTException
from flask import make_response                                   
from flask_restful import fields, Resource, marshal

log = logging.getLogger('cue-api.user')
connection.setup(['cassandra'], 'v0', protocol_version=3)

class User(Model):
    """Cassandra data model for user table with Cue user id as primary key."""
    uid = columns.UUID(primary_key=True)
    suri = columns.Text()
    active = columns.Boolean()
    name = columns.Text()
    joined_at = columns.DateTime()

user_fields = {
    'uid': fields.String, 
    'suri': fields.String, 
    'name': fields.String, 
    'active': fields.Boolean
}

def _retrieve_user(uid):
    """
    :param uid, a Cue user id
    :return user, returned as a cqlengine Model (None if not found)
    """
    if not util.validate_uuid(uid):
        log.error("{} is not a valid uuid".format(uid))
        raise CueAPIResourceRetrievalError("invalid uuid called on /user")
    try:
        user = User.get(uid=uid)
    except DoesNotExist as e:
        log.info("user with suri {} does not exist".format(suri))
        log.error(e)
        user = None
    except MultipleObjectsReturned as e:
        log.info("more than one user exists with suri {}".format(suri))
        log.error(e)
        user = None
    return user

def _create_user(suri):
    """
    :param string, Spotify resource identifier
    :return cqlengine.models.Model or None
    """
    uid = util.generate_uuid()
    now = time.time()
    name = 'Leland' #spotify: query for username by suri =requests.get("")
    try:
        User.if_not_exists().create(uid=uid, suri=suri, name=name, active=False, joined_at=now)
    except LWTException as e:
        log.error(e)
    return json.loads({'user': "this is a user"})

def _update_user(uid, active=None):
    """
    Change user attributes (in particular, 'active')
    :param uuid, a Cue user uid
    :return cqlengine.models.Model or None
    """
    #if field does not exist in data, do not alter it
    #if field is empty string, set it to false
    #return the user when done, with updated values
    pass

class UserAPI(Resource):
    """
    REST API for user table
    """
    decorators=[api]

    def get(self, uid):
        """
        :param uid, a CueUser uuid
        :return JSON response
        """
        # distill incoming data...
        log.debug("retrieving a user with uid {}".format(uid))
        user = _retrieve_user(uid)
        if user is None:
            raise CueAPIResourceRetrievalError("could not retrieve /user with uid {}".format(uid))
        return marshal(user, UserFields.user_fields, envelope='data')

    def post(self, suri, **kwargs):
        """
        Create a new user
        :param suri, 
        """
        log.debug("creating a user with suri {}".format(suri))
        user = _create_user(suri)
        if user is None:
            raise CueAPIResourceCreationError("user with suri {} already exists".format(suri))
        return marshal(user, user_fields, envelope='data')

    def put(self, uid, **kwargs):
        """
        - check if user exists
        - if so, alter the data fields as described in request.data
        - if not, and the requesite 
        """
        #parse request args
        u = _update_user(uid, **kwargs)
        return u

    def options(self):
        """
        Describe API functionality
        """
        r = make_response()
        r.headers['Allow'] = "['GET', 'POST', 'PUT', 'OPTIONS']"
        return r