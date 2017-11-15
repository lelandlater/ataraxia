import logging
from api.v0.decorators import api
from api.v0 import db
from api.v0.errors import *
from cassandra.cqlengine import columns as cql
from cassandra.cqlengine import connection
from cassandra.cqlengine.models import Model
from flask import make_response
from flask_restful import fields, Resource

log = logging.getLogger('cue-api.user')
connection.setup(['cassandra']), "cqlengine", protocol_version=3)

class UserBySuriModel(Model):
     """Cassandra data model for user table with Spotify URI as partition key."""
     suri = cql.Text(primary_key=True)
     uid = cql.UUID()
     active = cql.Boolean()
     name = cql.Text()
     joined_at = cql.DateTime()

class UserByUidModel(Model):
    """Cassandra data model for user table with Cue user id as primary key."""
    uid = cql.UUID(primary_key=True)
    suri = cql.Text()
    active = cql.Boolean()
    name = cql.Text()
    joined_at = cql.DateTime()

class UserDataFields:
    """Fields representing formatted output data from flask-restful 'Resource'."""
    user_data_fields = {
        'uid': fields.String, 
        'suri': fields.String, 
        'name': fields.String, 
        'active': fields.Boolean
    }
def _validate_suri_regex():
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
    #IMPLEMENT
    return False

 def _user_exists_with_uid(uid):
    # IMPLEMENT
    return False

 def _retrieve_all_users():
    return

 def _retrieve_user_with_uid(uid):
    return -1

 class UserAPI(Resource):
      """
      From Flask-Restful, a REST API for user table.
      """
      decorators=[api]    

     def get(self, uid):
          """
          :param: user UUID
          """
          # sanitize input
          log.debug('Retrieving a user with uid {0}'.format(uid))
          if not _valid_uid_regex(uid):
              raise CueAPIResourceRetrievalError("Improperly formated uid called on /user")
          if not _user_exists_with_uid(uid):
              raise UserDoesNotExist("No")    
  
     def put(self, uid):
        pass    

    def options(self):
        pass