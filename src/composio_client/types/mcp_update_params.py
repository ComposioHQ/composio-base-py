# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["McpUpdateParams"]


class McpUpdateParams(TypedDict, total=False):
    allowed_tools: Optional[List[str]]
    """List of action identifiers that should be enabled for this server"""

    name: str
    """
    Human-readable name to identify this MCP server instance (4-25 characters,
    alphanumeric and hyphens only)
    """

    toolkits: Optional[List[str]]
    """List of toolkit slugs this server should be configured to work with"""
