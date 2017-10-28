import sys
from models import cue, event, user
from flask import add_url_rule, redirect, make_response, url_for, request
from flask-restful import Resource, fields, marshal_with

from . import decorators.api,decorators.auth

v0 = Blueprint('v0', __name__, url_prefix='/v0')

def index():
    return redirect("https://docs.cue.zone/api", code=301)

v0.add_url_rule('/', index)



