# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.api.thing_ops_api import ThingOpsApi


class TestThingOpsApi(unittest.TestCase):
    """ThingOpsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ThingOpsApi()

    def tearDown(self) -> None:
        pass

    def test_thingops_ids_copy_post(self) -> None:
        """Test case for thingops_ids_copy_post

        Copy a thing(s) to a new collection
        """
        pass

    def test_thingops_ids_move_post(self) -> None:
        """Test case for thingops_ids_move_post

        Move a thing(s) to a new collection
        """
        pass

    def test_thingops_ids_remove_post(self) -> None:
        """Test case for thingops_ids_remove_post

        Remove a thing(s) from a collection
        """
        pass


if __name__ == '__main__':
    unittest.main()
