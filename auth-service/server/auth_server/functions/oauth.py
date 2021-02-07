import os
from secrets import token_urlsafe

from aiohttp import web
from aiohttp_session import setup, get_session
from authlib.integrations.base_client.async_app import AsyncRemoteApp
from authlib.integrations.httpx_client import AsyncOAuth2Client

from auth_server.functions.api_error import ApiError
from auth_server.functions.refresh_token import create_tokens_object

auth_base_url = os.getenv('AUTH_BASE_URL', "")


class MyOauth(AsyncOAuth2Client, AsyncRemoteApp):
    def __init__(self, access_token=None, request: web.Request = None):
        # , app = None, fetch_token = None, update_token = None
        scope = 'api email offline_access openid profile'
        redirect_uri = request.scheme + '://' + request.host + str(
            request.app.router['api_auth_v1_authSso_get'].url_for())
        super(MyOauth, self).__init__(
            client_id=os.getenv('CLIENT_ID', ""),
            client_secret=os.getenv('CLIENT_SECRET', ""),
            scope=scope,
            redirect_uri=redirect_uri
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


async def redirect_to_wsso(request: web.Request):
    oauth = MyOauth(request=request)
    login_endpoint = auth_base_url + "/oauth2/authorize"
    session = await get_session(request)
    code_verifier = token_urlsafe(16)
    nonce = token_urlsafe(16)
    session['code_verifier'] = code_verifier
    session['nonce'] = nonce
    uri, state = oauth.create_authorization_url(login_endpoint, code_verifier=code_verifier, nonce=nonce)
    session['state'] = state
    return uri


async def auth_wsso(request: web.Request, state, code):
    session = await get_session(request)
    if ('state' not in session
            or 'code_verifier' not in session
            or 'nonce' not in session
            or session['state'] != state):
        raise ApiError(401, 'Invalid session')
    code_verifier = session['code_verifier']
    nonce = session['nonce']
    oauth = MyOauth(request=request)
    token = await oauth.fetch_token(oauth.access_token_url, grant_type='authorization_code', code=code,
                                    code_verifier=code_verifier)
    result = await oauth.parse_id_token(token, nonce)
    user_id = result['sub']
    tokens = await create_tokens_object(user_id)
    return tokens
