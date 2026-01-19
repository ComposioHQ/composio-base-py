# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileCreatePresignedURLParams"]


class FileCreatePresignedURLParams(TypedDict, total=False):
    filename: Required[str]
    """Name of the original file. Example: "quarterly_report.pdf" """

    md5: Required[str]
    """MD5 hash of the file for deduplication and integrity verification.

    Example: "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6"
    """

    mimetype: Required[str]
    """Mime type of the original file. Example: "application/pdf", "image/png" """

    tool_slug: Required[str]
    """Slug of the action where this file belongs to.

    Example: "GMAIL_SEND_EMAIL", "SLACK_UPLOAD_FILE"
    """

    toolkit_slug: Required[str]
    """Slug of the app where this file belongs to. Example: "gmail", "slack", "github" """
