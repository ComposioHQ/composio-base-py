# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["SessionToolkitsParams"]


class SessionToolkitsParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination.

    The cursor is a base64 encoded string of the page and limit. The page is the
    page number and the limit is the number of items per page. The cursor is used to
    paginate through the items. The cursor is not required for the first page.
    """

    is_connected: Optional[bool]
    """Whether to filter by connected toolkits.

    If provided, only connected toolkits will be returned.
    """

    limit: Optional[float]
    """Number of items per page, max allowed is 1000"""

    search: str
    """Search query to filter toolkits by name, slug, or description"""

    toolkits: Optional[SequenceNotStr[str]]
    """Optional comma-separated list of toolkit slugs to filter by.

    If provided, only these toolkits will be returned, overriding the session
    configuration.
    """
