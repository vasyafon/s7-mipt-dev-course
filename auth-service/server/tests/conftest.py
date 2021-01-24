import base64
import logging
import pytest
import os

import connexion
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet
from gino_aiohttp import Gino

from dsm_auth_server import get_public_key, manage_logger, Const
from dsm_auth_server import db



@pytest.fixture
def client(loop, aiohttp_client):
    logging.getLogger('connexion.operation').setLevel('ERROR')
    options = {
        "swagger_ui": True
        }
    specification_dir = os.path.join(os.path.dirname(__file__), '..',
                                     'auth_server',
                                     'openapi')
    app = connexion.AioHttpApp(__name__, specification_dir=specification_dir,
                               options=options)
    app.app.cleanup_ctx.extend([
        get_public_key,
        manage_logger
    ])
    db.init_app(app.app,
                config=dict(
                    host=Const.DB_HOST,
                    port=Const.DB_PORT,
                    user=Const.DB_USER,
                    password=Const.DB_PASSWORD,
                    database=Const.DB_NAME
                ))


    app.add_api('openapi.yaml', pythonic_params=True,
                pass_context_arg_name='request')

    fernet_key = fernet.Fernet.generate_key()
    Const.SESSION_KEY = fernet_key
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app.app, EncryptedCookieStorage(secret_key, cookie_name='auth_session'))

    return loop.run_until_complete(aiohttp_client(app.app))
