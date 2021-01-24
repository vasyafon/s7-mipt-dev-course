# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from airport_load_server.models.base_model_ import Model
from airport_load_server import util


class FlightAirportLoadInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, flight_no: int=None, airport_code: str=None, pax_y_load: int=None, pax_c_load: int=None, children_y_load: int=None, children_c_load: int=None, infants_y_load: int=None, infants_c_load: int=None, scheduled_dep_datetime_utc: datetime=None, estimated_dep_datetime_utc: datetime=None):
        """FlightAirportLoadInfo - a model defined in OpenAPI

        :param flight_no: The flight_no of this FlightAirportLoadInfo.
        :param airport_code: The airport_code of this FlightAirportLoadInfo.
        :param pax_y_load: The pax_y_load of this FlightAirportLoadInfo.
        :param pax_c_load: The pax_c_load of this FlightAirportLoadInfo.
        :param children_y_load: The children_y_load of this FlightAirportLoadInfo.
        :param children_c_load: The children_c_load of this FlightAirportLoadInfo.
        :param infants_y_load: The infants_y_load of this FlightAirportLoadInfo.
        :param infants_c_load: The infants_c_load of this FlightAirportLoadInfo.
        :param scheduled_dep_datetime_utc: The scheduled_dep_datetime_utc of this FlightAirportLoadInfo.
        :param estimated_dep_datetime_utc: The estimated_dep_datetime_utc of this FlightAirportLoadInfo.
        """
        self.openapi_types = {
            'flight_no': int,
            'airport_code': str,
            'pax_y_load': int,
            'pax_c_load': int,
            'children_y_load': int,
            'children_c_load': int,
            'infants_y_load': int,
            'infants_c_load': int,
            'scheduled_dep_datetime_utc': datetime,
            'estimated_dep_datetime_utc': datetime
        }

        self.attribute_map = {
            'flight_no': 'flightNo',
            'airport_code': 'airportCode',
            'pax_y_load': 'paxYLoad',
            'pax_c_load': 'paxCLoad',
            'children_y_load': 'childrenYLoad',
            'children_c_load': 'childrenCLoad',
            'infants_y_load': 'infantsYLoad',
            'infants_c_load': 'infantsCLoad',
            'scheduled_dep_datetime_utc': 'scheduledDepDatetimeUTC',
            'estimated_dep_datetime_utc': 'estimatedDepDatetimeUTC'
        }

        self._flight_no = flight_no
        self._airport_code = airport_code
        self._pax_y_load = pax_y_load
        self._pax_c_load = pax_c_load
        self._children_y_load = children_y_load
        self._children_c_load = children_c_load
        self._infants_y_load = infants_y_load
        self._infants_c_load = infants_c_load
        self._scheduled_dep_datetime_utc = scheduled_dep_datetime_utc
        self._estimated_dep_datetime_utc = estimated_dep_datetime_utc

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FlightAirportLoadInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FlightAirportLoadInfo of this FlightAirportLoadInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def flight_no(self):
        """Gets the flight_no of this FlightAirportLoadInfo.


        :return: The flight_no of this FlightAirportLoadInfo.
        :rtype: int
        """
        return self._flight_no

    @flight_no.setter
    def flight_no(self, flight_no):
        """Sets the flight_no of this FlightAirportLoadInfo.


        :param flight_no: The flight_no of this FlightAirportLoadInfo.
        :type flight_no: int
        """
        if flight_no is None:
            raise ValueError("Invalid value for `flight_no`, must not be `None`")

        self._flight_no = flight_no

    @property
    def airport_code(self):
        """Gets the airport_code of this FlightAirportLoadInfo.


        :return: The airport_code of this FlightAirportLoadInfo.
        :rtype: str
        """
        return self._airport_code

    @airport_code.setter
    def airport_code(self, airport_code):
        """Sets the airport_code of this FlightAirportLoadInfo.


        :param airport_code: The airport_code of this FlightAirportLoadInfo.
        :type airport_code: str
        """
        if airport_code is None:
            raise ValueError("Invalid value for `airport_code`, must not be `None`")

        self._airport_code = airport_code

    @property
    def pax_y_load(self):
        """Gets the pax_y_load of this FlightAirportLoadInfo.


        :return: The pax_y_load of this FlightAirportLoadInfo.
        :rtype: int
        """
        return self._pax_y_load

    @pax_y_load.setter
    def pax_y_load(self, pax_y_load):
        """Sets the pax_y_load of this FlightAirportLoadInfo.


        :param pax_y_load: The pax_y_load of this FlightAirportLoadInfo.
        :type pax_y_load: int
        """

        self._pax_y_load = pax_y_load

    @property
    def pax_c_load(self):
        """Gets the pax_c_load of this FlightAirportLoadInfo.


        :return: The pax_c_load of this FlightAirportLoadInfo.
        :rtype: int
        """
        return self._pax_c_load

    @pax_c_load.setter
    def pax_c_load(self, pax_c_load):
        """Sets the pax_c_load of this FlightAirportLoadInfo.


        :param pax_c_load: The pax_c_load of this FlightAirportLoadInfo.
        :type pax_c_load: int
        """

        self._pax_c_load = pax_c_load

    @property
    def children_y_load(self):
        """Gets the children_y_load of this FlightAirportLoadInfo.


        :return: The children_y_load of this FlightAirportLoadInfo.
        :rtype: int
        """
        return self._children_y_load

    @children_y_load.setter
    def children_y_load(self, children_y_load):
        """Sets the children_y_load of this FlightAirportLoadInfo.


        :param children_y_load: The children_y_load of this FlightAirportLoadInfo.
        :type children_y_load: int
        """

        self._children_y_load = children_y_load

    @property
    def children_c_load(self):
        """Gets the children_c_load of this FlightAirportLoadInfo.


        :return: The children_c_load of this FlightAirportLoadInfo.
        :rtype: int
        """
        return self._children_c_load

    @children_c_load.setter
    def children_c_load(self, children_c_load):
        """Sets the children_c_load of this FlightAirportLoadInfo.


        :param children_c_load: The children_c_load of this FlightAirportLoadInfo.
        :type children_c_load: int
        """

        self._children_c_load = children_c_load

    @property
    def infants_y_load(self):
        """Gets the infants_y_load of this FlightAirportLoadInfo.


        :return: The infants_y_load of this FlightAirportLoadInfo.
        :rtype: int
        """
        return self._infants_y_load

    @infants_y_load.setter
    def infants_y_load(self, infants_y_load):
        """Sets the infants_y_load of this FlightAirportLoadInfo.


        :param infants_y_load: The infants_y_load of this FlightAirportLoadInfo.
        :type infants_y_load: int
        """

        self._infants_y_load = infants_y_load

    @property
    def infants_c_load(self):
        """Gets the infants_c_load of this FlightAirportLoadInfo.


        :return: The infants_c_load of this FlightAirportLoadInfo.
        :rtype: int
        """
        return self._infants_c_load

    @infants_c_load.setter
    def infants_c_load(self, infants_c_load):
        """Sets the infants_c_load of this FlightAirportLoadInfo.


        :param infants_c_load: The infants_c_load of this FlightAirportLoadInfo.
        :type infants_c_load: int
        """

        self._infants_c_load = infants_c_load

    @property
    def scheduled_dep_datetime_utc(self):
        """Gets the scheduled_dep_datetime_utc of this FlightAirportLoadInfo.


        :return: The scheduled_dep_datetime_utc of this FlightAirportLoadInfo.
        :rtype: datetime
        """
        return self._scheduled_dep_datetime_utc

    @scheduled_dep_datetime_utc.setter
    def scheduled_dep_datetime_utc(self, scheduled_dep_datetime_utc):
        """Sets the scheduled_dep_datetime_utc of this FlightAirportLoadInfo.


        :param scheduled_dep_datetime_utc: The scheduled_dep_datetime_utc of this FlightAirportLoadInfo.
        :type scheduled_dep_datetime_utc: datetime
        """

        self._scheduled_dep_datetime_utc = scheduled_dep_datetime_utc

    @property
    def estimated_dep_datetime_utc(self):
        """Gets the estimated_dep_datetime_utc of this FlightAirportLoadInfo.


        :return: The estimated_dep_datetime_utc of this FlightAirportLoadInfo.
        :rtype: datetime
        """
        return self._estimated_dep_datetime_utc

    @estimated_dep_datetime_utc.setter
    def estimated_dep_datetime_utc(self, estimated_dep_datetime_utc):
        """Sets the estimated_dep_datetime_utc of this FlightAirportLoadInfo.


        :param estimated_dep_datetime_utc: The estimated_dep_datetime_utc of this FlightAirportLoadInfo.
        :type estimated_dep_datetime_utc: datetime
        """

        self._estimated_dep_datetime_utc = estimated_dep_datetime_utc