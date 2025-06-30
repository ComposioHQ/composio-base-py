# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination.

    The cursor is a base64 encoded string of the page and limit. The page is the
    page number and the limit is the number of items per page. The cursor is used to
    paginate through the items. The cursor is not required for the first page.
    """

    limit: Optional[float]
    """Number of items per page"""

    tool_slug: str
    """Filter files by action slug. Example: "convert-to-pdf" """

    toolkit_slug: str
    """Filter files by app slug. Example: "file-converter" """
