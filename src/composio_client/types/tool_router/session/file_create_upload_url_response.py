# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["FileCreateUploadURLResponse"]


class FileCreateUploadURLResponse(BaseModel):
    expires_at: str
    """ISO 8601 timestamp when the upload URL expires"""

    mount_relative_path: str
    """Relative file path within the mount (e.g. "report.pdf")"""

    sandbox_mount_prefix: str
    """Absolute mount path inside the sandbox (e.g. /mnt/files)"""

    upload_url: str
    """Presigned upload URL — PUT the file content here"""
