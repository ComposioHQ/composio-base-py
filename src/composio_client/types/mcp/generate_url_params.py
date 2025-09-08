# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["GenerateURLParams"]


class GenerateURLParams(TypedDict, total=False):
    mcp_server_id: Required[str]
    """Unique identifier of the MCP server to generate URL for"""

    connected_account_ids: SequenceNotStr[str]
    """List of connected account identifiers"""

    managed_auth_by_composio: bool
    """Flag indicating if Composio manages authentication"""

    user_ids: SequenceNotStr[str]
    """List of user identifiers for whom the URL is generated"""
