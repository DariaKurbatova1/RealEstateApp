# import os
# from flask import Flask
# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping( SECRET_KEY='dev',
#     )
#     from .home_view import bp as home_bp
#     app.register_blueprint(home_bp)

import flask
app = flask.Flask(__name__)