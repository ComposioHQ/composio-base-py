# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AuthConfigListParams"]


class AuthConfigListParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination.

    The cursor is a base64 encoded string of the page and limit. The page is the
    page number and the limit is the number of items per page. The cursor is used to
    paginate through the items. The cursor is not required for the first page.
    """

    deprecated_app_id: str
    """The app id to filter by"""

    deprecated_status: str

    is_composio_managed: Union[str, bool]
    """Whether to filter by composio managed auth configs"""

    limit: Optional[float]
    """Number of items per page"""

    order_by: Literal["created_at", "updated_at", "no_of_connections"]
    """Field to order auth configs by"""

    order_direction: Literal["asc", "desc"]
    """Direction to order auth configs"""

    search: str
    """Search auth configs by name"""

    show_disabled: Optional[bool]
    """Show disabled auth configs"""

    toolkit_slug: str
    """The slug of the toolkit to filter by"""
