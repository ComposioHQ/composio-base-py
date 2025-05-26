# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ConnectedAccountDeleteResponse"]


class ConnectedAccountDeleteResponse(BaseModel):
    success: bool
    """Indicates whether the connected account was successfully deleted"""
