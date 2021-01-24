# coding: utf-8

"""
    Auth server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from auth_aiohttp_client.configuration import Configuration


class UserInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'user_id': 'str',
        'global_role': 'str',
        'groups': 'list[GroupInfo]'
    }

    attribute_map = {
        'user_id': 'userId',
        'global_role': 'globalRole',
        'groups': 'groups'
    }

    def __init__(self, user_id=None, global_role=None, groups=None, local_vars_configuration=None):  # noqa: E501
        """UserInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._global_role = None
        self._groups = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if global_role is not None:
            self.global_role = global_role
        if groups is not None:
            self.groups = groups

    @property
    def user_id(self):
        """Gets the user_id of this UserInfo.  # noqa: E501


        :return: The user_id of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserInfo.


        :param user_id: The user_id of this UserInfo.  # noqa: E501
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def global_role(self):
        """Gets the global_role of this UserInfo.  # noqa: E501


        :return: The global_role of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._global_role

    @global_role.setter
    def global_role(self, global_role):
        """Sets the global_role of this UserInfo.


        :param global_role: The global_role of this UserInfo.  # noqa: E501
        :type global_role: str
        """
        allowed_values = ["ADMIN", "USER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and global_role not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `global_role` ({0}), must be one of {1}"  # noqa: E501
                .format(global_role, allowed_values)
            )

        self._global_role = global_role

    @property
    def groups(self):
        """Gets the groups of this UserInfo.  # noqa: E501


        :return: The groups of this UserInfo.  # noqa: E501
        :rtype: list[GroupInfo]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserInfo.


        :param groups: The groups of this UserInfo.  # noqa: E501
        :type groups: list[GroupInfo]
        """

        self._groups = groups

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserInfo):
            return True

        return self.to_dict() != other.to_dict()
