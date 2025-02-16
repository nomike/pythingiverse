# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.models.topic_schema_comment_of_topic import TopicSchemaCommentOfTopic

class TestTopicSchemaCommentOfTopic(unittest.TestCase):
    """TopicSchemaCommentOfTopic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TopicSchemaCommentOfTopic:
        """Test TopicSchemaCommentOfTopic
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TopicSchemaCommentOfTopic`
        """
        model = TopicSchemaCommentOfTopic()
        if include_optional:
            return TopicSchemaCommentOfTopic(
                id = 56,
                topic_name = '',
                body = '',
                body_html = '',
                public_url = '',
                url = '',
                target_url = '',
                target_type = '',
                target_id = 56,
                parent_id = 56,
                parent_url = '',
                has_children = True,
                needs_moderation = True,
                is_root_comment = True,
                is_deleted = True,
                added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified = None,
                attachments = [
                    thingiverse.models.comment_attachments_inner.Comment_attachments_inner(
                        id = 56, 
                        name = '', 
                        download_url = '', )
                    ],
                user = thingiverse.models.user_summary_schema_1.user_summary_schema_1(
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
                things = [
                    thingiverse.models.topic_schema_comment_of_topic_things_inner.topic_schema_comment_of_topic_things_inner(
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
                        is_published = True, 
                        is_nsfw = True, 
                        is_purchased = True, 
                        is_private = True, 
                        collect_count = 56, 
                        comment_count = 56, )
                    ]
            )
        else:
            return TopicSchemaCommentOfTopic(
        )
        """

    def testTopicSchemaCommentOfTopic(self):
        """Test TopicSchemaCommentOfTopic"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
