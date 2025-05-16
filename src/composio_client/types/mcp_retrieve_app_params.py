# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["McpRetrieveAppParams"]


class McpRetrieveAppParams(TypedDict, total=False):
    auth_config_id: str
    """Auth configuration ID to filter by"""

    limit: Optional[float]
    """Number of items per page"""

    name: str
    """Name of the MCP server to filter by"""

    page_no: Optional[float]
    """Page number for pagination"""

    toolkit: str
    """Toolkit slug to filter by"""
