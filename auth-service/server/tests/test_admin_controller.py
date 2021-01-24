# coding: utf-8

import pytest
import json
from aiohttp import web

from dsm_auth_server.functions.access_token import generate_access_token
from dsm_auth_server.models.admin_refresh_token_info import AdminRefreshTokenInfo
from dsm_auth_server.models.admin_refresh_token_info_post import AdminRefreshTokenInfoPost
from dsm_auth_server.models.admin_refresh_token_list import AdminRefreshTokenList
from dsm_auth_server.models.api_error import ApiError
from dsm_auth_server.models.group_full import GroupFull
from dsm_auth_server.models.group_list import GroupList
from dsm_auth_server.models.group_post import GroupPost
from dsm_auth_server.models.tokens import Tokens
from dsm_auth_server.models.user_info import UserInfo
from dsm_auth_server.models.user_info_list import UserInfoList


async def test_admin_add_group(client):
    """Test case for admin_add_group

    add new group
    """

    access_token = await generate_access_token('v.baydin')

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token[0]}'
    }

    body = {
        "groupId": "test1",
        "description": "description1"
    }

    response = await client.request(
        method='POST',
        path='/api/auth/v2/admin/groups',
        headers=headers,
        json=body,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_admin_add_user(client):
    """Test case for admin_add_user

    add new user
    """

    access_token = await generate_access_token('v.baydin')

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token[0]}'
    }

    body = {
        "globalRole": "USER",
        "groups": [ {
            "mode": "READ",
            "groupId": "unittest"
        }],
        "userId": "test"
    }

    response = await client.request(
        method='POST',
        path='/api/auth/v2/admin/users',
        headers=headers,
        json=body,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_admin_get_group(client):
    """Test case for admin_get_group

    Get group
    """
    access_token = await generate_access_token('v.baydin')

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token[0]}'
    }
    response = await client.request(
        method='GET',
        path='/api/auth/v2/admin/groups/{group_id}'.format(group_id='unittest'),
        headers=headers,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_admin_get_user_info(client):
    """Test case for admin_get_user_info

    Get user info
    """
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'CookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/auth/v2/admin/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_admin_group_put(client):
    """Test case for admin_group_put

    Edit group
    """
    access_token = await generate_access_token('v.baydin')

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token[0]}'
    }

    body = {
        "groupId": "test1",
        "description": "description",
        "users": [{
            "mode": "READ",
            "userId": "test"
        }, {
            "mode": "READ",
            "userId": "unittest"
        }]
    }

    response = await client.request(
        method='PUT',
        path='/api/auth/v2/admin/groups/{group_id}'.format(group_id='test1'),
        headers=headers,
        json=body,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_admin_list_groups(client):
    """Test case for admin_list_groups

    list all groups
    """
    access_token = await generate_access_token('v.baydin')

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token[0]}'
    }
    response = await client.request(
        method='GET',
        path='/api/auth/v2/admin/groups',
        headers=headers,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_admin_list_users(client):
    """Test case for admin_list_users

    list all users
    """
    access_token = await generate_access_token('v.baydin')

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token[0]}'
    }
    response = await client.request(
        method='GET',
        path='/api/auth/v2/admin/users',
        headers=headers,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_admin_remove_group(client):
    """Test case for admin_remove_group

    Remove group from the system
    """
    access_token = await generate_access_token('v.baydin')

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token[0]}'
    }
    response = await client.request(
        method='DELETE',
        path='/api/auth/v2/admin/groups/{group_id}'.format(group_id='test1'),
        headers=headers,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_admin_remove_user(client):
    """Test case for admin_remove_user

    Remove user from the system
    """
    access_token = await generate_access_token('v.baydin')

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token[0]}'
    }
    response = await client.request(
        method='DELETE',
        path='/api/auth/v2/admin/users/{user_id}'.format(user_id='test'),
        headers=headers,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_admin_user_put(client):
    """Test case for admin_user_put

    Edit user
    """
    access_token = await generate_access_token('v.baydin')
    body = {
        "globalRole": "USER",
        "groups": [{
            "mode": "READ",
            "groupId": "groupId",
            "description": "description"
        }, {
            "mode": "READ",
            "groupId": "unittest",
            "description": "description"
        }],
        "userId": "unittest"
    }
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token[0]}'
    }
    response = await client.request(
        method='PUT',
        path='/api/auth/v2/admin/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_generate_refresh_token(client):
    """Test case for generate_refresh_token

    generate refresh token with arbitrary lifetime e.g. for services
    """
    body = {
        "expirationDateTime": "2000-01-23T04:56:07.000+00:00",
        "tokenName": "tokenName",
        "groups": [{
            "mode": "READ",
            "groupId": "groupId",
            "description": "description"
        }, {
            "mode": "READ",
            "groupId": "groupId",
            "description": "description"
        }]
    }
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'CookieAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/auth/v2/admin/refreshTokens',
        headers=headers,
        json=body,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_token_info(client):
    """Test case for get_token_info

    list all refresh tokens
    """
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'CookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/auth/v2/admin/refreshTokens/{token_id}'.format(token_id='token_id_example'),
        headers=headers,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_list_refresh_tokens(client):
    """Test case for list_refresh_tokens

    list all refresh tokens
    """
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'CookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/auth/v2/admin/refreshTokens',
        headers=headers,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_revoke_refresh_token(client):
    """Test case for revoke_refresh_token

    generate refresh token with arbitrary lifetime e.g. for services
    """
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'CookieAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/auth/v2/admin/refreshTokens/{token_id}'.format(token_id='token_id_example'),
        headers=headers,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')
