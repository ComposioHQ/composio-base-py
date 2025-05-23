# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["McpUpdateParams"]


class McpUpdateParams(TypedDict, total=False):
    actions: List[str]
    """List of action identifiers that should be enabled for this server"""

    apps: List[str]
    """List of application identifiers this server should be configured to work with"""

    name: str
    """
    Human-readable name to identify this MCP server instance (4-25 characters,
    alphanumeric and hyphens only)
    """
