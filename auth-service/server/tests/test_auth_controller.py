# coding: utf-8

import pytest
import json
from aiohttp import web

from dsm_auth_server.functions.access_token import generate_access_token
from dsm_auth_server.models.access_token import AccessToken
from dsm_auth_server.models.api_error import ApiError
from dsm_auth_server.models.login_credentials import LoginCredentials
from dsm_auth_server.models.public_key import PublicKey
from dsm_auth_server.models.tokens import Tokens
from dsm_auth_server.models.user_info import UserInfo


async def test_get_public_key(client):
    """Test case for get_public_key

    get public key to decrypt access tokens
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/auth/v2/publicKey',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_user_info(client):
    """Test case for get_user_info

    get user information
    """
    access_token = await generate_access_token('v.baydin')
    headers = { 
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token[0]}',
        'CookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/auth/v2/userInfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')



# async def test_login(client):
#     """Test case for login
#
#     Authenticate on WSSO
#     """
#     body = {
#   "redirectUri" : "redirectUri",
#   "code" : "code",
#   "codeVerifier" : "codeVerifier",
#   "nonce" : "nonce"
# }
#     headers = {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#     }
#     response = await client.request(
#         method='POST',
#         path='/api/auth/v2/login',
#         headers=headers,
#         json=body,
#         )
#     assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_refresh(client):
    """Test case for refresh

    generate access token from refresh token
    """
    refresh_token = '74273bd6-ff19-4e09-ab92-158494e044e1'

    headers = { 
        'Accept': 'application/json',
        'Authorization': f'Bearer {refresh_token}'
    }
    response = await client.request(
        method='POST',
        path='/api/auth/v2/refresh',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

