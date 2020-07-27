from pyrebase import pyrebase

from main.utils.firebase_utils import firebase_config


def initialize_firebase():
    config = firebase_config()
    return pyrebase.initialize_app(config)
