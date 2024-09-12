import os
from flask import Flask, flash, render_template, current_app



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    #home page
    from .home_views import bp as home_bp
    app.register_blueprint(home_bp)
    
    #sell page
    from .sell_views import bp as sell_bp
    app.register_blueprint(sell_bp)
    
    #upload image page
    from .upload_img_views import bp as upload_bp
    app.register_blueprint(upload_bp)
    
    from .edit_property_views import bp as edit_property_bp
    app.register_blueprint(edit_property_bp)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app