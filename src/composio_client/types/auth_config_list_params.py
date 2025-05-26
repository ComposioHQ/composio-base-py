# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypedDict

__all__ = ["AuthConfigListParams"]


class AuthConfigListParams(TypedDict, total=False):
    cursor: str
    """The cursor to paginate through the auth configs"""

    deprecated_app_id: str
    """The app id to filter by"""

    deprecated_status: str

    is_composio_managed: Union[str, bool]
    """Whether to filter by composio managed auth configs"""

    limit: Optional[float]
    """The number of auth configs to return"""

    show_disabled: bool
    """Show disabled auth configs"""

    toolkit_slug: str
    """The slug of the toolkit to filter by"""
