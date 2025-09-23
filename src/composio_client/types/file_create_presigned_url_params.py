# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileCreatePresignedURLParams"]


class FileCreatePresignedURLParams(TypedDict, total=False):
    filename: Required[str]
    """Name of the original file. Example: "photo.jpg" """

    md5: Required[str]
    """MD5 hash of the file for deduplication and integrity verification.

    Example: "d41d8cd98f00b204e9800998ecf8427e"
    """

    mimetype: Required[str]
    """Mime type of the original file. Example: "image/jpeg" """

    tool_slug: Required[str]
    """Slug of the action where this file belongs to. Example: "resize-image" """

    toolkit_slug: Required[str]
    """Slug of the app where this file belongs to. Example: "image-processing" """
