# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.models.comment_modified import CommentModified

class TestCommentModified(unittest.TestCase):
    """CommentModified unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommentModified:
        """Test CommentModified
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommentModified`
        """
        model = CommentModified()
        if include_optional:
            return CommentModified(
            )
        else:
            return CommentModified(
        )
        """

    def testCommentModified(self):
        """Test CommentModified"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
