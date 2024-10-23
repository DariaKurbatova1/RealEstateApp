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
    all_properties = '' 
    if request.method == 'POST':
        #get form value 
        price_min = (request.form['price_min'])
        price_max = (request.form['price_max'])
        bedroomNum = (request.form['bedroomNum'])
        bathroomNum = (request.form['bathNum'])
        #validation
        if (price_min == '#'):
            pass
        
        #if user does not fill filter form
        all_properties = db.properties.find()
        #if user inputs a min price
        if (price_min and price_max is None):
            price_min = int(price_min)
            query = {'price': {'$gt': price_min}}
            print(query)
            all_properties = properties.find(query)
            print(all_properties[0])
        #if user inputs a max price
        if (price_max and price_min is None):
            price_max = int(price_max)
            query = {'price': {'$lt': price_max}}
            print(query)
            all_properties = properties.find(query)
            print(all_properties[0])
        #if user inputs a min price and max price
        if (price_min and price_max):
            price_min = int(price_min)
            price_max = int(price_max)
            query = {'$and': [{'price': {'$gt': price_min},'price': {'$lt': price_max}}]}
            print(query)
            all_properties = properties.find(query)
            print(all_properties[0])
        
        #if user inputs min num of bedrooms
        if (bedroomNum):
            bedroomNum = int(bedroomNum)
            print(bedroomNum)
            query = {'bedroomNum': {'$gte': bedroomNum}}
            print(query)
            all_properties = properties.find(query)

        #if user inputs min num of bathrooms
        if (bathroomNum):
            bathroomNum = int(bathroomNum)
            query = {'bathroomNum': {'$gte': bathroomNum}}
            print(query)
            all_properties = properties.find(query)
            print(all_properties[0])
        
        
        
        
        return render_template('index.html', properties=all_properties)
    #select all properties
    all_properties = db.properties.find()

    return render_template('index.html', properties=all_properties)
