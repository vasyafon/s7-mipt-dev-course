import datetime
import os
from typing import Optional, Tuple

import pytz
from authlib.jose import jwt
import base64
from auth_server.functions.models import UserInfo, GlobalRole
from auth_server.functions.users import get_user_info

AUTH_PRIVATE_KEY = os.environ.get('AUTH_PRIVATE_KEY', None)
assert AUTH_PRIVATE_KEY is not None


async def mock_user_info(user_id: str) -> Optional[UserInfo]:
    if user_id == 'v.baydin':
        return UserInfo(
            userId=user_id,
            globalRole=GlobalRole.admin,
            groups=[]
        )
    else:
        return None


async def generate_access_token(user_id: str) -> Tuple[Optional[str], datetime.datetime]:
    user_info = await get_user_info(user_id, create_default=False)
    if user_info is None:
        user_info = UserInfo(
            userId=user_id,
            globalRole=GlobalRole.user,
            groups=[]
        )
    exp = datetime.datetime.now(tz=pytz.UTC) + datetime.timedelta(minutes=10)
    data = {
        "sub": user_id,
        "exp": exp,
        "user_info": str(user_info.json(by_alias=True))
    }
    token = jwt.encode(header={
        "alg": "RS256",
        "typ": "JWT"
    }, payload=data, key=base64.b64decode(AUTH_PRIVATE_KEY))
    return token.decode('utf-8'), exp
