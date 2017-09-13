import jwt
import logging
from flask import make_response
from flask_restful import Resource
from . import CueAPIRequestError, \
    UserSchema, EventSchema, CueSchema, TrackSchema, \
    generate_id, _create_user, check_suri_format
import sys

# from .. import session -- make sure it's the same session as ../run.py
req_log = logging.getLogger('cue-api-log.requests')
req_err_log = logging.getLogger('cue-api-log.request-errors')

_create_event=session.prepare("INSERT INTO events (evid, host) VALUES (?, ?)")
_create_cue=session.prepare("INSERT INTO cues (cid, evid) VALUES (?, ?)")
_get_user_by_suri=session.prepare("SELECT * FROM users_by_suri WHERE suri=?")
_get_user_by_uid=session.prepare("SELECT * FROM users_by_uid WHERE uid=?")
_get_events=session.prepare("SELECT (evid, name, created_at) FROM events")
_get_event_by_evid=session.prepare("SELECT * FROM events WHERE evid=?")
_get_cid_by_evid=session.prepare("SELECT (cid) FROM events WHERE evid=?")
_get_curr_track_by_evid=session.prepare("SELECT (curr_track) FROM events WHERE evid=?")
_get_next_track_by_cid=session.prepare("SELECT (next) FROM cues WHERE cid=?")
# TODO in logic.py --> recalibrate_cue(cid)

class User(Resource):
    def get(self, suri):
        try:
            # validate JWT
            query=_get_event_by_evid()
            # marshall to JSON
            resp=make_response(_get_user_by_suri(suri))
        except CueAPIRequestError as e:
            resp=make_reponse(e)
        resp.headers['Content-Type']='text/json'
        resp.headers['Content-Length']=sys.getsizeof(resp))
        return resp

    def get(self, uid): # jwt something
        try:
            # JWT stuff
            resp=make_response(_get_user_by_uid(uid), 200)
        except CueAPIRequestError as e:
            resp=make_reponse(e)
        resp.headers['Content-Type']='text/json'
        resp.headers['Content-Length']=sys.getsizeof(resp))
        return resp

    def put(self, uid, active): 
        try:
           # JWT stuff
        except except CueAPIRequestError as e:
            resp=make_response(e)
        resp.

    def post(self, suri):
        try:
            resp=make_response(_create_user(suri))
        except CueAPIRequestError as e:
        return reps

class Event(Resource):
    def get(self, evid):
        return True

    def post(self, evid, cid, tid):
        return True

    def put(self, evid, cid):
        # change the cue for a given event 
        return True

class Events(Resource):

    def get(self):
        try:
            # something something paginated responses ...
            resp=make_response(_get_events, 200) # paginate repsines to this huge call

    def get(self, evid):
        try:
            resp=make_reponse(_get_event_by_evid(evid), 200)
        except CueAPIRequestError as e:
            resp=make_reponse(e)
        resp.headers.add['Content-Type']='text/json'
        resp.headers.add['Content-Length']=sys.getsizeof(resp))
        return resp


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
        
        
        

