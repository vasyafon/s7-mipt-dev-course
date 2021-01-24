# coding: utf-8

import pytest
import json
from aiohttp import web



async def test_health_liveness_get(client):
    """Test case for health_liveness_get

    liveness probe
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/auth/v2/health/liveness',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_health_readiness_get(client):
    """Test case for health_readiness_get

    readiness probe
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/auth/v2/health/readiness',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

