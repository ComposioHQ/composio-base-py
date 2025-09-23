# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FileCreatePresignedURLResponse", "UnionMember0", "UnionMember1", "UnionMember2"]


class UnionMember0(BaseModel):
    id: str
    """ID of the request file. Example: "f1e2d3c4b5a6" """

    existing_url: str
    """URL of the existing request file.

    Example: "https://storage.example.com/projects/123/files/photo-1234.jpg"
    """

    existing_url: str = FieldInfo(alias="existingUrl")
    """[DEPRECATED] Use existing_url instead.

    URL of the existing request file. Example:
    "https://storage.example.com/projects/123/files/photo-1234.jpg"
    """

    key: str
    """S3 upload location. Example: "projects/123/files/photo-1234.jpg" """

    type: Literal["existing"]
    """Indicates the file already exists and does not need to be uploaded again"""


class UnionMember1(BaseModel):
    id: str
    """ID of the request file. Example: "f1e2d3c4b5a6" """

    key: str
    """S3 upload location. Example: "projects/123/files/photo-1234.jpg" """

    new_presigned_url: str
    """Presigned URL for upload.

    Example:
    "https://storage.example.com/projects/123/files/photo-1234.jpg?X-Amz-Algorithm=..."
    """

    new_presigned_url: str = FieldInfo(alias="newPresignedUrl")
    """[DEPRECATED] Use new_presigned_url instead.

    Presigned URL for upload. Example:
    "https://storage.example.com/projects/123/files/photo-1234.jpg?X-Amz-Algorithm=..."
    """

    type: Literal["new"]
    """Indicates this is a new file that needs to be uploaded"""


class UnionMember2(BaseModel):
    id: str
    """ID of the request file. Example: "f1e2d3c4b5a6" """

    key: str
    """S3 upload location. Example: "projects/123/files/photo-1234.jpg" """

    type: Literal["update"]
    """Indicates this file exists but needs to be updated with a new version"""

    update_presigned_url: str
    """Presigned URL for upload.

    Example:
    "https://storage.example.com/projects/123/files/photo-1234.jpg?X-Amz-Algorithm=..."
    """

    update_presigned_url: str = FieldInfo(alias="updatePresignedUrl")
    """[DEPRECATED] Use update_presigned_url instead.

    Presigned URL for upload. Example:
    "https://storage.example.com/projects/123/files/photo-1234.jpg?X-Amz-Algorithm=..."
    """


FileCreatePresignedURLResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2]
