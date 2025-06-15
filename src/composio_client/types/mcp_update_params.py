# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["McpUpdateParams"]


class McpUpdateParams(TypedDict, total=False):
    allowed_tools: List[str]
    """List of action identifiers that should be enabled for this server"""

    managed_auth_via_composio: bool
    """Whether the MCP server is managed by Composio"""

    name: str
    """
    Human-readable name to identify this MCP server instance (4-30 characters,
    alphanumeric, spaces, and hyphens only)
    """

    toolkits: List[str]
    """List of toolkit slugs this server should be configured to work with"""
