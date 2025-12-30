# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ToolProxyResponse", "BinaryData"]


class BinaryData(BaseModel):
    """Binary body response data. Present when the response is a binary file."""

    content_type: str
    """Content-Type of the binary data"""

    size: float
    """File size in bytes"""

    url: str
    """URL to download binary content"""

    expires_at: Optional[str] = None
    """ISO 8601 timestamp when the URL expires"""


class ToolProxyResponse(BaseModel):
    status: float
    """The HTTP status code returned from the proxied API"""

    binary_data: Optional[BinaryData] = None
    """Binary body response data. Present when the response is a binary file."""

    data: Optional[object] = None
    """The response data returned from the proxied API"""

    headers: Optional[Dict[str, str]] = None
    """The HTTP headers returned from the proxied API"""
