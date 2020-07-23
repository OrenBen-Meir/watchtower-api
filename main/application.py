from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from main.setup import Config, setup_requests, setup_login_manager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = setup_login_manager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():  # should handle database migrations
        from main.models import database_migrate
        database_migrate()

    # Todo: set up database migration

    setup_requests(app)

    return app
