import asyncio
import datetime
import os
import uuid

import connexion
import pytz
from gino import Gino
from auth_server import Const, create_tables
from auth_server.functions.models import UserInfo, GlobalRole, GroupInfo, Mode
from auth_server.functions.orm_models import RefreshTokenOrm
from auth_server.functions.refresh_token import RefreshToken
from auth_server.functions.users import add_user, get_user_info

from auth_server import db


async def generate_unittest_cred():
    await db.set_bind(
        f'postgresql://{Const.DB_USER}:{Const.DB_PASSWORD}@{Const.DB_HOST}:{Const.DB_PORT}/{Const.DB_NAME}')
    await db.gino.create_all()
    unittest_user = await get_user_info('unittest')
    if unittest_user is None:
        await add_user(UserInfo(
            userId='unittest',
            globalRole=GlobalRole.user,
            groups=[GroupInfo(
                groupId='unittest', description='group for unit tests', mode=Mode.admin
            )]
        ))

    refresh_token = RefreshToken(
        token_id=uuid.uuid4(),
        user_id='unittest',
        creation_date=datetime.datetime.now(tz=pytz.UTC),
        expiration_date=datetime.datetime.now(tz=pytz.UTC) + datetime.timedelta(days=365),
        is_revoked=False
    )
    await RefreshTokenOrm.delete.where(RefreshTokenOrm.user_id == 'unittest').gino.status()
    await RefreshTokenOrm.create(**refresh_token.dict())
    print('Unittest refresh token: ', refresh_token.token_id)

if __name__ == '__main__':
    asyncio.run(generate_unittest_cred())
