# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["FileDeleteResponse"]


class FileDeleteResponse(BaseModel):
    mount_relative_path: str
    """Relative file path that was deleted"""

    sandbox_mount_prefix: str
    """Absolute mount path inside the sandbox (e.g. /mnt/files)"""
