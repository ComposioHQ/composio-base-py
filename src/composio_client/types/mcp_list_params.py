# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["McpListParams"]


class McpListParams(TypedDict, total=False):
    auth_config_ids: str
    """Comma-separated list of auth config IDs to filter servers by"""

    limit: Optional[float]
    """Number of items per page (default: 10)"""

    name: str
    """Filter MCP servers by name (case-insensitive partial match)"""

    order_by: Literal["created_at", "updated_at"]
    """Field to order results by"""

    order_direction: Literal["asc", "desc"]
    """Direction of ordering"""

    page_no: Optional[float]
    """Page number for pagination (1-based)"""

    toolkits: str
    """Comma-separated list of toolkit slugs to filter servers by"""
