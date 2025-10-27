# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["TriggersTypeListParams"]


class TriggersTypeListParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination.

    The cursor is a base64 encoded string of the page and limit. The page is the
    page number and the limit is the number of items per page. The cursor is used to
    paginate through the items. The cursor is not required for the first page.
    """

    limit: Optional[float]
    """Number of items per page, max allowed is 1000"""

    toolkit_slugs: Optional[SequenceNotStr[str]]
    """Array of toolkit slugs to filter triggers by"""

    toolkit_versions: Union[str, Dict[str, str]]
    """Toolkit version specification.

    Use "latest" for latest versions or bracket notation for specific versions per
    toolkit.
    """
