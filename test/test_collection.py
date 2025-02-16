# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.models.collection import Collection

class TestCollection(unittest.TestCase):
    """Collection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Collection:
        """Test Collection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Collection`
        """
        model = Collection()
        if include_optional:
            return Collection(
                id = 7287575,
                name = 'Calibration objects (By CreativeTools)',
                description = 'meep',
                description_html = '<div><p><strong>meep</strong></p></div>
',
                added = '2017-01-16T22:21:25Z',
                modified = '2020-05-26T14:23:36Z',
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
                url = 'https://api.thingiverse.com/collections/7287575',
                count = 1,
                is_editable = False,
                is_featured = False,
                is_liked = False,
                is_watched = False,
                featured_on = '',
                featured_thing_id = 0,
                preview_image = 'https://cdn.thingiverse.com/renders/98/d7/7c/14/a1/8169058952_beddf5f755_o_preview_card.jpg',
                absolute_url = 'https://staging.thingiverse.com/CreativeTools/collections/7287575/things',
                thumbnail = 'https://cdn.thingiverse.com/renders/98/d7/7c/14/a1/8169058952_beddf5f755_o_preview_medium.jpg'
            )
        else:
            return Collection(
                id = 7287575,
                name = 'Calibration objects (By CreativeTools)',
                description = 'meep',
                added = '2017-01-16T22:21:25Z',
                modified = '2020-05-26T14:23:36Z',
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
                url = 'https://api.thingiverse.com/collections/7287575',
                count = 1,
                is_editable = False,
                is_featured = False,
                is_watched = False,
                featured_thing_id = 0,
                preview_image = 'https://cdn.thingiverse.com/renders/98/d7/7c/14/a1/8169058952_beddf5f755_o_preview_card.jpg',
                absolute_url = 'https://staging.thingiverse.com/CreativeTools/collections/7287575/things',
                thumbnail = 'https://cdn.thingiverse.com/renders/98/d7/7c/14/a1/8169058952_beddf5f755_o_preview_medium.jpg',
        )
        """

    def testCollection(self):
        """Test Collection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
