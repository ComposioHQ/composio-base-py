# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["McpUpdateParams"]


class McpUpdateParams(TypedDict, total=False):
    allowed_tools: SequenceNotStr[str]
    """List of action identifiers that should be enabled for this server"""

    auth_config_ids: SequenceNotStr[str]
    """List of auth config IDs to use for this MCP server."""

    managed_auth_via_composio: bool
    """Whether the MCP server is managed by Composio"""

    name: str
    """
    Human-readable name to identify this MCP server instance (4-30 characters,
    alphanumeric, spaces, and hyphens only)
    """

    toolkits: SequenceNotStr[str]
    """List of toolkit slugs this server should be configured to work with."""
