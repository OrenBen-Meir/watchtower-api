from pyrebase import pyrebase
import os


def initialize_firebase():
    config = {
        "apiKey": os.environ.get("FIREBASE_API_KEY"),
        "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN"),
        "databaseURL": os.environ.get("FIREBASE_DATABASE_URL"),
        "projectId": os.environ.get("FIREBASE_PROJECT_ID"),
        "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET"),
        "messagingSenderId": os.environ.get("FIREBASE_MESSAGING_SENDER_ID"),
        "appId": os.environ.get("FIREBASE_APP_ID"),
        "measurementId": os.environ.get("FIREBASE_MEASUREMENT_ID")
    }

    return pyrebase.initialize_app(config)
