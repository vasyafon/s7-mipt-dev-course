# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from airport_load_server.models.base_model_ import Model
from airport_load_server.models.brief_airport_load_info import BriefAirportLoadInfo
from airport_load_server import util


class GlobalLoadInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[BriefAirportLoadInfo]=None):
        """GlobalLoadInfo - a model defined in OpenAPI

        :param data: The data of this GlobalLoadInfo.
        """
        self.openapi_types = {
            'data': List[BriefAirportLoadInfo]
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GlobalLoadInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GlobalLoadInfo of this GlobalLoadInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this GlobalLoadInfo.


        :return: The data of this GlobalLoadInfo.
        :rtype: List[BriefAirportLoadInfo]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GlobalLoadInfo.


        :param data: The data of this GlobalLoadInfo.
        :type data: List[BriefAirportLoadInfo]
        """

        self._data = data