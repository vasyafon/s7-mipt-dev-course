import datetime
import json
from typing import List, Optional
from uuid import UUID

from aiohttp_session import get_session
from authlib.jose import jwt
from authlib.jose.errors import DecodeError
from connexion.exceptions import OAuthResponseProblem, OAuthProblem
from cryptography import fernet
from pydantic import BaseModel

from auth_server import Const
from auth_server.functions.models import UserInfo

import os

from auth_server.functions.refresh_token import get_user_id_by_refresh_token

DEBUG = os.getenv('DEBUG', False)


def decode_api_key(api_key: str) -> Optional[dict]:
    try:
        token = jwt.decode(api_key, key=Const.AUTH_PUBLIC_KEY)
    except DecodeError:
        return None

    user_info = UserInfo.parse_raw(token['user_info'])
    t = dict(
        sub=user_info.user_id,
        expires_at=datetime.datetime.fromtimestamp(token['exp']),
        user_info=user_info
    )
    if t['expires_at'] < datetime.datetime.now() and not DEBUG:
        return None
    return t


def info_from_BearerAuth(token: str) -> dict:
    """
    Check and retrieve authentication information from custom bearer token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    Should return None if auth is invalid or does not allow access to called API.
    """
    return decode_api_key(token)


def info_from_RefreshAuth(token: str) -> Optional[dict]:
    """
    Check and retrieve authentication information from custom bearer token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    Should return None if auth is invalid or does not allow access to called API.
    """
    try:
        uuid_obj = UUID(token, version=4)
    except ValueError:
        return None
    user_id_coro = get_user_id_by_refresh_token(token)
    return {'sub_coro': user_id_coro}
