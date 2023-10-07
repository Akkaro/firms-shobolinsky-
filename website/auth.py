from flask import Blueprint
from . import Database as db
import json
from bson import json_util

auth = Blueprint('auth', __name__)


def parse_json(data):
    return json.loads(json_util.dumps(data))


@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign up</p>"

@auth.route('/Database')
def Database():
    return parse_json(db.GetDataFromDb())
