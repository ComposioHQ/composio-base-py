# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TriggerInstanceDeleteResponse"]


class TriggerInstanceDeleteResponse(BaseModel):
    trigger_id: str = FieldInfo(alias="triggerId")
    """The ID of the deleted trigger instance"""
