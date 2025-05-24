# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ToolProxyResponse"]


class ToolProxyResponse(BaseModel):
    status: float
    """The HTTP status code returned from the proxied API"""

    data: Optional[object] = None
    """The response data returned from the proxied API"""

    headers: Optional[Dict[str, str]] = None
    """The HTTP headers returned from the proxied API"""
