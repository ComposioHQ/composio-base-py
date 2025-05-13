# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["McpUpdateParams"]


class McpUpdateParams(TypedDict, total=False):
    actions: List[str]
    """Actions available for the server"""

    apps: List[str]
    """App IDs associated with the server"""

    name: str
    """Name of the MCP server"""
