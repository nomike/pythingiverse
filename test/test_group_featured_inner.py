# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.models.group_featured_inner import GroupFeaturedInner

class TestGroupFeaturedInner(unittest.TestCase):
    """GroupFeaturedInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupFeaturedInner:
        """Test GroupFeaturedInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupFeaturedInner`
        """
        model = GroupFeaturedInner()
        if include_optional:
            return GroupFeaturedInner(
                id = 56,
                name = '',
                thumbnail = '',
                url = '',
                public_url = '',
                creator = thingiverse.models.user_summary_schema_1.user_summary_schema_1(
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
                    is_verified = False, ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_published = 0,
                is_nsfw = False,
                is_purchased = 0,
                is_private = 0,
                collect_count = 56,
                comment_count = 56,
                make_count = 56,
                like_count = 56,
                preview_image = '',
                tags = [
                    thingiverse.models.group_featured_inner_tags_inner.Group_featured_inner_tags_inner(
                        name = '', 
                        tag = '', 
                        things_url = '', 
                        absolute_url = '', 
                        url = '', 
                        count = 56, )
                    ]
            )
        else:
            return GroupFeaturedInner(
        )
        """

    def testGroupFeaturedInner(self):
        """Test GroupFeaturedInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
