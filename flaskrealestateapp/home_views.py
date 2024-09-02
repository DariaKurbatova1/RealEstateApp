from flask import (Blueprint, render_template)
# from . import app
from flaskrealestateapp.property import Property
from flask import Flask

bp = Blueprint('home_view', __name__, url_prefix='/')
@bp.route("/")
def index():
    property1 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000)
    property2 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000)
    property3 = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000)

    properties = [property1, property2, property3]
    return render_template('index.html', properties=properties)
