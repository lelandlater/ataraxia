import jwt
import logging
from flask import make_response
from flask_restful import Resource
from . import CueAPIRequestError, _add_track_to_cue, _get_user_by_uid, \
                  _get_user_by_suri, _get_cue_by_cid, _get_event_by_evid, \
                  UserSchema, EventSchema, CueSchema, TrackSchema
import sys
# from .. import session -- make sure it's the same session as ../run.py
log = logging.getLogger('cue-api-log')

create_event=session.prepare("INSERT INTO v0.events (evid, host) VALUES (?, ?)")
create_cue=session.prepare("INSERT INTO v0.cues (cid, evid) VALUES (?, ?)")
get_user_by_suri=session.prepare("SELECT * FROM users_by_suri WHERE suri=?")
get_user_by_uid=session.prepare("SELECT * FROM users_by_uid WHERE uid=?")
get_event_by_evid=session.prepare("SELECT * FROM events WHERE evid=?")
get_cid_by_evid=session.prepare("SELECT (cid) FROM events WHERE evid=?")
get_curr_track_by_evid=session.prepare("SELECT (curr_track) FROM events WHERE evid=?")
get_next_track_by_cid
class User(Resource):
    def get(self, suri):
        try:
            resp=make_response(_get_user_by_suri(suri))
        except CueAPIRequestError as e:
            resp=make_reponse(e)
        resp.headers.add['Content-Type']='text/json'
        resp.headers.add['Content-Length']=sys.getsizeof(resp))
        return resp

    def get(self, uid):
        # marshmallow data to User schema
        _get_user_by_uid(uid)
        return True

    def put(self, uid):

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

    def post(self, evid, cid, tid):
        return True

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
    def nothing():
        pass
        
        
        

