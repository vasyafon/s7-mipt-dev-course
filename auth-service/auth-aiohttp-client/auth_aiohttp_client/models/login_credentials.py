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


class LoginCredentials(object):
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
        'code': 'str',
        'code_verifier': 'str',
        'nonce': 'str',
        'redirect_uri': 'str'
    }

    attribute_map = {
        'code': 'code',
        'code_verifier': 'codeVerifier',
        'nonce': 'nonce',
        'redirect_uri': 'redirectUri'
    }

    def __init__(self, code=None, code_verifier=None, nonce=None, redirect_uri=None, local_vars_configuration=None):  # noqa: E501
        """LoginCredentials - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._code_verifier = None
        self._nonce = None
        self._redirect_uri = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if code_verifier is not None:
            self.code_verifier = code_verifier
        if nonce is not None:
            self.nonce = nonce
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri

    @property
    def code(self):
        """Gets the code of this LoginCredentials.  # noqa: E501


        :return: The code of this LoginCredentials.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LoginCredentials.


        :param code: The code of this LoginCredentials.  # noqa: E501
        :type code: str
        """

        self._code = code

    @property
    def code_verifier(self):
        """Gets the code_verifier of this LoginCredentials.  # noqa: E501


        :return: The code_verifier of this LoginCredentials.  # noqa: E501
        :rtype: str
        """
        return self._code_verifier

    @code_verifier.setter
    def code_verifier(self, code_verifier):
        """Sets the code_verifier of this LoginCredentials.


        :param code_verifier: The code_verifier of this LoginCredentials.  # noqa: E501
        :type code_verifier: str
        """

        self._code_verifier = code_verifier

    @property
    def nonce(self):
        """Gets the nonce of this LoginCredentials.  # noqa: E501


        :return: The nonce of this LoginCredentials.  # noqa: E501
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this LoginCredentials.


        :param nonce: The nonce of this LoginCredentials.  # noqa: E501
        :type nonce: str
        """

        self._nonce = nonce

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this LoginCredentials.  # noqa: E501


        :return: The redirect_uri of this LoginCredentials.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this LoginCredentials.


        :param redirect_uri: The redirect_uri of this LoginCredentials.  # noqa: E501
        :type redirect_uri: str
        """

        self._redirect_uri = redirect_uri

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
        if not isinstance(other, LoginCredentials):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoginCredentials):
            return True

        return self.to_dict() != other.to_dict()
