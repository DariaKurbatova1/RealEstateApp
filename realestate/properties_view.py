from flask import (render_template)
from . import app
from property import Property

@app.route("/properties/")
def get_properties():
    #will add get/post handling later
    properties = [Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000), \
        Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000), \
        Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000)]
    return render_template('properties.html', properties=properties)