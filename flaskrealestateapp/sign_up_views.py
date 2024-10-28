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

bp = Blueprint('sign_up_view', __name__, url_prefix='/signup/')

@bp.route("/", methods=['GET', 'POST'])
def sign_up():
    return render_template('signup.html')