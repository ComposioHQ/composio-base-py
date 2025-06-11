# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["McpListParams"]


class McpListParams(TypedDict, total=False):
    auth_config_id: str
    """Filter MCP servers by authentication configuration ID"""

    limit: Optional[float]
    """Number of items per page (default: 10)"""

    name: str
    """Filter MCP servers by name (case-insensitive partial match)"""

    page_no: Optional[float]
    """Page number for pagination (1-based)"""

    toolkit: str
    """Filter MCP servers by toolkit slug"""
