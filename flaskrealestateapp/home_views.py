from flask import (Blueprint, render_template, request, flash, redirect, url_for)
from flask import Flask
from pymongo import MongoClient
import gridfs
import os
import base64


#create db client
# client = MongoClient('localhost', 27017)
# #create mongodb database
# db = client.flask_properties
# #create collection
# properties = db.properties
client = MongoClient(os.environ.get("MONGO_URI"))
db = client.flask_properties
properties = db.properties
fs = gridfs.GridFS(db)
bp = Blueprint('home_view', __name__, url_prefix='/')

@bp.route("/", methods=['GET', 'POST'])
def index():
    query = {}

    #all_properties = '' 
    if request.method == 'POST':
        #get search query
        search_query = request.form.get('search_query', '').strip()
        print(search_query)
        if search_query and search_query != '':
            query['address'] = {'$regex': search_query, '$options': 'i'}

        #get form value 
        price_min = (request.form.get('price_min'))
        price_max = (request.form.get('price_max'))
        bedroomNum = (request.form.get('bedroomNum'))
        bathroomNum = (request.form.get('bathNum'))
        
        if search_query:
            query['address'] = search_query

        
        
        
        #if user does not fill filter form
        all_properties = list(db.properties.find())
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
        all_properties = list(db.properties.find(query))
        for property in all_properties:
            image_file = fs.find_one({"property_id": property['id']})
            if image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
                property['image'] = image_data
        
        
        
        return render_template('index1.html', properties=all_properties)
    #select all properties
    all_properties = list(db.properties.find())
    for property in all_properties:
        image_file = fs.find_one({"property_id": property['id']})
        if image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
            property['image'] = image_data

    return render_template('index1.html', properties=all_properties)

@bp.route("/delete/<property_id>", methods=['POST'])
def delete_property(property_id):
    property_id = int(property_id)
    property = properties.find_one({'id': property_id})
    if not property:
        flash("Property not found.", "error")
        return redirect(url_for('home_view.index'))
    
    properties.delete_one({'id': property_id})
    fs.delete(fs.find_one({"property_id": int(property_id)})._id)
    #delete image too
    image = fs.find_one({"property_id": property_id})
    if image:
        fs.delete(image._id)
    flash("Property deleted successfully!", "success")
    return redirect(url_for('home_view.index'))
