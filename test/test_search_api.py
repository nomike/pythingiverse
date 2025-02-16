# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.api.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SearchApi()

    def tearDown(self) -> None:
        pass

    def test_search_tag_tag_get(self) -> None:
        """Test case for search_tag_tag_get

        """
        pass

    def test_search_term_autocomplete_get(self) -> None:
        """Test case for search_term_autocomplete_get

        """
        pass

    def test_search_term_typecollections_get(self) -> None:
        """Test case for search_term_typecollections_get

        Search for Collections
        """
        pass

    def test_search_term_typemakes_get(self) -> None:
        """Test case for search_term_typemakes_get

        Search for Makes
        """
        pass

    def test_search_term_typethings_get(self) -> None:
        """Test case for search_term_typethings_get

        Search for Things
        """
        pass

    def test_search_term_typeusers_get(self) -> None:
        """Test case for search_term_typeusers_get

        Search for Users
        """
        pass


if __name__ == '__main__':
    unittest.main()
