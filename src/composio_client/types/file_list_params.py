# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    tool_slug: str
    """Name of the action where this file belongs to."""

    toolkit_slug: str
    """Slug of the app where this file belongs to."""
