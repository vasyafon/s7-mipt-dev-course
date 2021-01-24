# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from dsm_auth_server.models.base_model_ import Model
from dsm_auth_server.models.user_in_group import UserInGroup
from dsm_auth_server import util


class GroupFull(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, group_id: str=None, description: str=None, users: List[UserInGroup]=None):
        """GroupFull - a model defined in OpenAPI

        :param group_id: The group_id of this GroupFull.
        :param description: The description of this GroupFull.
        :param users: The users of this GroupFull.
        """
        self.openapi_types = {
            'group_id': str,
            'description': str,
            'users': List[UserInGroup]
        }

        self.attribute_map = {
            'group_id': 'groupId',
            'description': 'description',
            'users': 'users'
        }

        self._group_id = group_id
        self._description = description
        self._users = users

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GroupFull':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GroupFull of this GroupFull.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group_id(self):
        """Gets the group_id of this GroupFull.


        :return: The group_id of this GroupFull.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupFull.


        :param group_id: The group_id of this GroupFull.
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def description(self):
        """Gets the description of this GroupFull.


        :return: The description of this GroupFull.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GroupFull.


        :param description: The description of this GroupFull.
        :type description: str
        """

        self._description = description

    @property
    def users(self):
        """Gets the users of this GroupFull.


        :return: The users of this GroupFull.
        :rtype: List[UserInGroup]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this GroupFull.


        :param users: The users of this GroupFull.
        :type users: List[UserInGroup]
        """

        self._users = users
