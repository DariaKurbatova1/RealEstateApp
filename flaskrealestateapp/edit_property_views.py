from flask import (Blueprint, render_template, request, redirect, url_for, flash)
from flask import Flask
from pymongo import MongoClient
import os
import gridfs
from PIL import Image
import io
import base64

client = MongoClient(os.environ.get("MONGO_URI"))
db = client.flask_properties
properties = db.properties

fs = gridfs.GridFS(db)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

bp = Blueprint('edit_property', __name__, url_prefix='/edit_property/')

@bp.route("/<int:property_id>", methods=['GET', 'POST'])
def edit_property(property_id):
    #select the edited document
    property = properties.find_one({'id':property_id})
    print(property)
    existing_image = None
    if 'image_id' in property:
        image_file = fs.find_one({"_id": property['image_id']})
        if image_file:
            print('image found')
            existing_image = base64.b64encode(image_file.read()).decode('utf-8')
        else:
            print('image not found')
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
        
        #insert new version of the property
        properties.update_one(
            {'id': property_id},
            {'$set': {
                'price': price,
                'bedroomNum': bedroomNum,
                'bathroomNum': bathroomNum,
                'squareFeet': squareFeet,
                'lotSize': lotSize
            }}
        )
        #upload new picture
        if 'file' not in request.files:
            #flash('No file part')
            flash("File upload is required.", "error")
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file and allowed_file(file.filename):
            #delete old pic
            if 'image_id' in property:
                fs.delete(property['image_id'])
            #convert pic
            img = Image.open(file)
            img = img.convert("RGB")
            buffer = io.BytesIO()
            img.save(buffer, format="JPEG")
            buffer.seek(0)
            #add pic to db
            gridfs_id = fs.put(buffer, filename=f"{property_id}.jpg", property_id=property_id)
            properties.update_one(
                {'id': property_id},
                {'$set': {'image_id': gridfs_id}}
            )
            
        flash("Property edited successfully!", "success")
        return redirect(url_for('home_view.index'))

    return render_template('edit-property.html', property=property, existing_image=existing_image)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS