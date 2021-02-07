import os

from aiohttp import web
from aiohttp_session import get_session
from authlib.integrations.base_client.async_app import AsyncRemoteApp
from authlib.integrations.httpx_client import AsyncOAuth2Client

from auth_server.functions.api_error import ApiError
from auth_server.functions.refresh_token import create_tokens_object


class GoogleOauth(AsyncOAuth2Client, AsyncRemoteApp):
    def __init__(self, request: web.Request = None):
        scope = 'email openid profile'
        redirect_uri = request.scheme + '://' + request.host + str(
            request.app.router['api_auth_v1_authSso_get'].url_for())
        super(GoogleOauth, self).__init__(
            client_id=os.getenv('GOOGLE_CLIENT_ID', ""),
            client_secret=os.getenv('GOOGLE_CLIENT_SECRET', ""),
            scope=scope,
            redirect_uri=redirect_uri
        )
        self._server_metadata_url = None
        self.server_metadata = {
            'jwks_uri': "https://www.googleapis.com/oauth2/v3/certs"
        }
        self.client_kwargs = {}
        self.request_token_url = f'https://oauth2.googleapis.com/token'
        self.access_token_url = self.request_token_url

    async def get_session(self, request: web.Request):
        self.session = await get_session(request)

    async def fetch_jwk_set(self, loop=None):
        jwks = await self.request('GET', self.server_metadata['jwks_uri'], withhold_token=True)
        self.server_metadata['jwks'] = jwks.json()

    async def parse_id_token(self, token, nonce, claims_options=None):
        await self.fetch_jwk_set()
        user_info = await self._parse_id_token(token, nonce, claims_options=claims_options)
        return user_info

    async def get_token_google(self, authorization_response):
        token = await self.fetch_token(self.request_token_url, authorization_response=str(authorization_response))
        user_info = await self.parse_id_token(token, None)
        user_id = user_info['sub']
        tokens = await create_tokens_object(user_id)
        return tokens


async def redirect_to_google(request: web.Request):
    oauth = GoogleOauth(request=request)
    google_auth_endpoint = "https://accounts.google.com/o/oauth2/v2/auth"
    uri, state = oauth.create_authorization_url(google_auth_endpoint)
    session = await get_session(request)
    session['state'] = state
    # return web.Response(status=200)
    return uri


async def auth_google(request: web.Request, state):
    session = await get_session(request)
    if 'state' not in session or session['state'] != state:
        raise ApiError(401, 'Invalid state')
    oauth = GoogleOauth(request=request)
    result = await oauth.get_token_google(request.url)
    return result
