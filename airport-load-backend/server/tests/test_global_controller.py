# coding: utf-8

import pytest
import json
from aiohttp import web

from airport_load_server.models.api_error import ApiError
from airport_load_server.models.global_load_info import GlobalLoadInfo


async def test_get_global_info(client, get_access_token):
    """Test case for get_global_info

    get global situation in all airports
    """
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {get_access_token}',
    }
    response = await client.request(
        method='GET',
        path='/api/airportLoad/v1/global',
        headers=headers,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')
