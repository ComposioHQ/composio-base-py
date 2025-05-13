# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["FileListResponse", "Item"]


class Item(BaseModel):
    filename: str
    """Name of the original file."""

    md5: str
    """MD5 of a file."""

    mimetype: str
    """Mime type of the original file."""

    tool_slug: str
    """Name of the action where this file belongs to."""

    toolkit_slug: str
    """Slug of the app where this file belongs to."""


class FileListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = None

    total_pages: float
