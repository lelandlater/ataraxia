from flask_restful import Resource
from logic import CueAPIRequestError, _add_track_to_cue, _get_user_by_uid, _get_user_by_suri, _get_cue_by_cid, _get_event
from schemas import UserSchema, EventSchema, CueSchema, TrackSchema
from werkzeug.datastructures import Headers, CallbackDict
from run import log
import sys

class User(Resource):
    def get(self, suri):
        try:
            resp=_get_user_by_suri(suri)
        except CueAPIRequestError as e:
            resp=
        d=Headers()
        d.add('Content-Type', 'text/json')
        d.add('Content-Length', sys.getsizeof(resp))

    def get(self, uid):
        # marshmallow data to User schema
        _get_user_by_uid(uid)
        return True

    def post(self, suri):
        try:
            _create_new_user(suri)
        except CueAPIRequestError as e:
            print("FAILURE! code: {0}".format(e.code))
            exit(0)
        return 200

class Event(Resource):
    def get(self, evid):
        return True

    def post(self, evid, cid, tid )
    def put(self, evid, cid):
        # change the cue for a given event 
        return True

class Events(Resource):

    def get(self, evid):
        _get_event(evid)

class Cue(Resource):
    """
    A weighted list of tracks.
    - Every event has a single unique cue.
    - After every post, rebalances.
    - Data for the current track, on deck track.
    - Weigh
    """
    def get(self, cid):
       _get_cue_by_cid(cid)
       return "cue %d" % cid
    
    def put(self, cid, track):
        # access
        try:
            _add_track_to_cue(cid, track)
        except CueAPIRequestError as e:
            print("FAILURE! code: {0}".format(e.code))
            exit(0)
        return 0

class Track(Resource):
    def get(self, tid):
        ()
        
        
        

