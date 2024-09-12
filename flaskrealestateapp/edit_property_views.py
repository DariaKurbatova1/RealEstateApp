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

bp = Blueprint('edit_property', __name__, url_prefix='/edit_property/')

@bp.route("/", methods=['GET', 'POST'])
def edit_property():
    if request.method == 'POST':
        #insert property
        #properties.insert_one({'content': 'hello'})
        pass
    
    #select all properties
    #all_properties = db.properties.find()

    return render_template('edit-property.html')
