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
        query = {}

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
        if price_min:
            query['price'] = query.get('price', {})
            query['price']['$gte'] = int(price_min)
        if price_max:
            query['price'] = query.get('price', {})
            query['price']['$lte'] = int(price_max)
        if bedroomNum:
            query['bedroomNum'] = {'$gte': int(bedroomNum)}
        if bathroomNum:
            query['bathroomNum'] = {'$gte': int(bathroomNum)}

        #find properties matching query
        all_properties = properties.find(query)
        
        
        
        
        return render_template('index1.html', properties=all_properties)
    #select all properties
    all_properties = db.properties.find()

    return render_template('index1.html', properties=all_properties)
