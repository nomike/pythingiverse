# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.api.event_api import EventApi


class TestEventApi(unittest.TestCase):
    """EventApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EventApi()

    def tearDown(self) -> None:
        pass

    def test_events_get(self) -> None:
        """Test case for events_get

        List of events
        """
        pass

    def test_events_id_get(self) -> None:
        """Test case for events_id_get

        Get event by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
