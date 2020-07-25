from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from main.setup import Config, setup_requests, initialize_firebase

db = SQLAlchemy()
firebase = initialize_firebase()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():  # should handle database migrations
        from main.models import database_migrate
        database_migrate()

    setup_requests(app)

    return app
