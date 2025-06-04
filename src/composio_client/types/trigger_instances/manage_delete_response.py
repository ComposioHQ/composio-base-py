# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ManageDeleteResponse"]


class ManageDeleteResponse(BaseModel):
    trigger_id: str
    """The ID of the deleted trigger instance"""
