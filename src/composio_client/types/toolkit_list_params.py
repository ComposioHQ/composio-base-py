# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ToolkitListParams"]


class ToolkitListParams(TypedDict, total=False):
    category: str
    """Filter toolkits by category"""

    cursor: str
    """Cursor for pagination.

    The cursor is a base64 encoded string of the page and limit. The page is the
    page number and the limit is the number of items per page. The cursor is used to
    paginate through the items. The cursor is not required for the first page.
    """

    is_local: Optional[bool]
    """Whether to include local toolkits in the results"""

    limit: Optional[float]
    """Number of items per page"""

    managed_by: Literal["composio", "all", "project"]
    """Filter toolkits by who manages them"""

    sort_by: Literal["usage", "alphabetically"]
    """Sort order for returned toolkits"""
