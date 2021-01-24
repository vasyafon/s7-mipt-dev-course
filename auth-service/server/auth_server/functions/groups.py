from typing import Optional

import asyncpg

from auth_server import db
from auth_server.functions.api_error import ApiError
from auth_server.functions.models import GroupPost, GroupFull, UserInGroup, GroupList
from auth_server.functions.orm_models import GroupOrm, UserGroupOrm, UserOrm


async def add_group(group_post: GroupPost) -> GroupFull:
    # try:
    async with db.acquire():
        if (await GroupOrm.get(group_post.group_id)) is not None:
            raise ApiError(409, 'Group already exists')
        await GroupOrm.create(group_id=group_post.group_id, description=group_post.description)
    # except asyncpg.exceptions.IntegrityConstraintViolationError:
    #     await delete_user(user_info.user_id)
    #     raise DsmApiError(400, 'Some error')

    result = await get_group(group_post.group_id)
    return result


async def get_group(group_id) -> Optional[GroupFull]:
    async with db.acquire():
        u: GroupOrm = await GroupOrm.get(group_id)
        if u is None:
            raise ApiError(404, 'Group not found')

        users_groups = await db.select(
            [
                UserGroupOrm.user_id, UserGroupOrm.mode
            ]
        ).select_from(
            UserGroupOrm
        ).where(
            UserGroupOrm.group_id == group_id
        ).gino.all()

        group = GroupFull(groupId=group_id, description=u.description, users=[])
        for ug in users_groups:
            uid, mode = ug
            group.users.append(UserInGroup(userId=uid, mode=mode.value))
        return group


async def delete_group(group_id):
    async with db.acquire():
        u: GroupOrm = await GroupOrm.get(group_id)
        if u is None:
            raise ApiError(404, 'Group not found')
        await UserGroupOrm.delete.where(UserGroupOrm.group_id == group_id).gino.status()
        await u.delete()


async def get_all_groups() -> GroupList:
    async with db.acquire():
        groups = await GroupOrm.select('group_id').gino.all()
    group_list = GroupList(groups=[])
    for group in groups:
        g = await get_group(group[0])
        group_list.groups.append(g)
    return group_list


async def put_group(group: GroupFull) -> GroupFull:
    try:
        async with db.acquire():
            group_orm = await GroupOrm.get(group.group_id)
            if group_orm is None:
                raise ApiError(404, 'Group not found')
            await group_orm.update(description=group.description).apply()
            if group.users is not None:
                for u in group.users:
                    user: Optional[UserOrm] = await UserOrm.get(u.user_id)
                    if user is None:
                        raise ApiError(404, 'User not found')
                    ug = await UserGroupOrm.query.where(
                        (UserGroupOrm.user_id == user.user_id) & (UserGroupOrm.group_id == group.group_id)).gino.first()
                    if ug is None:
                        await UserGroupOrm.create(user_id=user.user_id, group_id=group.group_id, mode=u.mode)
                    else:
                        await ug.update(mode=u.mode).apply()
    except asyncpg.exceptions.IntegrityConstraintViolationError:
        raise ApiError(400, 'Some error')
    result = await get_group(group.group_id)
    return result
