import datetime
import uuid

import pytz

from auth_server.functions.access_token import generate_access_token
from auth_server.functions.api_error import ApiError
from auth_server.functions.connection import PgPool, fetch_all_query, execute_query, fetch_one_query
from pydantic import BaseModel, constr

from auth_server import Const
from auth_server.functions.models import Tokens, TokenResponse
from auth_server.functions.orm_models import db, RefreshTokenOrm


class RefreshToken(BaseModel):
    token_id: uuid.UUID
    user_id: constr(max_length=63)
    creation_date: datetime.datetime
    expiration_date: datetime.datetime
    is_revoked: bool

    class Config:
        orm_mode = True


async def generate_refresh_token_by_user(user_id):
    ## Make all valid refresh tokens invalid
    query = f'''
        update {Const.DB_SCHEMA}.refresh_tokens
        set is_revoked=true
        where user_id=$1 and expiration_date > current_date and not is_revoked 
    '''
    await execute_query(query, (user_id,))
    refresh_token = RefreshToken(
        token_id=uuid.uuid4(),
        user_id=user_id,
        creation_date=datetime.datetime.now(tz=pytz.UTC),
        expiration_date=datetime.datetime.now(tz=pytz.UTC) + datetime.timedelta(days=1),
        is_revoked=False
    )
    await RefreshTokenOrm.create(**refresh_token.dict())
    return refresh_token


async def get_user_id_by_refresh_token(refresh_token: str):
    refresh_token_uuid = uuid.UUID(refresh_token, version=4)
    async with db.acquire():
        token_data: RefreshTokenOrm = await RefreshTokenOrm.query.where(
            (RefreshTokenOrm.token_id == refresh_token_uuid) &
            (RefreshTokenOrm.expiration_date > datetime.datetime.now())
            & (RefreshTokenOrm.is_revoked.is_(False))
        ).gino.first()

    if token_data is None:
        return None
    return token_data.user_id


async def create_tokens_object(user_id) -> Tokens:
    refresh_token = await generate_refresh_token_by_user(user_id)
    access_token, access_token_exp = await generate_access_token(user_id)
    if access_token is None:
        print(f"User {user_id} is not registered in the service")
        raise ApiError
    return Tokens(
        refreshToken=TokenResponse(
            token=str(refresh_token.token_id),
            expiresAt=refresh_token.expiration_date),
        accessToken=TokenResponse(
            token=access_token,
            expiresAt=access_token_exp)
    )
