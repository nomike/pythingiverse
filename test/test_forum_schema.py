# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.models.forum_schema import ForumSchema

class TestForumSchema(unittest.TestCase):
    """ForumSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ForumSchema:
        """Test ForumSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ForumSchema`
        """
        model = ForumSchema()
        if include_optional:
            return ForumSchema(
                id = 56,
                name = '',
                slug = '',
                thumbnail = '',
                topic_count = 56
            )
        else:
            return ForumSchema(
        )
        """

    def testForumSchema(self):
        """Test ForumSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
