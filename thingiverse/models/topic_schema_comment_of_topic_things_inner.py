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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thingiverse.models.user_summary_schema1 import UserSummarySchema1
from typing import Optional, Set
from typing_extensions import Self

class TopicSchemaCommentOfTopicThingsInner(BaseModel):
    """
    TopicSchemaCommentOfTopicThingsInner
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    thumbnail: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    public_url: Optional[StrictStr] = None
    creator: Optional[UserSummarySchema1] = None
    created_at: Optional[datetime] = None
    is_published: Optional[StrictBool] = None
    is_nsfw: Optional[StrictBool] = None
    is_purchased: Optional[StrictBool] = None
    is_private: Optional[StrictBool] = None
    collect_count: Optional[StrictInt] = None
    comment_count: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "name", "thumbnail", "url", "public_url", "creator", "created_at", "is_published", "is_nsfw", "is_purchased", "is_private", "collect_count", "comment_count"]

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
        """Create an instance of TopicSchemaCommentOfTopicThingsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # set to None if creator (nullable) is None
        # and model_fields_set contains the field
        if self.creator is None and "creator" in self.model_fields_set:
            _dict['creator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TopicSchemaCommentOfTopicThingsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "thumbnail": obj.get("thumbnail"),
            "url": obj.get("url"),
            "public_url": obj.get("public_url"),
            "creator": UserSummarySchema1.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "created_at": obj.get("created_at"),
            "is_published": obj.get("is_published"),
            "is_nsfw": obj.get("is_nsfw"),
            "is_purchased": obj.get("is_purchased"),
            "is_private": obj.get("is_private"),
            "collect_count": obj.get("collect_count"),
            "comment_count": obj.get("comment_count")
        })
        return _obj


