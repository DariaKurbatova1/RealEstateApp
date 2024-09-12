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

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

bp = Blueprint('edit_property', __name__, url_prefix='/edit_property/')

@bp.route("/<int:property_id>", methods=['GET', 'POST'])
def edit_property(property_id):
    #select the edited document
    property = properties.find_one({'id':1})
    
    if request.method == 'POST':
        #validation
        ###
        #get form value and insert new record
        price = request.form['price']
        bedroomNum = request.form['bedroomNum']
        bathroomNum = request.form['bathroomNum']
        squareFeet = request.form['squareFeet']
        lotSize = request.form['lotSize']
        
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
            file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], (property_id+'.jpg')))
        
        #delete the old instance of the record
    
    
    
    

    return render_template('edit-property.html', property=property)
