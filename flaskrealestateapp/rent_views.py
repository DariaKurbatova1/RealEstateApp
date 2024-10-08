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

bp = Blueprint('rent_view', __name__, url_prefix='/rent/')

@bp.route("/", methods=['GET', 'POST'])
def rent_property():
    return render_template('rent.html')