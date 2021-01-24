from typing import List, Dict
from aiohttp import web

from auth_server import util


async def health_liveness_get(request: web.Request, ) -> web.Response:
    """liveness probe

    


    """
    return web.Response(status=200)


async def health_readiness_get(request: web.Request, ) -> web.Response:
    """readiness probe

    


    """
    return web.Response(status=200)
