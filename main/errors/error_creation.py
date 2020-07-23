from main.errors import ApplicationException


def server_error(reasons: list = None, **kwargs) -> ApplicationException:
    return ApplicationException(message="internal server error", status_code=500, reasons=reasons, payload=kwargs)


def not_found(reasons: list = None, **kwargs) -> ApplicationException:
    return ApplicationException(message="not found", status_code=404, reasons=reasons, payload=kwargs)


def permission_error(reasons: list = None, **kwargs) -> ApplicationException:
    return ApplicationException(message="permission denied", status_code=403, reasons=reasons, payload=kwargs)


def authorization_error(reasons: list = None, **kwargs) -> ApplicationException:
    return ApplicationException(message="unauthorized", status_code=401, reasons=reasons, payload=kwargs)


def bad_request(reasons: list = None, **kwargs) -> ApplicationException:
    return ApplicationException(message="bad request", status_code=400, reasons=reasons, payload=kwargs)
