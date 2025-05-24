# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["APIKeyDeleteResponse"]


class APIKeyDeleteResponse(BaseModel):
    message: str
    """Status message providing details about the deletion operation"""

    success: bool
    """Boolean flag indicating if the deletion operation was successful"""
