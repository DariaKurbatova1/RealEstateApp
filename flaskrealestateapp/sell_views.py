from flask import (Blueprint, render_template, request, redirect, url_for, flash)
from flaskrealestateapp.property import Property
from flask import Flask
from pymongo import MongoClient
from werkzeug.utils import secure_filename

import os

#create db client
client = MongoClient('localhost', 27017)
#create mongodb database
db = client.flask_properties
#create collection
properties = db.properties

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


bp = Blueprint('sell_view', __name__, url_prefix='/sell/')

@bp.route("/", methods=['GET', 'POST'])
def sell_property():
    if request.method == 'POST':
        try:
            #get the id of newly inserted record
            new_id = (db.properties.count_documents({}))+1
            #get form value and insert new record
            offerType = request.form.get('offerType')
            if not offerType:
                flash("Offer type is required.")
            type = request.form.get('type')
            if not type:
                flash("Type is required.")
            price = int(request.form.get('price'))
            if price <= 0:
                flash("Price must be a positive number.")
                return redirect(request.url)
            address = request.form.get('address')
            if not address:
                flash("Address is required.")
                return redirect(request.url)
            bedroomNum = int(request.form.get('bedroomNum'))
            if bedroomNum < 0:
                flash("Number of bedrooms cannot be negative.")
                return redirect(request.url)
            bathroomNum = int(request.form.get('bathroomNum'))
            if bathroomNum < 0:
                flash("Number of bathrooms cannot be negative.")
                return redirect(request.url)
            squareFeet = request.form.get('squareFeet')
            if squareFeet <= 0:
                flash("Square feet must be a positive number.")
                return redirect(request.url)
            lotSize = request.form.get('lotSize')
            if lotSize <= 0:
                flash("Lot size must be a positive number.")
                return redirect(request.url)
        except ValueError:
            flash("Please enter valid numeric values for price, bedroom and bathroom counts, square feet, and lot size.")
            return redirect(request.url)
        properties.insert_one({
            'id': new_id,
            'offerType': offerType,
            'price': price,
            'address': address,
            'bedroomNum': bedroomNum,
            'bathroomNum': bathroomNum,
            'squareFeet': squareFeet,
            'lotSize': lotSize
        })
        #get the id of newly inserted record
        #upload file
        if 'file' not in request.files:
            #flash('No file part')
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            #flash('No selected file')
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            basedir = os.path.abspath(os.path.dirname(__file__))
            new_id = str(new_id)
            file_extention = '.'+filename.rsplit('.', 1)[1].lower()
            new_filename = new_id + file_extention
            file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], (new_id+'.jpg')))
            
            return redirect(url_for('home_view.index'))
        return redirect(url_for('home_view.index'))


    return render_template('sell.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS