from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class AuthMethod(Enum):
    bearer = 0
    cookie = 1


class TokenInfo(object):
    __data: dict

    def __init__(self, user_id: str = None, groups_read: List[str] = None, groups_write: List[str] = None,
                 groups_admin: List[str] = None, api_key: str = None, auth_method=AuthMethod.bearer):
        self.__data = {}
        self.__data['user_id'] = user_id
        self.__data['groups_read'] = groups_read
        self.__data['groups_write'] = groups_write
        self.__data['groups_admin'] = groups_admin
        self.__data['api_key'] = api_key
        self.__data['auth_method'] = auth_method

    def get(self, key, default=None):
        if hasattr(self, key):
            return getattr(self, key)
        else:
            return default

    @property
    def user_id(self) -> str:
        return self.__data['user_id']

    @property
    def uid(self) -> str:
        return self.__data['user_id']

    @property
    def sub(self) -> str:
        return self.__data['user_id']

    @property
    def groups_read(self) -> List[str]:
        return self.__data['groups_read']

    @property
    def groups_write(self) -> List[str]:
        return self.__data['groups_write']

    @property
    def groups_admin(self) -> List[str]:
        return self.__data['groups_admin']

    @property
    def api_key(self) -> str:
        return self.__data['api_key']

    @property
    def auth_method(self) -> AuthMethod:
        return self.__data['auth_method']


class Mode(Enum):
    read = 'READ'
    write = 'WRITE'
    admin = 'ADMIN'


class GroupInfo(BaseModel):
    group_id: Optional[str] = Field(None, alias='groupId')
    description: Optional[str] = None
    mode: Optional[Mode] = None


class GlobalRole(Enum):
    admin = 'ADMIN'
    user = 'USER'


class UserInfo(BaseModel):
    user_id: Optional[str] = Field(None, alias='userId')
    global_role: Optional[GlobalRole] = Field(None, alias='globalRole')
    groups: Optional[List[GroupInfo]] = None
