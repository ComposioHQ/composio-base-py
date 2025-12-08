# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ConnectedAccountDeleteResponse"]


class ConnectedAccountDeleteResponse(BaseModel):
    """Response returned after successfully deleting a connected account"""

    success: bool
    """Indicates whether the connected account was successfully deleted"""
