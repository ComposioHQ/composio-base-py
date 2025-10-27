# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    auth_config_ids: Union[str, SequenceNotStr[str]]
    """Comma-separated list of auth config IDs to filter tools by"""

    cursor: str
    """Cursor for pagination.

    The cursor is a base64 encoded string of the page and limit. The page is the
    page number and the limit is the number of items per page. The cursor is used to
    paginate through the items. The cursor is not required for the first page.
    """

    important: Literal["true", "false"]
    """Filter to only show important/featured tools (set to "true" to enable)"""

    include_deprecated: bool
    """Include deprecated tools in the response"""

    limit: Optional[float]
    """Number of items per page, max allowed is 1000"""

    scopes: Optional[SequenceNotStr[str]]
    """Array of scopes to filter tools by)"""

    search: str
    """Free-text search query to find tools by name, description, or functionality"""

    tags: SequenceNotStr[str]
    """Filter tools by one or more tags (can be specified multiple times)"""

    tool_slugs: str
    """
    Comma-separated list of specific tool slugs to retrieve (overrides other
    filters)
    """

    toolkit_slug: str
    """The slug of the toolkit to filter by"""

    toolkit_versions: Union[str, Dict[str, str]]
    """Toolkit version specification.

    Use "latest" for latest versions or bracket notation for specific versions per
    toolkit.
    """
