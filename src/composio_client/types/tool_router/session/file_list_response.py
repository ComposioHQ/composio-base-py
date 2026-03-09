# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["FileListResponse", "Item"]


class Item(BaseModel):
    last_modified: str
    """ISO 8601 timestamp of last modification"""

    mount_relative_path: str
    """Relative file path within the mount (e.g. "report.pdf")"""

    sandbox_mount_prefix: str
    """Absolute mount path inside the sandbox (e.g. /mnt/files)"""

    size: float
    """File size in bytes"""


class FileListResponse(BaseModel):
    items: List[Item]
    """List of files in the mount"""

    next_cursor: Optional[str] = None
    """Cursor for the next page of results. If absent, there are no more pages."""
