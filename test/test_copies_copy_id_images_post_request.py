# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.models.copies_copy_id_images_post_request import CopiesCopyIdImagesPostRequest

class TestCopiesCopyIdImagesPostRequest(unittest.TestCase):
    """CopiesCopyIdImagesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CopiesCopyIdImagesPostRequest:
        """Test CopiesCopyIdImagesPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CopiesCopyIdImagesPostRequest`
        """
        model = CopiesCopyIdImagesPostRequest()
        if include_optional:
            return CopiesCopyIdImagesPostRequest(
                filename = None
            )
        else:
            return CopiesCopyIdImagesPostRequest(
        )
        """

    def testCopiesCopyIdImagesPostRequest(self):
        """Test CopiesCopyIdImagesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
