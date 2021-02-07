from aiohttp_session import get_session

from auth_server.functions.access_token import generate_access_token
from auth_server.functions.api_error import ApiError
from auth_server.functions.models import TokenResponse, UserInfo
from auth_server.functions.refresh_token import get_user_id_by_refresh_token


async def refresh(request, token_info: dict):
    session = await get_session(request)
    if 'user_info' in token_info:
        user_info: UserInfo = token_info['user_info']
        user_id = user_info.user_id
    elif 'sub_coro' in token_info:
        user_id = await token_info['sub_coro']
        if user_id is None:
            raise ApiError(401, 'Unauthorized')
        token_info['sub'] = user_id
    elif 'refresh_token' in session:
        refresh_token = session['refresh_token']
        user_id = await get_user_id_by_refresh_token(refresh_token)
    else:
        raise ApiError(401, 'auth key error')
    access_token, exp = await generate_access_token(user_id)
    result = TokenResponse(token=access_token, expiresAt=exp)
    return result