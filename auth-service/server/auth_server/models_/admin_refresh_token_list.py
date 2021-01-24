# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from dsm_auth_server.models.base_model_ import Model
from dsm_auth_server.models.admin_refresh_token_info import AdminRefreshTokenInfo
from dsm_auth_server import util


class AdminRefreshTokenList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, refresh_token_info: List[AdminRefreshTokenInfo]=None):
        """AdminRefreshTokenList - a model defined in OpenAPI

        :param refresh_token_info: The refresh_token_info of this AdminRefreshTokenList.
        """
        self.openapi_types = {
            'refresh_token_info': List[AdminRefreshTokenInfo]
        }

        self.attribute_map = {
            'refresh_token_info': 'refreshTokenInfo'
        }

        self._refresh_token_info = refresh_token_info

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AdminRefreshTokenList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AdminRefreshTokenList of this AdminRefreshTokenList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def refresh_token_info(self):
        """Gets the refresh_token_info of this AdminRefreshTokenList.


        :return: The refresh_token_info of this AdminRefreshTokenList.
        :rtype: List[AdminRefreshTokenInfo]
        """
        return self._refresh_token_info

    @refresh_token_info.setter
    def refresh_token_info(self, refresh_token_info):
        """Sets the refresh_token_info of this AdminRefreshTokenList.


        :param refresh_token_info: The refresh_token_info of this AdminRefreshTokenList.
        :type refresh_token_info: List[AdminRefreshTokenInfo]
        """

        self._refresh_token_info = refresh_token_info