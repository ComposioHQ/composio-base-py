# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["TriggersTypeListParams"]


class TriggersTypeListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for fetching next page of results"""

    limit: Optional[float]
    """Number of items to return per page"""

    toolkit_slugs: Optional[List[str]]
    """Array of toolkit slugs to filter triggers by"""
