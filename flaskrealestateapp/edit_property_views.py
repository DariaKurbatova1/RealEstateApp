from flask import (Blueprint, render_template, request, redirect, url_for, flash)
# from . import app
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

bp = Blueprint('edit_property', __name__, url_prefix='/edit_property/')

@bp.route("/<int:property_id>", methods=['GET', 'POST'])
def edit_property(property_id):
    #select the edited document
    property = properties.find_one({'id':property_id})
    
    if request.method == 'POST':
        #get form value and insert new record
        try:
            price = int(request.form.get('price'))
            if price <= 0:
                flash("Price must be a positive number.", "error")
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
        #delete the old version of the property
        query = {"address": property['address']}
        properties.delete_one(query)
        
        #insert new version of the property
        properties.insert_one({
            'id': property_id,
            'offerType': property['offerType'],
            'price': price,
            'address': property['address'],
            'bedroomNum': bedroomNum,
            'bathroomNum': bathroomNum,
            'squareFeet': squareFeet,
            'lotSize': lotSize
        })
        #upload new picture
        if 'file' not in request.files:
            #flash('No file part')
            flash("File upload is required.", "error")
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            basedir = os.path.abspath(os.path.dirname(__file__))
            file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], (str(property_id)+'.jpg')))
            
        flash("Property edited successfully!", "success")
        return redirect(url_for('home_view.index'))
        #delete the old instance of the record
    
    
    
    

    return render_template('edit-property.html', property=property)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS