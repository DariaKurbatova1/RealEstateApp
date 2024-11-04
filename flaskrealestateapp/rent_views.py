from flask import (Blueprint, render_template)
from pymongo import MongoClient
import os
import gridfs
import base64

client = MongoClient(os.environ.get("MONGO_URI"))
db = client.flask_properties
properties = db.properties
fs = gridfs.GridFS(db)

bp = Blueprint('rent_view', __name__, url_prefix='/rent/')

@bp.route("/", methods=['GET', 'POST'])
def rent_property():
    query = {'offerType': 'rent'}
    all_properties = list(db.properties.find(query))
    for property in all_properties:
        image_file = fs.find_one({"property_id": property['id']})
        if image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
            property['image'] = image_data
    return render_template('rent.html', properties=all_properties)