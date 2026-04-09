# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ConnectedAccountPatchResponse"]


class ConnectedAccountPatchResponse(BaseModel):
    id: str
    """The unique identifier of the updated connected account"""

    status: str
    """
    The current status of the connected account after the update (ACTIVE, EXPIRED,
    INACTIVE, etc.)
    """

    success: bool
    """Whether the update was successful"""
