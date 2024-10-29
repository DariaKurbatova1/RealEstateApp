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

bp = Blueprint('buy_view', __name__, url_prefix='/buy/')

@bp.route("/", methods=['GET', 'POST'])
def buy_property():
    query = {'offerType': 'sale'}
    all_properties = properties.find(query)
    return render_template('buy.html', properties=all_properties)