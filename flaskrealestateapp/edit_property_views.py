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


bp = Blueprint('edit_property', __name__, url_prefix='/edit_property/')

@bp.route("/<int:property_id>", methods=['GET', 'POST'])
def edit_property(property_id):
    if request.method == 'POST':
        pass
    
    #select all properties
    #all_propertie  s = db.properties.find()
    
    #get property from db using id
    property = db.find({id:property_id})

    return render_template('edit-property.html', property=property)
