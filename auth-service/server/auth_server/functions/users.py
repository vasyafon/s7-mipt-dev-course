from typing import Optional, List

import asyncpg.exceptions

from auth_server import db
from auth_server.functions.api_error import ApiError
from auth_server.functions.models import UserInfo, GlobalRole, GroupInfo, UserInfoList, Mode
from auth_server.functions.orm_models import GroupOrm, UserOrm, UserGroupOrm


async def add_user(user_info: UserInfo):
    try:
        async with db.acquire():
            if (await UserOrm.get(user_info.user_id)) is not None:
                raise ApiError(409, 'User already exists')
            role = user_info.global_role
            await UserOrm.create(user_id=user_info.user_id, global_role=role)
            if user_info.groups is not None:
                for g in user_info.groups:
                    group: Optional[GroupOrm] = await GroupOrm.get(g.group_id)
                    if group is None:
                        await GroupOrm.create(group_id=g.group_id, description=g.description)
                    await UserGroupOrm.create(user_id=user_info.user_id, group_id=g.group_id, mode=g.mode)
    except asyncpg.exceptions.IntegrityConstraintViolationError as ex:
        print(str(ex))
        await delete_user(user_info.user_id)

        raise ApiError(400, 'Some error')

    result = await get_user_info(user_info.user_id)
    return result


async def get_user_info(user_id, create_default=False) -> Optional[UserInfo]:
    async with db.acquire():
        u: UserOrm = await UserOrm.get(user_id)
        if u is None:
            if not create_default:
                return None
            else:
                return await add_user(UserInfo(
                    userId=user_id,
                    globalRole=GlobalRole.user,
                    groups=[
                        # GroupInfo(
                        # groupId='common',
                        # description='Common group for all users',
                        # mode=Mode.read)
                    ]
                ))

        user = UserInfo(userId=user_id, globalRole=GlobalRole(u.global_role))

        user_groups = await db.select(
            [
                UserGroupOrm.group_id, UserGroupOrm.mode,
                GroupOrm.description

            ]
        ).select_from(
            UserGroupOrm.join(GroupOrm)
        ).where(
            UserGroupOrm.user_id == user_id
        ).gino.all()
        user.groups = []
        for ug in user_groups:
            user.groups.append(GroupInfo(groupId=ug.group_id, description=ug.description, mode=ug.mode))
        return user


async def delete_user(user_id):
    async with db.acquire():
        u: UserOrm = await UserOrm.get(user_id)
        if u is None:
            raise ApiError(404, 'User not found')
        await UserGroupOrm.delete.where(UserGroupOrm.user_id == user_id).gino.status()
        await u.delete()


async def get_all_users() -> UserInfoList:
    async with db.acquire():
        user_ids = await UserOrm.select('user_id').gino.all()
    user_info_list = UserInfoList(users=[])
    for u in user_ids:
        user = await get_user_info(u[0])
        user_info_list.users.append(user)
    return user_info_list


async def put_user(user: UserInfo) -> UserInfo:
    try:
        async with db.acquire():
            user_orm = await UserOrm.get(user.user_id)
            if user_orm is None:
                raise ApiError(404, 'User not found')
            await user_orm.update(global_role=user.global_role).apply()

            await UserGroupOrm.delete.where(UserGroupOrm.user_id == user.user_id).gino.status()
            if user.groups is not None:
                for g in user.groups:
                    group: Optional[GroupOrm] = await GroupOrm.get(g.group_id)
                    if group is None:
                        await GroupOrm.create(group_id=g.group_id, description=g.description)
                    await UserGroupOrm.create(user_id=user.user_id, group_id=g.group_id, mode=g.mode)
    except asyncpg.exceptions.IntegrityConstraintViolationError:
        raise ApiError(400, 'Some error')
    result = await get_user_info(user.user_id)
    return result
