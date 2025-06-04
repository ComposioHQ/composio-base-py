# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AdminRefreshAuthTokensResponse", "Failure"]


class Failure(BaseModel):
    connection_id: str = FieldInfo(alias="connectionId")
    """Connection ID that failed during refresh"""

    error: str
    """Specific error code identifying why the refresh operation failed"""


class AdminRefreshAuthTokensResponse(BaseModel):
    failures: List[Failure]
    """Array of connections that failed to refresh with detailed error information"""

    success: List[str]
    """List of connections where token refresh was successful or not needed"""
