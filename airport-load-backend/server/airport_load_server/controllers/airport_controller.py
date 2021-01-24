from typing import List, Dict
from aiohttp import web

from airport_load_server.models.api_error import ApiError
from airport_load_server.models.detailed_airport_load_info import DetailedAirportLoadInfo
from airport_load_server import util


async def get_airport_information(request: web.Request, airport_code, token_info=None) -> web.Response:
    """get detailed information in seelcted airport

    

    :param airport_code: 
    :type airport_code: str

    """
    return web.Response(status=200)
