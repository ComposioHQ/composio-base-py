# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileCreateUploadURLParams"]


class FileCreateUploadURLParams(TypedDict, total=False):
    session_id: Required[str]
    """The unique identifier of the tool router session"""

    mount_relative_path: Required[str]
    """Supports subdirectories (e.g. "data/output.csv", "images/charts/chart.png")"""

    mimetype: str
    """MIME type of the file being uploaded"""
