# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["FileListResponse", "Item"]


class Item(BaseModel):
    filename: str
    """Name of the original file. Example: "document.docx" """

    md5: str
    """MD5 hash of the file for integrity verification.

    Example: "d41d8cd98f00b204e9800998ecf8427e"
    """

    mimetype: str
    """Mime type of the original file.

    Example:
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    """

    tool_slug: str
    """Slug of the action where this file belongs to. Example: "convert-to-pdf" """

    toolkit_slug: str
    """Slug of the app where this file belongs to. Example: "file-converter" """


class FileListResponse(BaseModel):
    current_page: float

    items: List[Item]

    total_items: float

    total_pages: float

    next_cursor: Optional[str] = None
