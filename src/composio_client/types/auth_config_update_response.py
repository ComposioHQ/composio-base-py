# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AuthConfigUpdateResponse"]


class AuthConfigUpdateResponse(BaseModel):
    message: str
    """A human-readable result message"""

    success: bool
    """Whether the auth config was updated"""
