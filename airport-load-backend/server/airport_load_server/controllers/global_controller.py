from typing import List, Dict

import orjson
from aiohttp import web

from airport_load_server.functions.global_info import get_global_load
from airport_load_server.models.api_error import ApiError
from airport_load_server.models.global_load_info import GlobalLoadInfo
from airport_load_server import util


async def get_global_info(request: web.Request, token_info=None) -> web.Response:
    """get global situation in all airports
    """
    result = await get_global_load()
    return web.Response(status=200, body=orjson.dumps(result.to_dict()))
