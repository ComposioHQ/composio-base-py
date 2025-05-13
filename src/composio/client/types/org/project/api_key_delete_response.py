# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["APIKeyDeleteResponse"]


class APIKeyDeleteResponse(BaseModel):
    message: str
    """Status message"""

    success: bool
    """Whether the operation was successful"""
