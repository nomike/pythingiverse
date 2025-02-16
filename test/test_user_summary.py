# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.models.user_summary import UserSummary

class TestUserSummary(unittest.TestCase):
    """UserSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSummary:
        """Test UserSummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSummary`
        """
        model = UserSummary()
        if include_optional:
            return UserSummary(
                id = 1336,
                name = 'CreativeTools',
                first_name = 'Creative',
                last_name = 'Tools',
                url = 'https://api.thingiverse.com/users/CreativeTools',
                public_url = 'https://www.thingiverse.com/CreativeTools',
                thumbnail = 'https://cdn.thingiverse.com/renders/b3/a5/0c/45/3f/CT_thumb_medium.jpg',
                count_of_followers = 9828,
                count_of_following = 975,
                count_of_designs = 147,
                make_count = 56,
                accepts_tips = False,
                is_following = True,
                location = 'Halmstad, Sweden',
                cover = 'https://cdn.thingiverse.com/renders/6d/54/65/5c/9b/Thingiverse_background_3_preview_large.jpg',
                is_admin = False,
                is_moderator = False,
                is_featured = False,
                is_verified = False
            )
        else:
            return UserSummary(
        )
        """

    def testUserSummary(self):
        """Test UserSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
