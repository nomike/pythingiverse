# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.api.message_api import MessageApi


class TestMessageApi(unittest.TestCase):
    """MessageApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MessageApi()

    def tearDown(self) -> None:
        pass

    def test_messages_post(self) -> None:
        """Test case for messages_post

        Create a new message to share a thing
        """
        pass


if __name__ == '__main__':
    unittest.main()
