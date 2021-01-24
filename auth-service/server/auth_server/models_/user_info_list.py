# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from dsm_auth_server.models.base_model_ import Model
from dsm_auth_server.models.user_info import UserInfo
from dsm_auth_server import util


class UserInfoList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, users: List[UserInfo]=None):
        """UserInfoList - a model defined in OpenAPI

        :param users: The users of this UserInfoList.
        """
        self.openapi_types = {
            'users': List[UserInfo]
        }

        self.attribute_map = {
            'users': 'users'
        }

        self._users = users

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserInfoList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserInfoList of this UserInfoList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def users(self):
        """Gets the users of this UserInfoList.


        :return: The users of this UserInfoList.
        :rtype: List[UserInfo]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this UserInfoList.


        :param users: The users of this UserInfoList.
        :type users: List[UserInfo]
        """

        self._users = users
