import os
import connexion
from mipt_auth_wrapper import get_auth_public_key

from airport_load_server.functions.const import Const


async def set_auth_public_key(app):
    Const.AUTH_PUBLIC_KEY = await get_auth_public_key()
    yield


SERVER_PORT = int(os.getenv('SERVER_PORT', '8080'))


def main():
    options = {
        "swagger_ui": True
    }
    specification_dir = os.path.join(os.path.dirname(__file__), 'openapi')
    app = connexion.AioHttpApp(__name__, specification_dir=specification_dir, options=options)
    app.app.cleanup_ctx.extend([
        set_auth_public_key
    ])
    app.add_api('openapi.yaml',
                arguments={'title': 'API to show passenger load in airports'},
                pythonic_params=True,
                pass_context_arg_name='request')
    app.run(port=SERVER_PORT)
