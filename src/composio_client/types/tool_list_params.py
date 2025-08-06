# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    auth_config_ids: Optional[List[str]]
    """Filter tools by auth config id"""

    cursor: str
    """Cursor for pagination.

    The cursor is a base64 encoded string of the page and limit. The page is the
    page number and the limit is the number of items per page. The cursor is used to
    paginate through the items. The cursor is not required for the first page.
    """

    important: Literal["true", "false"]
    """Filter to only show important/featured tools (set to "true" to enable)"""

    limit: Optional[float]
    """Number of items per page"""

    scopes: Optional[List[str]]
    """Array of scopes to filter tools by)"""

    search: str
    """Free-text search query to find tools by name, description, or functionality"""

    tags: List[str]
    """Filter tools by one or more tags (can be specified multiple times)"""

    tool_slugs: str
    """
    Comma-separated list of specific tool slugs to retrieve (overrides other
    filters)
    """

    toolkit_slug: str
    """The slug of the toolkit to filter by"""
