# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TriggerInstanceUpsertResponse"]


class TriggerInstanceUpsertResponse(BaseModel):
    trigger_id: str = FieldInfo(alias="triggerId")
    """ID of the updated trigger"""
