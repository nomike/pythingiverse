# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.models.subscriptions0_dashboard_get200_response_items_inner import Subscriptions0DashboardGet200ResponseItemsInner

class TestSubscriptions0DashboardGet200ResponseItemsInner(unittest.TestCase):
    """Subscriptions0DashboardGet200ResponseItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Subscriptions0DashboardGet200ResponseItemsInner:
        """Test Subscriptions0DashboardGet200ResponseItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Subscriptions0DashboardGet200ResponseItemsInner`
        """
        model = Subscriptions0DashboardGet200ResponseItemsInner()
        if include_optional:
            return Subscriptions0DashboardGet200ResponseItemsInner(
                message = '',
                image = thingiverse.models._subscriptions_0_dashboard_get_200_response_items_inner_image._subscriptions_0_dashboard_get_200_response_items_inner_image(
                    link = '', 
                    title = '', 
                    img_src = '', ),
                type = '',
                is_subscribed = True,
                user = thingiverse.models.user_schema.user_schema(
                    id = 1336, 
                    name = 'CreativeTools', 
                    first_name = 'Creative', 
                    last_name = 'Tools', 
                    email = 'thingiverse@creativetools.se', 
                    url = 'https://api.thingiverse.com/users/CreativeTools', 
                    public_url = 'https://www.thingiverse.com/CreativeTools', 
                    thumbnail = 'https://cdn.thingiverse.com/renders/b3/a5/0c/45/3f/CT_thumb_medium.jpg', 
                    bio = 'Creative Tools offers a wide range of software and hardware for both beginners and professional 2D and 3D creators. We always release [our 3D models](http:\/\/www.thingiverse.com\/CreativeTools\/designs) free of charge for anyone to download and use. Please [let us know](mailto:thingiverse@creativetools.se) if you have comments on our files or want to suggest future project ideas. Your feedback is highly appreciated!\r\n\r\n### Do you like our designs?\r\nPlease support us by placing your next 3D related order at [www.creativetools.se](https:\/\/www.creativetools.se\/). We offer a wide range of 3D software and 3D hardware, and are authorized resellers of well-known brands such as [Autodesk](https:\/\/www.creativetools.se\/autodesk), [Adobe](https:\/\/www.creativetools.se\/adobe), [Chaos Group](https:\/\/www.creativetools.se\/chaos-group), [Ultimaker](https:\/\/www.creativetools.se\/ultimaker), [Flashforge](https:\/\/www.creativetools.se\/flashforge), [MakerBot](https:\/\/www.creativetools.se\/makerbot) and [Formlabs](https:\/\/www.creativetools.se\/formlabs).\r\n\r\n\r\nWe would be honoured to serve you as a customer at [www.creativetools.se](https:\/\/www.creativetools.se).\r\n\r\n* * *  \r\n######[Online store](https:\/\/www.creativetools.se\/) - [Blog](https:\/\/blog.creativetools.se\/) -  [#3DBenchy](http:\/\/www.3DBenchy.com) - [Twitter](http:\/\/twitter.com\/CreativeTools) - [Facebook](http:\/\/facebook.com\/creativetools) - [YouTube](http:\/\/youtube.com\/creativetools) - [Instagram](http:\/\/instagram.com\/creative_tools) - [LinkedIn](https:\/\/www.linkedin.com\/company\/creative-tools)', 
                    bio_html = '<div><p>Creative Tools offers a wide range of software and hardware for both beginners and professional 2D and 3D creators. We always release <a rel=\"ugc nofollow\" href=\"/CreativeTools/designs\">our 3D models</a> free of charge for anyone to download and use. Please <a href=\"mailto:thingiverse%20at%20creativetools.se\">let us know</a> if you have comments on our files or want to suggest future project ideas. Your feedback is highly appreciated!</p><h3>Do you like our designs?</h3><p>Please support us by placing your next 3D related order at <a rel=\"ugc nofollow\" href=\"https://www.creativetools.se/\">www.creativetools.se</a>. We offer a wide range of 3D software and 3D hardware, and are authorized resellers of well-known brands such as <a rel=\"ugc nofollow\" href=\"https://www.creativetools.se/autodesk\">Autodesk</a>, <a rel=\"ugc nofollow\" href=\"https://www.creativetools.se/adobe\">Adobe</a>, <a rel=\"ugc nofollow\" href=\"https://www.creativetools.se/chaos-group\">Chaos Group</a>, <a rel=\"ugc nofollow\" href=\"https://www.creativetools.se/ultimaker\">Ultimaker</a>, <a rel=\"ugc nofollow\" href=\"https://www.creativetools.se/flashforge\">Flashforge</a>, <a rel=\"ugc nofollow\" href=\"https://www.creativetools.se/makerbot\">MakerBot</a> and <a rel=\"ugc nofollow\" href=\"https://www.creativetools.se/formlabs\">Formlabs</a>.</p><p>We would be honoured to serve you as a customer at <a rel=\"ugc nofollow\" href=\"https://www.creativetools.se\">www.creativetools.se</a>.</p><hr><h6><a rel=\"ugc nofollow\" href=\"https://www.creativetools.se/\">Online store</a> - <a rel=\"ugc nofollow\" href=\"https://blog.creativetools.se/\">Blog</a> -  <a rel=\"ugc nofollow\" href=\"http://www.3DBenchy.com\">#3DBenchy</a> - <a rel=\"ugc nofollow\" href=\"http://twitter.com/CreativeTools\">Twitter</a> - <a rel=\"ugc nofollow\" href=\"http://facebook.com/creativetools\">Facebook</a> - <a rel=\"ugc nofollow\" href=\"http://youtube.com/creativetools\">YouTube</a> - <a rel=\"ugc nofollow\" href=\"http://instagram.com/creative_tools\">Instagram</a> - <a rel=\"ugc nofollow\" href=\"https://www.linkedin.com/company/creative-tools\">LinkedIn</a></h6></div>\n', 
                    level = 10, 
                    location = 'Halmstad, Sweden', 
                    country = '', 
                    registered = '2009-11-10T10:49:44Z', 
                    last_active = '2023-08-01T13:53:53Z', 
                    cover_image = 'https://cdn.thingiverse.com/renders/6d/54/65/5c/9b/Thingiverse_background_3_preview_birdwing.jpg', 
                    things_url = 'https://api.thingiverse.com/users/CreativeTools/things', 
                    copies_url = 'https://api.thingiverse.com/users/CreativeTools/copies', 
                    likes_url = 'https://api.thingiverse.com/users/CreativeTools/likes', 
                    printers = [
                        thingiverse.models.user_printers_inner.User_printers_inner(
                            id = 2553, 
                            name = 'An army of 3D printers', 
                            public_url = '', )
                        ], 
                    programs = [
                        thingiverse.models.user_programs_inner.User_programs_inner(
                            id = 38, 
                            name = 'Rhino', )
                        ], 
                    types = [
                        thingiverse.models.user_types_inner.User_types_inner(
                            id = 12, 
                            name = 'Professional', )
                        ], 
                    skill_level = 'Advanced', 
                    accepts_tips = False, 
                    groups = [
                        thingiverse.models.user_groups_inner.User_groups_inner(
                            id = 25, 
                            name = 'Engineering', 
                            public_url = 'https://www.thingiverse.com/groups/engineering', )
                        ], 
                    website = 'http://CreativeTools.se', 
                    twitter = thingiverse.models.user_twitter.User_twitter(
                        account_name = 'CreativeTools', 
                        account_url = 'http://twitter.com/CreativeTools', ), 
                    count_of_followers = 9828, 
                    count_of_following = 975, 
                    count_of_designs = 147, 
                    collection_count = 16, 
                    make_count = 56, 
                    like_count = 56, 
                    has_favorite = True, 
                    favorite_count = 6, 
                    is_admin = False, 
                    is_moderator = False, 
                    is_featured = False, 
                    is_verified = False, 
                    is_following = True, ),
                is_personal = True,
                time = '',
                id = 56,
                content = None
            )
        else:
            return Subscriptions0DashboardGet200ResponseItemsInner(
        )
        """

    def testSubscriptions0DashboardGet200ResponseItemsInner(self):
        """Test Subscriptions0DashboardGet200ResponseItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
