from flask import (Blueprint, render_template)
from . import app
from . property import Property
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos

#bp = Blueprint('home_view', __name__, url_prefix='/')

property1 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000)
property2 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000)
property3 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000)

properties = [property1, property2, property3]

@app.route("/")
def index():
  return render_template('index.html', properties=properties)

# @app.route("/db/")
# def db():
#   return render_template('db.html')