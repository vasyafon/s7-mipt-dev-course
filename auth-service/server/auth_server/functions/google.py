import os

from aiohttp import web
from aiohttp_session import get_session
from authlib.integrations.base_client.async_app import AsyncRemoteApp
from authlib.integrations.httpx_client import AsyncOAuth2Client

from auth_server.functions.access_token import generate_access_token
from auth_server.functions.models import ApiError, Tokens, TokenResponse
from auth_server.functions.refresh_token import generate_refresh_token_by_user


class GoogleOauth(AsyncOAuth2Client, AsyncRemoteApp):
    def __init__(self, request: web.Request = None):
        scope = 'email openid profile'
        redirect_uri = request.scheme + '://' + request.host + str(
            request.app.router['api_auth_v1_authGoogle_get'].url_for())
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

        refresh_token = await generate_refresh_token_by_user(user_id)
        access_token, access_token_exp = await generate_access_token(user_id)
        if access_token is None:
            print(f"User {user_id} is not registered in the service")
            raise ApiError

        return Tokens(
            refreshToken=TokenResponse(
                token=str(refresh_token.token_id),
                expiresAt=refresh_token.expiration_date),
            accessToken=TokenResponse(
                token=access_token,
                expiresAt=access_token_exp)
        )
