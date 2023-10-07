from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
@views.route('/safety')
def safety():
    return render_template("safety.html")
@views.route('/map')
def map():
    return render_template("map.html")