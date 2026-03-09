# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileCreateDownloadURLParams"]


class FileCreateDownloadURLParams(TypedDict, total=False):
    session_id: Required[str]
    """The unique identifier of the tool router session"""

    mount_relative_path: Required[str]
    """Relative file path within the mount"""
