from main.errors import ApplicationException

def server_error(**kwargs) -> ApplicationException:
    return ApplicationException(message="internal server error", status_code=500, payload=kwargs)

def not_found(**kwargs) -> ApplicationException:
    return ApplicationException(message="not found", status_code=404, payload=kwargs)

def permission_error(**kwargs) -> ApplicationException:
    return ApplicationException(message="permission denied", status_code=403, payload=kwargs)
    
def bad_request(**kwargs) -> ApplicationException:
    return ApplicationException(message="bad request", status_code=400, payload=kwargs)
