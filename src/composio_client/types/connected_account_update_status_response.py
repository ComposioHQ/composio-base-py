# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ConnectedAccountUpdateStatusResponse"]


class ConnectedAccountUpdateStatusResponse(BaseModel):
    success: bool
    """Indicates whether the connected account status was successfully updated"""
