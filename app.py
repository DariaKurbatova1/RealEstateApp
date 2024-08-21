import flask
from flask import abort
from property import Property
app = flask.Flask(__name__)

property1 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000)
property2 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000)
property3 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000)

properties = [property1, property2, property3]

@app.route('/')
def index():
    return f'{property1}'

@app.route('/properties/')
def get_properties():
    if not properties or len(properties)==0:
        abort(404)
    listProperties='<ul>'
    for property in properties:
        listProperties += f'<li>{property}</li>'
    listProperties += '</ul>'
    return listProperties

