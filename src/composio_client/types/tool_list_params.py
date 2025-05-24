# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for fetching next page of results (base64 encoded)"""

    important: Literal["true", "false"]
    """Filter to only show important/featured tools (set to "true" to enable)"""

    limit: str
    """Maximum number of tools to return per page (defaults to 20, max 100)"""

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
