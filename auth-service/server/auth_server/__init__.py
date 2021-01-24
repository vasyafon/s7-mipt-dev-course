import asyncio
import base64
import os
import connexion
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp_session import get_session, setup
from cryptography import fernet
from cryptography.fernet import Fernet
from gino import GinoEngine, GinoConnection
from gino_aiohttp import Gino

from auth_server.cleanup_ctx import manage_logger, get_public_key
from auth_server.const import Const

# from auth_server.functions.auth_db import create_auth_db

db = Gino(schema=Const.DB_SCHEMA)


async def create_tables(app_):
    await db.gino.create_all()


def main():
    options = {
        "swagger_ui": True
    }

    specification_dir = os.path.join(os.path.dirname(__file__), 'openapi')
    app = connexion.AioHttpApp(__name__,
                               specification_dir=specification_dir,
                               options=options,
                               server_args=dict(middlewares=[
                                   db
                               ]))
    setup(app.app, EncryptedCookieStorage(Fernet.generate_key().decode())
          )

    db.init_app(app.app,
                config=dict(
                    host=Const.DB_HOST,
                    port=Const.DB_PORT,
                    user=Const.DB_USER,
                    password=Const.DB_PASSWORD,
                    database=Const.DB_NAME
                ))

    app.add_api('openapi.yaml',
                arguments={'title': 'DSM Auth server'},
                pythonic_params=True,
                pass_context_arg_name='request')

    app.app.cleanup_ctx.extend([
        get_public_key,
        manage_logger
    ])

    app.app.on_startup.append(create_tables)

    app.run(port=8080)
