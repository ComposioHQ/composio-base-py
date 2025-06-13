# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["GenerateURLResponse"]


class GenerateURLResponse(BaseModel):
    connected_account_urls: List[str]
    """List of URLs generated for each connected account ID"""

    mcp_url: str
    """Base MCP URL without any query parameters"""

    user_ids_url: List[str]
    """List of URLs generated for each user ID"""
