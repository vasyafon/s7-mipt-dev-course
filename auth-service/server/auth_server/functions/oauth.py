# from authlib.integrations.flask_client import OAuth
import os

from aiohttp import web
from aiohttp_session import setup, get_session
from authlib.integrations.base_client.async_app import AsyncRemoteApp
from authlib.integrations.httpx_client import AsyncOAuth2Client

auth_base_url = os.getenv('AUTH_BASE_URL', "")


class MyOauth(AsyncOAuth2Client, AsyncRemoteApp):
    def __init__(self, access_token=None, request: web.Request = None):
        # , app = None, fetch_token = None, update_token = None
        scope = 'api email offline_access openid profile'

        super(MyOauth, self).__init__(
            client_id=os.getenv('CLIENT_ID', ""),
            client_secret=os.getenv('CLIENT_SECRET', ""),
            scope=scope
        )
        self._server_metadata_url = None
        self.server_metadata = {}
        self.base_url = auth_base_url
        self.access_token_url = f'{auth_base_url}/oauth2/token'
        self.authorize_url = f'{auth_base_url}/oauth2/authorize'
        self.server_metadata['jwks_uri'] = f'{auth_base_url}/oauth2/jwks'
        self.client_kwargs = {}
        self.request_token_url = f'{auth_base_url}/oauth2/token'

    async def get_session(self, request: web.Request):
        self.session = await get_session(request)

    async def fetch_jwk_set(self, loop=None):
        jwks = await self.request('GET', self.server_metadata['jwks_uri'], withhold_token=True)
        self.server_metadata['jwks'] = jwks.json()

    async def parse_id_token(self, token, nonce, claims_options=None):
        await self.fetch_jwk_set()
        user_info = await self._parse_id_token(token, nonce, claims_options=claims_options)
        return user_info
