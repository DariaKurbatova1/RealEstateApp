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
        #get form value 
        price_min = request.form['price_min']
        price_max = request.form['price_max']
        bedroomNum = request.form['bedroomNum']
        bathNum = request.form['bathNum']
        squareFeet_min = request.form['squareFeet_min']
        squareFeet_max = request.form['squareFeet_max']
        lotSize_min = request.form['lotSize_min']
        lotSize_min = request.form['lotSize_min']
        #validation
        if (price_min > price_max):
            pass
        if (squareFeet_min > squareFeet_max):
            pass
        if (lotSize_min > lotSize_max):
            pass
        query = {"price": {"$gt": "5000000"}}
        all_properties = properties.find(query)
        
        return render_template('index.html', properties=all_properties)
    #select all properties
    all_properties = db.properties.find()

    return render_template('index.html', properties=all_properties)
