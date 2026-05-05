# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionToolsParams"]


class SessionToolsParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination.

    The cursor is a base64 encoded string of the page and limit. The page is the
    page number and the limit is the number of items per page. The cursor is used to
    paginate through the items. The cursor is not required for the first page.
    """

    limit: int
    """Number of items per page, max allowed is 500"""
