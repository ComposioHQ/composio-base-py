# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TriggerInstanceUpsertResponse", "Deprecated"]


class Deprecated(BaseModel):
    uuid: str
    """ID of the updated trigger"""


class TriggerInstanceUpsertResponse(BaseModel):
    deprecated: Deprecated

    trigger_id: str
    """ID of the updated trigger"""
