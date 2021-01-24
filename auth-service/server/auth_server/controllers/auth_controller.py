import hashlib
import os
from typing import List, Dict
from aiohttp import web
from aiohttp_session import get_session
from authlib.integrations.httpx_client import AsyncOAuth2Client

from auth_server.functions.access_token import generate_access_token
# from auth_server.models.api_error import ApiError
# from auth_server.models.login_credentials import LoginCredentials

# from auth_server.models.tokens import Tokens
# from auth_server.models.user_info import UserInfo
from auth_server import util, Const
from auth_server.functions.api_error import ApiError
from auth_server.functions.google import GoogleOauth
from auth_server.functions.models import LoginCredentials, TokenResponse, PublicKey, UserInfo
from auth_server.functions.login import login as login_backend


async def get_public_key(request: web.Request, **kwargs) -> web.Response:
    """get public key to decrypt access tokens
    """

    public_key = PublicKey(publicKey=Const.AUTH_PUBLIC_KEY)
    return web.Response(status=200, body=public_key.json(by_alias=True))


async def get_user_info(request: web.Request, token_info: dict, **kwargs) -> web.Response:
    """get user information
    """

    return web.Response(status=200, body=token_info['user_info'].json(by_alias=True))


async def login(request: web.Request, body, **kwargs) -> web.Response:
    """Authenticate on WSSO
    :param body:
    :type body: dict | bytes
    """
    body = LoginCredentials.parse_obj(body)
    result = await login_backend(body)
    return web.Response(status=200, body=result.json(by_alias=True))


# async def login_google(request: web.Request, body) -> web.Response:
#     """Authenticate on Google
#
#
#
#     :param body:
#     :type body: dict | bytes
#
#     """
#     body = LoginCredentials.parse_obj(body)
#     result = await login_backend(body, request=request)
#     return web.Response(status=200, body=result.json(by_alias=True))

async def auth_google(request: web.Request, state=None, code=None, scope=None) -> web.Response:
    """Authenticate on Google
    :param state:
    :type state: str
    :param code:
    :type code: str
    :param scope:
    :type scope: str
    """
    session = await get_session(request)
    if 'state' not in session or session['state'] != state:
        return web.Response(status=401, body='Invalid state')
    oauth = GoogleOauth(request=request)
    result = await oauth.get_token_google(request.url)
    return web.Response(status=200, body=result.json(by_alias=True))


async def open_google_auth(request: web.Request, ) -> web.Response:
    """Redirect to Google Authentication

    """
    oauth = GoogleOauth(request=request)
    google_auth_endpoint = "https://accounts.google.com/o/oauth2/v2/auth"
    uri, state = oauth.create_authorization_url(google_auth_endpoint)
    session = await get_session(request)
    session['state'] = state
    # return web.Response(status=200)

    return web.HTTPFound(uri)


async def refresh(request: web.Request, token_info: dict, **kwargs) -> web.Response:
    """generate access token from refresh token
    """
    if 'user_info' in token_info:
        user_info: UserInfo = token_info['user_info']
        user_id = user_info.user_id
    elif 'sub_coro' in token_info:
        user_id = await token_info['sub_coro']
        if user_id is None:
            raise ApiError(401, 'Unauthorized')
        token_info['sub'] = user_id
    else:
        raise ApiError(400, 'auth key error')
    access_token, exp = await generate_access_token(user_id)
    result = TokenResponse(token=access_token, expiresAt=exp)
    return web.Response(status=200, body=result.json(by_alias=True))
