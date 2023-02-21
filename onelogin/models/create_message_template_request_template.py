# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import json
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from onelogin.models.create_message_template_request_template_one_of import CreateMessageTemplateRequestTemplateOneOf
from onelogin.models.create_message_template_request_template_one_of1 import CreateMessageTemplateRequestTemplateOneOf1
from typing import Any, List
from pydantic import StrictStr, Field

CREATEMESSAGETEMPLATEREQUESTTEMPLATE_ONE_OF_SCHEMAS = ["CreateMessageTemplateRequestTemplateOneOf", "CreateMessageTemplateRequestTemplateOneOf1"]

class CreateMessageTemplateRequestTemplate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: CreateMessageTemplateRequestTemplateOneOf
    __oneof_schema_1: Optional[CreateMessageTemplateRequestTemplateOneOf] = None
    # data type: CreateMessageTemplateRequestTemplateOneOf1
    __oneof_schema_2: Optional[CreateMessageTemplateRequestTemplateOneOf1] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(CREATEMESSAGETEMPLATEREQUESTTEMPLATE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        error_messages = []
        match = 0
        # validate data type: CreateMessageTemplateRequestTemplateOneOf
        if type(v) is not CreateMessageTemplateRequestTemplateOneOf:
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateMessageTemplateRequestTemplateOneOf`")
        else:
            match += 1

        # validate data type: CreateMessageTemplateRequestTemplateOneOf1
        if type(v) is not CreateMessageTemplateRequestTemplateOneOf1:
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateMessageTemplateRequestTemplateOneOf1`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateMessageTemplateRequestTemplate with oneOf schemas: CreateMessageTemplateRequestTemplateOneOf, CreateMessageTemplateRequestTemplateOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateMessageTemplateRequestTemplate with oneOf schemas: CreateMessageTemplateRequestTemplateOneOf, CreateMessageTemplateRequestTemplateOneOf1. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> CreateMessageTemplateRequestTemplate:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> CreateMessageTemplateRequestTemplate:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into CreateMessageTemplateRequestTemplateOneOf
        try:
            instance.actual_instance = CreateMessageTemplateRequestTemplateOneOf.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into CreateMessageTemplateRequestTemplateOneOf1
        try:
            instance.actual_instance = CreateMessageTemplateRequestTemplateOneOf1.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateMessageTemplateRequestTemplate with oneOf schemas: CreateMessageTemplateRequestTemplateOneOf, CreateMessageTemplateRequestTemplateOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateMessageTemplateRequestTemplate with oneOf schemas: CreateMessageTemplateRequestTemplateOneOf, CreateMessageTemplateRequestTemplateOneOf1. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())




