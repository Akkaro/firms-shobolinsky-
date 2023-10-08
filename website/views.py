from flask import Blueprint, render_template, redirect

import Database
from mapping_tools.create_map import *
from website.api import add_user_report

from Database import *


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/safety')
def safety():
    return render_template("safety.html")


@views.route('/refress_db')
def refress_db():
    print("in refress_db")
    GetDataFromApi()
    news_feed = GetNewsFromDb()

    return render_template("News.html", news=news_feed)

@views.route('/News')
def News():
    news_feed = GetNewsFromDb()
    return render_template("News.html", news=news_feed)


@views.route('/map')
def map():
    ip=get_ip()
    region=get_region_by_ip(ip)
    code,region=country_code_prep(region)
    data,region=prepare_data(code,region)
    create_map(data,region)
    return render_template("map.html")


@views.route('/report',  methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        add_user_report();
        return render_template("specify.html")
    return render_template("report.html")



