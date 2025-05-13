# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    cursor: str
    """The cursor to paginate through the results"""

    important: str
    """Whether to filter by important tools"""

    limit: str
    """The number of results to return"""

    search: str
    """The search query to filter by"""

    tags: Optional[List[str]]
    """The tags to filter the tools by"""

    tool_slugs: str
    """The slugs of the tools to filter by"""

    toolkit_slug: str
    """The slug of the toolkit to filter by"""
