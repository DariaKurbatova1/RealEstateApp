from flask import (Blueprint, render_template, request, redirect, url_for)
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
        #get the id of newly inserted record
        new_id = (db.properties.count_documents({}))+1
        #get form value and insert new record
        offerType = request.form['offerType']
        price = request.form['price']
        address = request.form['address']
        bedroomNum = request.form['bedroomNum']
        bathroomNum = request.form['bathroomNum']
        squareFeet = request.form['squareFeet']
        lotSize = request.form['lotSize']
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