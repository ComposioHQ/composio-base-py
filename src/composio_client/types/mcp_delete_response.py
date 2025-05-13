# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["McpDeleteResponse"]


class McpDeleteResponse(BaseModel):
    success: bool
    """Operation success status"""
