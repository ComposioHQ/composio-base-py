# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["GenerateURLParams"]


class GenerateURLParams(TypedDict, total=False):
    mcp_server_id: Required[str]
    """Unique identifier of the MCP server to generate URL for"""

    connected_account_ids: List[str]
    """List of connected account identifiers"""

    managed_auth_by_composio: bool
    """Flag indicating if Composio manages authentication"""

    user_ids: List[str]
    """List of user identifiers for whom the URL is generated"""
