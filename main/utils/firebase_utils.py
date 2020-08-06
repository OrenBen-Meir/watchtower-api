import os
import requests
from pyrebase.pyrebase import raise_detailed_error
import json

"""
Custom firebase utilities for functions not available in pyrebase
"""


def firebase_config():
    return {
        "apiKey": os.environ.get("FIREBASE_API_KEY"),
        "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN"),
        "databaseURL": os.environ.get("FIREBASE_DATABASE_URL"),
        "projectId": os.environ.get("FIREBASE_PROJECT_ID"),
        "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET"),
        "messagingSenderId": os.environ.get("FIREBASE_MESSAGING_SENDER_ID"),
        "appId": os.environ.get("FIREBASE_APP_ID"),
        "measurementId": os.environ.get("FIREBASE_MEASUREMENT_ID")
    }


def delete_user_account(id_token):
    """
    Takes in a user idToken and deletes an account associated with it in firebase.
    Function is a tweak of the following commit to the github repository of pyrebase:
    https://github.com/thisbejim/Pyrebase/pull/203/commits/ea3810eb76105634a05afdc0c4e419f185ca867d
    """
    api_key = firebase_config()["apiKey"]
    request_ref = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/deleteAccount?key={api_key}"
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"idToken": id_token})
    request_object = requests.post(request_ref, headers=headers, data=data)
    raise_detailed_error(request_object)
    return request_object.json()
