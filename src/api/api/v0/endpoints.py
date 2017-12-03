import sys
from flask import Blueprint, redirect
from flask_restful import Api
from api.v0.models import user, event, cue

v0 = Blueprint('v0', __name__, url_prefix='/v0')
api = Api(v0)

def index():
    return redirect("https://docs.cue.zone/api", code=301)
    
v0.add_url_rule('/', 'index', index)
api.add_resource(user.UserAPI, '/users', '/users/<uuid:uid>')
api.add_resource(event.EventAPI, '/events', '/events/<uuid:evid>')
api.add_resource(cue.CueAPI, '/cues', '/cues/<uuid:cid>')