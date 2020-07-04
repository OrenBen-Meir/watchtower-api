from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager 
from flask_mail import Mail
from main.config import Config                       # This is the same as before but we migrated all the app.config calls into the config file.

db = SQLAlchemy()                                   # This initilizes SQLAlchemy!
bcrypt = Bcrypt()                                   # This initializes bcrypt!

def create_app(config_class=Config):
    app = Flask(__name__)                               # __name__ is referencing the name of this file
    app.config.from_object(Config)                      # We're passing in the Config class we imported, into the app config. 
    
    db.init_app(app)
    bcrypt.init_app(app)

    #Todo: set up database migration

    # import and register bluprints
    from main.controllers.test import testBlueprint
    from main.controllers.rootUrls import root

    app.register_blueprint(testBlueprint)
    app.register_blueprint(root)

    @app.after_request
    def add_header(r):
        """
        Add headers to both force latest IE rendering engine or Chrome Frame,
        and also to cache the rendered page for 10 minutes.
        """
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
        return r

    return app