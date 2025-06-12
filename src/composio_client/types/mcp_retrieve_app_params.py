# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["McpRetrieveAppParams"]


class McpRetrieveAppParams(TypedDict, total=False):
    auth_config_ids: Optional[List[str]]
    """Filter MCP servers by authentication configuration IDs"""

    limit: Optional[float]
    """Number of items per page (default: 10)"""

    name: str
    """Filter MCP servers by name (case-insensitive partial match)"""

    page_no: Optional[float]
    """Page number for pagination (1-based)"""

    toolkits: Optional[List[str]]
    """
    Filter MCP servers by toolkit slugs (returns servers matching any of the
    provided toolkits)
    """
