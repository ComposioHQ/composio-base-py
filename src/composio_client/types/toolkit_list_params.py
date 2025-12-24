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

    include_deprecated: Optional[bool]
    """Include deprecated toolkits in the response"""

    limit: Optional[float]
    """Number of items per page, max allowed is 1000"""

    managed_by: Literal["composio", "all", "project"]
    """Filter toolkits by who manages them"""

    search: str
    """Search query to filter toolkits by name, slug, or description"""

    sort_by: Literal["usage", "alphabetically"]
    """Sort order for returned toolkits"""
