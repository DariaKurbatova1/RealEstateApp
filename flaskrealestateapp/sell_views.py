from flask import (Blueprint, render_template, request, redirect, url_for, flash)
from flask import Flask
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import gridfs
import os

client = MongoClient(os.environ.get("MONGO_URI"))
db = client.flask_properties
properties = db.properties
fs = gridfs.GridFS(db)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

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
                flash("Offer type is required.", "error")
            type = request.form.get('type')
            if not type:
                flash("Type is required.", "error")
            price = int(request.form.get('price'))
            if price <= 0:
                flash("Price must be a positive number.", "error")
                return redirect(request.url)
            address = request.form.get('address')
            if not address:
                flash("Address is required.", "error")
                return redirect(request.url)
            bedroomNum = int(request.form.get('bedroomNum'))
            if bedroomNum < 0:
                flash("Number of bedrooms cannot be negative.", "error")
                return redirect(request.url)
            bathroomNum = int(request.form.get('bathroomNum'))
            if bathroomNum < 0:
                flash("Number of bathrooms cannot be negative.", "error")
                return redirect(request.url)
            squareFeet = request.form.get('squareFeet')
            squareFeet = int(squareFeet)
            if squareFeet < 0:
                flash("Square feet must be a positive number.", "error")
                return redirect(request.url)
            lotSize = request.form.get('lotSize')
            lotSize = int(lotSize)
            if lotSize < 0:
                flash("Lot size must be a positive number.", "error")
                return redirect(request.url)
        except ValueError:
            flash("Please enter valid numeric values for price, bedroom and bathroom counts, square feet, and lot size.", "error")
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
            flash("File upload is required.", "error")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', "error")
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fs.put(file, filename=filename, property_id=new_id)
            
            flash("Property added successfully!", "success")
            
            return redirect(url_for('home_view.index'))
        return redirect(url_for('home_view.index'))


    return render_template('sell.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS