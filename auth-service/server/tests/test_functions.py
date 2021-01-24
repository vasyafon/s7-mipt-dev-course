from dsm_auth_server.functions.access_token import generate_access_token
from dsm_auth_server.functions.refresh_token import get_user_id_by_refresh_token


async def test_get_access_token(client):
    token,exp = await generate_access_token('v.baydin')


async def test_get_user_by_refresh_token(client):
    await  get_user_id_by_refresh_token('74273bd6-ff19-4e09-ab92-158494e044e1')