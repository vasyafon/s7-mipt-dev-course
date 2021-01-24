from typing import List, Dict
from aiohttp import web

from auth_server.functions.groups import add_group, get_group, put_group, delete_group, get_all_groups
from auth_server.functions.models import GlobalRole, UserInfo, GroupPost, GroupFull, AdminRefreshTokenInfoPost
from auth_server.functions.users import add_user, get_user_info, delete_user, get_all_users, put_user
from auth_server import util



async def admin_add_group(request: web.Request, body, token_info: dict, **kwargs) -> web.Response:
    """add new group



    :param body: User parameters
    :type body: dict | bytes

    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')

    new_group_info = GroupPost.parse_obj(body)
    group = await add_group(new_group_info)
    return web.Response(status=200, body=group.json(by_alias=True))



async def admin_add_user(request: web.Request, body, token_info: dict, **kwargs) -> web.Response:
    """add new user

    

    :param body: User parameters
    :type body: dict | bytes

    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')

    new_user_info = UserInfo.parse_obj(body)
    result = await add_user(new_user_info)
    return web.Response(status=200, body=result.json(by_alias=True))



async def admin_get_group(request: web.Request, group_id, token_info: dict, **kwargs) -> web.Response:
    """Get group



    :param group_id:
    :type group_id: str

    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')

    group = await get_group(group_id=group_id)
    return web.Response(status=200, body=group.json(by_alias=True))



async def admin_get_user_info(request: web.Request, user_id, token_info: dict, **kwargs) -> web.Response:
    """Get user info

    

    :param user_id: 
    :type user_id: str

    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')
    result = await get_user_info(user_id)
    return web.Response(status=200, body=result.json(by_alias=True))



async def admin_group_put(request: web.Request, group_id, body, token_info: dict, **kwargs) -> web.Response:
    """Edit group



    :param group_id:
    :type group_id: str
    :param body: User parameters
    :type body: dict | bytes

    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')

    new_group_full = GroupFull.parse_obj(body)
    if new_group_full.group_id != group_id:
        return web.Response(status=400, reason='GroupId mismatch')
    group = await put_group(new_group_full)
    return web.Response(status=200, body=group.json(by_alias=True))



async def admin_list_groups(request: web.Request, token_info: dict, **kwargs) -> web.Response:
    """list all groups
    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')

    result = await get_all_groups()

    return web.Response(status=200, body=result.json(by_alias=True))



async def admin_list_users(request: web.Request, token_info: dict, **kwargs) -> web.Response:
    """list all users

    


    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')

    result = await get_all_users()

    return web.Response(status=200, body=result.json(by_alias=True))



async def admin_remove_group(request: web.Request, group_id, token_info: dict, **kwargs) -> web.Response:
    """Remove group from the system



    :param group_id:
    :type group_id: str

    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')
    await delete_group(group_id)
    return web.Response(status=200)



async def admin_remove_user(request: web.Request, user_id, token_info: dict, **kwargs) -> web.Response:
    """Remove user from the system

    

    :param user_id: 
    :type user_id: str

    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')
    result = await delete_user(user_id)
    return web.Response(status=200)



async def admin_user_put(request: web.Request, user_id, body, token_info: dict, **kwargs) -> web.Response:
    """Edit user

    

    :param user_id: 
    :type user_id: str
    :param body: User parameters
    :type body: dict | bytes

    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')
    user_info = UserInfo.parse_obj(body)
    result = await put_user(user_info)
    return web.Response(status=200, body=result.json(by_alias=True))



async def generate_refresh_token(request: web.Request, body, token_info: dict, **kwargs) -> web.Response:
    """generate refresh token with arbitrary lifetime e.g. for services

    

    :param body: Token setup
    :type body: dict | bytes

    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')
    body = AdminRefreshTokenInfoPost.parse_obj(body)
    return web.Response(status=200)



async def get_token_info(request: web.Request, token_id, token_info: dict, **kwargs) -> web.Response:
    """list all refresh tokens

    

    :param token_id: 
    :type token_id: str

    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')
    return web.Response(status=200)



async def list_refresh_tokens(request: web.Request, token_info: dict, **kwargs) -> web.Response:
    """list all refresh tokens

    


    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')
    return web.Response(status=200)



async def revoke_refresh_token(request: web.Request, token_id, token_info: dict, **kwargs) -> web.Response:
    """generate refresh token with arbitrary lifetime e.g. for services

    

    :param token_id: 
    :type token_id: str

    """
    user_info: UserInfo = token_info['user_info']
    if user_info.global_role != GlobalRole.admin:
        return web.Response(status=401, reason='Only admin can use this endpoint')
    return web.Response(status=200)
