class ApplicationException(Exception):

    def __init__(self, message: str = "", status_code: int = 400, reasons: list = None, payload: dict = None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload
        self.reasons = reasons

    def to_dict(self) -> dict:
        rv = dict(self.payload or ())
        rv["status_code"] = self.status_code
        rv['message'] = self.message
        rv["reasons"] = self.reasons
        return rv
