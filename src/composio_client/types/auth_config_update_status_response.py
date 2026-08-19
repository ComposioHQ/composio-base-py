# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AuthConfigUpdateStatusResponse"]


class AuthConfigUpdateStatusResponse(BaseModel):
    message: str
    """A human-readable result message"""

    success: bool
    """Whether the status update succeeded"""
