from flask import (Blueprint, render_template, request)
from flaskrealestateapp.property import Property
from flask import Flask
from pymongo import MongoClient

#create db client
client = MongoClient('localhost', 27017)
#create mongodb database
db = client.flask_properties
#create collection
properties = db.properties


bp = Blueprint('sell_view', __name__, url_prefix='/sell/')

@bp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass


    return render_template('sell.html')