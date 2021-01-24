import os

from aiohttp import web
from aiohttp_session import setup, get_session
from authlib.integrations.httpx_client import AsyncOAuth2Client

from auth_server.functions.access_token import generate_access_token
from auth_server.functions.api_error import ApiError
from auth_server.functions.google import GoogleOauth
from auth_server.functions.models import Tokens, TokenResponse, LoginCredentials
from auth_server.functions.oauth import MyOauth
from auth_server.functions.refresh_token import generate_refresh_token_by_user


async def login(cred: LoginCredentials, request=None) -> Tokens:
    client = GoogleOauth(request)
    try:
        token = await client.fetch_token(client.access_token_url, grant_type='authorization_code', code=cred.code,
                                         code_verifier=cred.code_verifier, redirect_uri=cred.redirect_uri)
        user_info = await client.parse_id_token(token, cred.nonce)
    finally:
        await client.aclose()

    user_id = user_info['email']

    refresh_token = await generate_refresh_token_by_user(user_id)
    access_token, access_token_exp = await generate_access_token(user_id)
    if access_token is None:
        print(f"User {user_id} is not registered in the service")
        raise ApiError

    # if request is not None:
    #     session = await get_session(request)
    #     session['access_token'] = access_token
    #     session['refresh_token'] = str(refresh_token.token_id)

    return Tokens(
        refreshToken=TokenResponse(
            token=str(refresh_token.token_id),
            expiresAt=refresh_token.expiration_date),
        accessToken=TokenResponse(
            token=access_token,
            expiresAt=access_token_exp)
    )
