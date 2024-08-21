from flask import (Blueprint, render_template)
from . import app

#bp = Blueprint('home_view', __name__, url_prefix='/')

@app.route("/")
def index():
  return render_template('index.html')