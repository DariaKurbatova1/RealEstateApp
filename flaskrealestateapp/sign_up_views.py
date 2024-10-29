from flask import (Blueprint, render_template, request, redirect, url_for)
from flaskrealestateapp.property import Property
from flask import Flask
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash

#create db client
client = MongoClient('localhost', 27017)
#create mongodb database
db = client.flask_properties
#create collection
users = db.users

bp = Blueprint('sign_up_view', __name__, url_prefix='/signup/')

@bp.route("/", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation checks
        try:
            if not email or '@' not in email:
                flash("Invalid email. Please provide a valid email.")
                return render_template('signup.html')
            
            if len(password) < 6:
                flash("Password should be at least 6 characters long.")
                return render_template('signup.html')
            
            if password != confirm_password:
                flash("Passwords must match.")
                return render_template('signup.html')
            
            #check if user already exists
            if users.find_one({'email': email}):
                flash("User with this email already exists")
                return redirect(url_for('login_view.login'))
            
            #create user
            hashed_password = generate_password_hash(password)
            user = {
                'email': email,
                'password': hashed_password,
                'name': name
            }
            try:
                users.insert_one(user)
                flash("User created successfully. Please log in.")
                return redirect(url_for('login_view.login'))
            except Exception as e:
                    print(f"Error inserting user: {e}")
                    flash("An error occurred while creating your account. Please try again.")
                    return render_template('signup.html')
        except Exception as e:
            print(f"General error: {e}")
            flash("An error occurred. Please try again.")
            return render_template('signup.html')
    
    return render_template('signup.html')