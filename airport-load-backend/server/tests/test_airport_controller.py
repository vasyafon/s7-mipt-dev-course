# coding: utf-8

import pytest
import json
from aiohttp import web

from airport_load_server.models.api_error import ApiError
from airport_load_server.models.detailed_airport_load_info import DetailedAirportLoadInfo


async def test_get_airport_information(client,get_access_token):
    """Test case for get_airport_information

    get detailed information in seelcted airport
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': f'Bearer {get_access_token}',
    }
    response = await client.request(
        method='GET',
        path='/api/airportLoad/v1/airport/{airport_code}'.format(airport_code='airport_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

