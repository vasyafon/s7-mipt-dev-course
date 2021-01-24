import logging
import pytest
import os
import pretty_errors
import connexion
from urllib3 import PoolManager

from airport_load_server import set_auth_public_key


@pytest.fixture
def get_access_token():
    refresh_token = os.getenv('REFRESH_TOKEN', '74273bd6-ff19-4e09-ab92-158494e044e1')
    import urllib3
    import json
    auth_url = os.getenv('AUTH_URL', 'http://localhost:8080/api/auth/v1')
    http = PoolManager(retries=3)
    response = http.request('POST', f'{auth_url}/refresh', headers={'Authorization': f'Bearer {refresh_token}'})
    pk = json.loads(response.data.decode('utf-8'))
    return pk['token']


@pytest.fixture
def client(loop, aiohttp_client, get_access_token):
    logging.getLogger('connexion.operation').setLevel('ERROR')
    options = {
        "swagger_ui": True
    }
    specification_dir = os.path.join(os.path.dirname(__file__), '..',
                                     'airport_load_server',
                                     'openapi')
    app = connexion.AioHttpApp(__name__, specification_dir=specification_dir,
                               options=options)
    app.app.cleanup_ctx.extend([
        set_auth_public_key
    ])
    app.add_api('openapi.yaml', pythonic_params=True,
                pass_context_arg_name='request')
    return loop.run_until_complete(aiohttp_client(app.app))
