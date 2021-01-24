class DsmApiError(Exception):
    code: int = 400
    message: str = 'API exception'

    def __init__(self, code=None, message=None):
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message


class DsmNotAuthorizedApiError(DsmApiError):
    code: int = 401
    message: str = 'Not Authorized'


class DsmForbiddenApiError(DsmApiError):
    code: int = 403
    message: str = 'Forbidden'


class DsmNotFoundApiError(DsmApiError):
    code: int = 404
    message: str = 'Not Found'


class DsmMethodNotAllowedApiError(DsmApiError):
    code: int = 405
    message: str = 'Method Not allowed'


class DsmInternalServerError(DsmApiError):
    code: int = 500
    message: str = 'Internal Server Error'
