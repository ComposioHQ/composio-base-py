# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    session_id: Required[str]
    """The unique identifier of the tool router session"""

    cursor: str
    """Pagination cursor from the previous response next_cursor field"""

    limit: float
    """Maximum number of files to return per page (1-500)"""

    mount_relative_prefix: str
    """Relative path prefix within the mount for filtering"""
