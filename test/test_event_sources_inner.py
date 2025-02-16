# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thingiverse.models.event_sources_inner import EventSourcesInner

class TestEventSourcesInner(unittest.TestCase):
    """EventSourcesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventSourcesInner:
        """Test EventSourcesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventSourcesInner`
        """
        model = EventSourcesInner()
        if include_optional:
            return EventSourcesInner(
                thumbnail = '',
                default_image = thingiverse.models.image_summary_schema.image_summary_schema(
                    id = 2012326, 
                    url = 'https://cdn.thingiverse.com/assets/ee/dc/9a/fb/74/1_3D-printed_3DBenchy_by_Creative-Tools.com.JPG', 
                    name = '1_3D-printed_3DBenchy_by_Creative-Tools.com.JPG', 
                    sizes = [
                        thingiverse.models.image_summary_sizes_inner.ImageSummary_sizes_inner(
                            type = 'thumb', 
                            size = 'large', 
                            url = 'https://cdn.thingiverse.com/renders/62/ab/d7/e3/ea/1_3D-printed_3DBenchy_by_Creative-Tools.com_thumb_large.JPG', )
                        ], 
                    added = '2015-04-09T12:55:23Z', )
            )
        else:
            return EventSourcesInner(
        )
        """

    def testEventSourcesInner(self):
        """Test EventSourcesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
