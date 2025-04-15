# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["McpListParams"]


class McpListParams(TypedDict, total=False):
    app_id: List[str]
    """App IDs to filter by"""

    connected_account_id: List[str]
    """Connected account IDs to filter by"""

    cursor: Optional[float]
    """Cursor for pagination"""

    entity_id: List[str]
    """Entity IDs to filter by"""

    integration_id: str
    """Integration ID to filter by"""

    limit: Optional[float]
    """Limit for pagination"""
