# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    tool_slug: str
    """Filter files by action slug. Example: "convert-to-pdf" """

    toolkit_slug: str
    """Filter files by app slug. Example: "file-converter" """
