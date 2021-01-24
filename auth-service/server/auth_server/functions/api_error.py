class ApiError(BaseException):
    code = 400
    message = 'Error'

    def __init__(self, code=400, message='Error'):
        self.code = code
        self.message = message
