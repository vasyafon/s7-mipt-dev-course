from aiohttp import web
from auth_server.functions.access_token import generate_access_token
from auth_server import util, Const
from auth_server.functions.api_error import ApiError
from auth_server.functions.google import GoogleOauth, redirect_to_google, auth_google
from auth_server.functions.models import  TokenResponse, PublicKey, UserInfo
from auth_server.functions.oauth import redirect_to_wsso, auth_wsso


async def get_public_key(request: web.Request, **kwargs) -> web.Response:
    """get public key to decrypt access tokens
    """

    public_key = PublicKey(publicKey=Const.AUTH_PUBLIC_KEY)
    return web.Response(status=200, body=public_key.json(by_alias=True))


async def get_user_info(request: web.Request, token_info: dict, **kwargs) -> web.Response:
    """get user information
    """

    return web.Response(status=200, body=token_info['user_info'].json(by_alias=True))


async def auth(request: web.Request, state=None, code=None, scope=None) -> web.Response:
    """Authenticate on Google
    :param state:
    :type state: str
    :param code:
    :type code: str
    :param scope:
    :type scope: str
    """
    # result = await auth_google(request, state)
    result = await auth_wsso(request, state, code)
    return web.Response(status=200, body=result.json(by_alias=True))


async def login(request: web.Request, ) -> web.Response:
    """Redirect to Google Authentication

    """

    # uri = await redirect_to_google(request)
    uri = await redirect_to_wsso(request)
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
