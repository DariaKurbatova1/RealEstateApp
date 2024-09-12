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

bp = Blueprint('home_admin_view', __name__, url_prefix='/admin/')
@bp.route("/", methods=['GET', 'POST'])
def index_admin():
    if request.method == 'POST':
        #insert property
        #properties.insert_one({'content': 'hello'})
        pass
    
    #select all properties
    all_properties = db.properties.find()

    return render_template('index-admin.html', properties=all_properties)

@bp.route("/<int:property_id>", methods=['GET', 'POST'])
def edit_property(property_id):
    if request.method == 'POST':
        pass
    
    #select all properties
    #all_propertie  s = db.properties.find()

    return render_template('edit-property.html', property_id=property_id)