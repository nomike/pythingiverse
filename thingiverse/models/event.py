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
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thingiverse.models.event_sources_inner import EventSourcesInner
from thingiverse.models.event_subscription import EventSubscription
from thingiverse.models.event_targets_inner import EventTargetsInner
from typing import Optional, Set
from typing_extensions import Self

class Event(BaseModel):
    """
    Event
    """ # noqa: E501
    id: Optional[StrictInt] = None
    type: Optional[StrictInt] = None
    message: Optional[StrictStr] = None
    time: Optional[datetime] = None
    targets: Optional[List[EventTargetsInner]] = None
    sources: Optional[List[EventSourcesInner]] = None
    subscription: Optional[EventSubscription] = None
    __properties: ClassVar[List[str]] = ["id", "type", "message", "time", "targets", "sources", "subscription"]

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
        """Create an instance of Event from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in targets (list)
        _items = []
        if self.targets:
            for _item_targets in self.targets:
                if _item_targets:
                    _items.append(_item_targets.to_dict())
            _dict['targets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sources (list)
        _items = []
        if self.sources:
            for _item_sources in self.sources:
                if _item_sources:
                    _items.append(_item_sources.to_dict())
            _dict['sources'] = _items
        # override the default output from pydantic by calling `to_dict()` of subscription
        if self.subscription:
            _dict['subscription'] = self.subscription.to_dict()
        # set to None if subscription (nullable) is None
        # and model_fields_set contains the field
        if self.subscription is None and "subscription" in self.model_fields_set:
            _dict['subscription'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "message": obj.get("message"),
            "time": obj.get("time"),
            "targets": [EventTargetsInner.from_dict(_item) for _item in obj["targets"]] if obj.get("targets") is not None else None,
            "sources": [EventSourcesInner.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None,
            "subscription": EventSubscription.from_dict(obj["subscription"]) if obj.get("subscription") is not None else None
        })
        return _obj


