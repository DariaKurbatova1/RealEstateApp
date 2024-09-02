from flask import (Blueprint, render_template, request, redirect, url_for)
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
def sell_property():
    if request.method == 'POST':
        offerType = request.form['offerType']
        type = request.form['type']
        price = request.form['price']
        address = request.form['address']
        bedroomNum = request.form['bedroomNum']
        bathroomNum = request.form['bathroomNum']
        squareFeet = request.form['squareFeet']
        lotSize = request.form['lotSize']
        properties.insert_one({
            'offerType': offerType,
            'type': type,
            'price': price,
            'address': address,
            'bedroomNum': bedroomNum,
            'bathroomNum': bathroomNum,
            'squareFeet': squareFeet,
            'lotSize': lotSize
        })
        return redirect(url_for('home_view.index'))


    return render_template('sell.html')