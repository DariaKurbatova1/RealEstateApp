from flask import (Blueprint, render_template, request, redirect, url_for, flash)
from flaskrealestateapp.property import Property
from flask import Flask
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
from werkzeug.security import check_password_hash


#create db client
client = MongoClient('localhost', 27017)
#create mongodb database
db = client.flask_properties
#create collection
users = db.users

bp = Blueprint('login_view', __name__, url_prefix='/login/')

@bp.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email or '@' not in email:
            flash("Invalid email. Please provide a valid email.")
            return render_template('login.html')

        if not password:
            flash("Password is required.")
            return render_template('login.html')
        
        #check if user exists
        user = users.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            flash("Login successful!", "success")
            return redirect(url_for('home_view.index'))  
        else:
            flash("Invalid email or password.")
    
    return render_template('login.html')