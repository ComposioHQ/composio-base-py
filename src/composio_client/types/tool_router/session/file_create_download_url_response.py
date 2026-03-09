# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["FileCreateDownloadURLResponse"]


class FileCreateDownloadURLResponse(BaseModel):
    download_url: str
    """Presigned download URL for the file"""

    expires_at: str
    """ISO 8601 timestamp when the download URL expires"""

    mount_relative_path: str
    """Relative file path within the mount (e.g. "report.pdf")"""

    sandbox_mount_prefix: str
    """Absolute mount path inside the sandbox (e.g. /mnt/files)"""
