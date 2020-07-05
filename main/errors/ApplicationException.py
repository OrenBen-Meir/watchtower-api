from flask import jsonify

class ApplicationException(Exception):

    def __init__(self, message : str = "", status_code : int = 400, payload : dict = None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self) -> dict:
        rv = dict(self.payload or ())
        rv["status_code"] = self.status_code
        rv['message'] = self.message
        return rv