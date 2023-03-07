# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onelogin
from onelogin.models.email_config import EmailConfig  # noqa: E501
from onelogin.rest import ApiException

class TestEmailConfig(unittest.TestCase):
    """EmailConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EmailConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailConfig`
        """
        model = onelogin.models.email_config.EmailConfig()  # noqa: E501
        if include_optional :
            return EmailConfig(
                address = 'smtp.sendgrid.net', 
                use_tls = True, 
                var_from = 'email@example.com', 
                domain = 'example.com', 
                user_name = 'user-name', 
                password = 'password', 
                port = 587
            )
        else :
            return EmailConfig(
                address = 'smtp.sendgrid.net',
                var_from = 'email@example.com',
                domain = 'example.com',
        )
        """

    def testEmailConfig(self):
        """Test EmailConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()