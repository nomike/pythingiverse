# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.models.group_forum import GroupForum

class TestGroupForum(unittest.TestCase):
    """GroupForum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupForum:
        """Test GroupForum
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupForum`
        """
        model = GroupForum()
        if include_optional:
            return GroupForum(
                id = 56,
                name = '',
                description = '',
                slug = '',
                thumbnail = '',
                topic_count = 56,
                tags = [
                    ''
                    ]
            )
        else:
            return GroupForum(
        )
        """

    def testGroupForum(self):
        """Test GroupForum"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
