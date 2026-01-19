# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FileCreatePresignedURLResponse",
    "UnionMember0",
    "UnionMember0Metadata",
    "UnionMember1",
    "UnionMember1Metadata",
    "UnionMember2",
    "UnionMember2Metadata",
]


class UnionMember0Metadata(BaseModel):
    storage_backend: Literal["s3", "azure_blob_storage"]
    """Storage backend used for the file.

    If this is azure, use `x-ms-blob-type` header to set the blob type to
    `BlockBlob` while uploading the file
    """


class UnionMember0(BaseModel):
    id: str
    """ID of the request file. Example: "req_file_7kXm2pL9qNvR" """

    existing_url: str
    """URL of the existing request file.

    Example:
    "https://storage.composio.dev/projects/prj_abc123/requests/gmail/attachment_7kXm2p.pdf"
    """

    existing_url: str = FieldInfo(alias="existingUrl")
    """[DEPRECATED] Use existing_url instead.

    URL of the existing request file. Example:
    "https://storage.composio.dev/projects/prj_abc123/requests/gmail/attachment_7kXm2p.pdf"
    """

    key: str
    """S3 upload location.

    Example:
    "projects/prj_abc123/requests/gmail/GMAIL_SEND_EMAIL/attachment_7kXm2p.pdf"
    """

    metadata: UnionMember0Metadata

    type: Literal["existing"]
    """Indicates the file already exists and does not need to be uploaded again"""


class UnionMember1Metadata(BaseModel):
    storage_backend: Literal["s3", "azure_blob_storage"]
    """Storage backend used for the file.

    If this is azure, use `x-ms-blob-type` header to set the blob type to
    `BlockBlob` while uploading the file
    """


class UnionMember1(BaseModel):
    id: str
    """ID of the request file. Example: "req_file_9mZn4qR8sXwT" """

    key: str
    """S3 upload location.

    Example:
    "projects/prj_xyz789/requests/slack/SLACK_UPLOAD_FILE/document_9mZn4q.docx"
    """

    metadata: UnionMember1Metadata

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
    """Indicates this is a new file that needs to be uploaded"""


class UnionMember2Metadata(BaseModel):
    storage_backend: Literal["s3", "azure_blob_storage"]
    """Storage backend used for the file.

    If this is azure, use `x-ms-blob-type` header to set the blob type to
    `BlockBlob` while uploading the file
    """


class UnionMember2(BaseModel):
    id: str
    """ID of the request file. Example: "req_file_3bKp6vN1hYjS" """

    key: str
    """S3 upload location.

    Example:
    "projects/prj_def456/requests/github/GITHUB_CREATE_ISSUE/screenshot_3bKp6v.png"
    """

    metadata: UnionMember2Metadata

    type: Literal["update"]
    """Indicates this file exists but needs to be updated with a new version"""

    update_presigned_url: str
    """Presigned URL for upload.

    Example:
    "https://storage.composio.dev/projects/prj_def456/requests/github/screenshot_3bKp6v.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=3600..."
    """

    update_presigned_url: str = FieldInfo(alias="updatePresignedUrl")
    """[DEPRECATED] Use update_presigned_url instead.

    Presigned URL for upload. Example:
    "https://storage.composio.dev/projects/prj_def456/requests/github/screenshot_3bKp6v.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=3600..."
    """


FileCreatePresignedURLResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2]
