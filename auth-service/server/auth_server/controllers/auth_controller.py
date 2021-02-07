from aiohttp import web
from auth_server import util, Const
from auth_server.functions.models import PublicKey
from auth_server.functions.oauth import redirect_to_wsso, auth_wsso
from auth_server.functions.refresh import refresh as refresh_backend


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
    return result


async def login(request: web.Request, redirection=None) -> web.Response:
    """Redirect to Google Authentication

    """

    # uri = await redirect_to_google(request)
    login_url = await redirect_to_wsso(request, redirection)
    return web.Response(status=200, body=login_url.json(by_alias=True))
    # web.HTTPFound(uri)


async def refresh(request: web.Request, token_info: dict, **kwargs) -> web.Response:
    """generate access token from refresh token
    """
    result = await refresh_backend(request, token_info)
    return web.Response(status=200, body=result.json(by_alias=True))
