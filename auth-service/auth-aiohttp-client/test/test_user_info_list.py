# coding: utf-8

"""
    Auth server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import auth_aiohttp_client
from auth_aiohttp_client.models.user_info_list import UserInfoList  # noqa: E501
from auth_aiohttp_client.rest import ApiException

class TestUserInfoList(unittest.TestCase):
    """UserInfoList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserInfoList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = auth_aiohttp_client.models.user_info_list.UserInfoList()  # noqa: E501
        if include_optional :
            return UserInfoList(
                users = [
                    auth_aiohttp_client.models.user_info.UserInfo(
                        user_id = '', 
                        global_role = 'ADMIN', 
                        groups = [
                            auth_aiohttp_client.models.group_info.GroupInfo(
                                group_id = '', 
                                description = '', 
                                mode = 'READ', )
                            ], )
                    ]
            )
        else :
            return UserInfoList(
        )

    def testUserInfoList(self):
        """Test UserInfoList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
