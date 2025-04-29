# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileCreatePresignedURLParams"]


class FileCreatePresignedURLParams(TypedDict, total=False):
    action: Required[str]
    """Name of the action where this file belongs to."""

    app: Required[str]
    """Name of the app where this file belongs to."""

    filename: Required[str]
    """Name of the original file."""

    md5: Required[str]
    """MD5 of a file."""

    mimetype: Required[str]
    """Mime type of the original file."""
