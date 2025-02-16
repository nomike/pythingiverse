# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.api.file_api import FileApi


class TestFileApi(unittest.TestCase):
    """FileApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FileApi()

    def tearDown(self) -> None:
        pass

    def test_files0_upload_file_post(self) -> None:
        """Test case for files0_upload_file_post

        Upload a file as pendingupload
        """
        pass

    def test_files_file_id_download_get(self) -> None:
        """Test case for files_file_id_download_get

        Get tracked download URL
        """
        pass

    def test_files_file_id_get(self) -> None:
        """Test case for files_file_id_get

        Get info about a file by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
