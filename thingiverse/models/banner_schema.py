# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BannerSchema(BaseModel):
    """
    BannerSchema
    """ # noqa: E501
    banner_image: Optional[StrictStr] = None
    big_banner_image: Optional[StrictStr] = None
    banner_tablet_image: Optional[StrictStr] = None
    banner_mobile_image: Optional[StrictStr] = None
    banner_url: Optional[StrictStr] = None
    banner_video: Optional[StrictStr] = None
    big_banner_video: Optional[StrictStr] = None
    banner_tablet_video: Optional[StrictStr] = None
    banner_mobile_video: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["banner_image", "big_banner_image", "banner_tablet_image", "banner_mobile_image", "banner_url", "banner_video", "big_banner_video", "banner_tablet_video", "banner_mobile_video", "location"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BannerSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BannerSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "banner_image": obj.get("banner_image"),
            "big_banner_image": obj.get("big_banner_image"),
            "banner_tablet_image": obj.get("banner_tablet_image"),
            "banner_mobile_image": obj.get("banner_mobile_image"),
            "banner_url": obj.get("banner_url"),
            "banner_video": obj.get("banner_video"),
            "big_banner_video": obj.get("big_banner_video"),
            "banner_tablet_video": obj.get("banner_tablet_video"),
            "banner_mobile_video": obj.get("banner_mobile_video"),
            "location": obj.get("location")
        })
        return _obj


