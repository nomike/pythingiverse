# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.models.messages_post_request import MessagesPostRequest

class TestMessagesPostRequest(unittest.TestCase):
    """MessagesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MessagesPostRequest:
        """Test MessagesPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessagesPostRequest`
        """
        model = MessagesPostRequest()
        if include_optional:
            return MessagesPostRequest(
                to_user = 'MakerBot',
                subject = 'Message Subject',
                body = 'The actual message'
            )
        else:
            return MessagesPostRequest(
                to_user = 'MakerBot',
                subject = 'Message Subject',
                body = 'The actual message',
        )
        """

    def testMessagesPostRequest(self):
        """Test MessagesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
