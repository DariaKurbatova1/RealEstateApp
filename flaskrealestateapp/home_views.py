from flask import (Blueprint, render_template, request)
# from . import app
from flaskrealestateapp.property import Property
from flask import Flask
from pymongo import MongoClient

#create db client
client = MongoClient('localhost', 27017)
#create mongodb database
db = client.flask_properties
#create collection
properties = db.properties
#

bp = Blueprint('home_view', __name__, url_prefix='/')

@bp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #insert property
        #properties.insert_one({'content': 'hello'})
        pass
    
    property1 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000)
    property2 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000)
    property3 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000)
    
    #select all properties
    all_properties = db.properties.find()

    properties = [property1, property2, property3]
    return render_template('index.html', properties=all_properties)
