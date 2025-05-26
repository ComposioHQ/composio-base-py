# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["McpCreateParams"]


class McpCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    Human-readable name to identify this MCP server instance (4-25 characters,
    alphanumeric and hyphens only)
    """

    allowed_tools: List[str]
    """List of tool slugs that should be allowed for this server.

    If not provided, all available tools for the authentication configuration will
    be enabled.
    """

    auth_config_id: str
    """ID reference to an existing authentication configuration"""

    ttl: Literal["1d", "3d", "1 month", "no expiration"]
    """Time-to-live duration for this MCP server"""
