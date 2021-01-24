import base64


from auth_server.const import Const
import os


async def get_public_key(app):
    public_key_b64 = os.environ.get('AUTH_PUBLIC_KEY', None)
    Const.AUTH_PUBLIC_KEY = base64.b64decode(public_key_b64)
    yield


