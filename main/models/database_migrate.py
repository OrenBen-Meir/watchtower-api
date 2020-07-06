from flask import current_app
from flask_migrate import Migrate
from main.application import db
from .user_model import User

def database_migrate():                                                             # This is to migrate changes in our models to our database
    migrate = Migrate(current_app, db, compare_type=True)