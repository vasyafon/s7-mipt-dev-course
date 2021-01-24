import hashlib
import json
import os
from enum import Enum
from typing import List, Optional
import datetime

import auth_aiohttp_client
import pytz
from authlib.common.errors import AuthlibBaseError
from authlib.jose.errors import DecodeError, BadSignatureError
from auth_aiohttp_client import PublicKey
from flask.json.tag import TaggedJSONSerializer
from itsdangerous import URLSafeTimedSerializer
from pydantic import BaseModel, Field
from authlib.jose import jwt

from mipt_auth_wrapper.token_info import TokenInfo, UserInfo, AuthMethod, Mode


def decode_api_key_v2(api_key: str, auth_public_key: str, required_scopes=None) -> Optional[TokenInfo]:
    """
    Check and retrieve authentication information from api_key.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    Should return None if api_key is invalid or does not allow access to called API.
    """

    try:
        token = jwt.decode(api_key, key=auth_public_key)
    except AuthlibBaseError:
        return None

    expires_at = datetime.datetime.fromtimestamp(token['exp'])
    user_info = UserInfo.parse_raw(token['user_info'])

    now = datetime.datetime.now()
    if now > expires_at:
        return None

    t = TokenInfo(
        user_id=user_info.user_id,
        groups_read=[g.group_id for g in user_info.groups],
        groups_write=[g.group_id for g in user_info.groups if g.mode in (Mode.write, Mode.admin)],
        groups_admin=[g.group_id for g in user_info.groups if g.mode == Mode.admin],
        api_key=api_key,
        auth_method=AuthMethod.bearer
    )
    return t


async def get_auth_public_key() -> str:
    auth_url = os.getenv('AUTH_URL', 'http://localhost:8080/api/auth/v2')
    config = auth_aiohttp_client.Configuration(
        host=auth_url
    )
    api_client = auth_aiohttp_client.ApiClient(configuration=config)
    api = auth_aiohttp_client.AuthApi(api_client=api_client)
    public_key: PublicKey = await api.get_public_key()
    await api_client.close()
    return public_key.public_key


def decrypt_api_key(api_key):
    secret_key = os.getenv('FLASK_SECRET_KEY', None)
    assert secret_key is not None

    signer_kwargs = dict(
        key_derivation="hmac", digest_method=hashlib.sha1
    )

    serializer = URLSafeTimedSerializer(
        secret_key,
        salt="cookie-session",
        serializer=TaggedJSONSerializer(),
        signer_kwargs=signer_kwargs,
    )
    return serializer.loads(api_key)
