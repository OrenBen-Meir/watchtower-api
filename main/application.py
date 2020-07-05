from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager 
from flask_mail import Mail

from main.setup import Config, setup_requests

db = SQLAlchemy()                                   # This initilizes SQLAlchemy!
bcrypt = Bcrypt()                                   # This initializes bcrypt!

def create_app(config_class=Config):
    app = Flask(__name__)                             # __name__ is referencing the name of this file
    app.config.from_object(Config)                 # We're passing in the Config class we imported, into the app config. 
    
    db.init_app(app)
    bcrypt.init_app(app)

    #Todo: set up database migration

    setup_requests(app)

    return app