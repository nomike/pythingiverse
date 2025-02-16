# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.api.comment_api import CommentApi


class TestCommentApi(unittest.TestCase):
    """CommentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CommentApi()

    def tearDown(self) -> None:
        pass

    def test_comments0_markdown_post(self) -> None:
        """Test case for comments0_markdown_post

        Convert text to markdown
        """
        pass

    def test_comments_comment_id_delete(self) -> None:
        """Test case for comments_comment_id_delete

        Softdelete a comment
        """
        pass

    def test_comments_comment_id_get(self) -> None:
        """Test case for comments_comment_id_get

        Get a comment by id
        """
        pass

    def test_comments_comment_id_patch(self) -> None:
        """Test case for comments_comment_id_patch

        Update a comment
        """
        pass

    def test_comments_comment_id_replies_get(self) -> None:
        """Test case for comments_comment_id_replies_get

        Get replies of a certain comment
        """
        pass

    def test_comments_comment_id_reply_post(self) -> None:
        """Test case for comments_comment_id_reply_post

        Reply to a comment
        """
        pass

    def test_comments_comment_id_restore_post(self) -> None:
        """Test case for comments_comment_id_restore_post

        Restore a deleted comment
        """
        pass

    def test_comments_comment_id_spam_post(self) -> None:
        """Test case for comments_comment_id_spam_post

        Mark comment as a spam
        """
        pass

    def test_comments_get(self) -> None:
        """Test case for comments_get

        Get the latest comments
        """
        pass

    def test_comments_post(self) -> None:
        """Test case for comments_post

        Reply to a comment
        """
        pass


if __name__ == '__main__':
    unittest.main()
