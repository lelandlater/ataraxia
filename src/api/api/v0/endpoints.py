import sys
from models import cue, event, user
from flask import add_url_rule, redirect, make_response, url_for, request
from flask.views import MethodView
from . import decorators.api,decorators.auth

v0 = Blueprint('v0', __name__, url_prefix='/v0')

def index():
    return redirect("https://docs.cue.zone/api", code=301)

class UserAPI(MethodView):
    decorators=[decorators.api,decorators.auth]

    def get(self):
        """
        Return all Cue users.
        """
        resp.set_data(user._get_all_users())


    def get(self, inp):
        """
        :param: user UUID
        """
        resp = make_response(user._get_user_by_uid(uid))
        return resp

    def post(self, uid):
        """
        :param: user Spotify unique identifier
        """
        resp=make_response(cue._get_user_by_suri(uid))        
        resp.headers['Content-Type']='application/json'
        resp.headers['Content-Length']=sys.getsizeof(resp)  
        return resp

    def post(self):
        pass



@v0.route('/events/<uuid:evid>/')
    """
    :param: user 
    """
    if request.method == 'GET':

    resp=make_response(event._get_event_by_evid() 

v0.add_url_rule('/', index)


