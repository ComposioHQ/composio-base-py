# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FileCreatePresignedURLResponse", "Metadata"]


class Metadata(BaseModel):
    storage_backend: Literal["s3", "azure_blob_storage"]
    """Storage backend used for the file.

    If this is azure, use `x-ms-blob-type` header to set the blob type to
    `BlockBlob` while uploading the file
    """


class FileCreatePresignedURLResponse(BaseModel):
    id: str
    """ID of the request file. Example: "req_file_9mZn4qR8sXwT" """

    key: str
    """Object storage upload location.

    Example:
    "projects/prj_xyz789/requests/slack/SLACK_UPLOAD_FILE/document_9mZn4q.docx"
    """

    metadata: Metadata

    new_presigned_url: str
    """Presigned URL for upload.

    Example:
    "https://storage.composio.dev/projects/prj_xyz789/requests/slack/document_9mZn4q.docx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=3600..."
    """

    new_presigned_url: str = FieldInfo(alias="newPresignedUrl")
    """[DEPRECATED] Use new_presigned_url instead.

    Presigned URL for upload. Example:
    "https://storage.composio.dev/projects/prj_xyz789/requests/slack/document_9mZn4q.docx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=3600..."
    """

    type: Literal["new"]
    """[DEPRECATED] Indicates this is a new file that needs to be uploaded"""
