# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FileCreatePresignedURLResponse", "UnionMember0", "UnionMember1", "UnionMember2"]


class UnionMember0(BaseModel):
    id: str
    """ID of the file"""

    existing_url: str = FieldInfo(alias="existingUrl")
    """URL of the existing file"""

    key: str
    """S3 upload location"""

    type: Literal["existing"]


class UnionMember1(BaseModel):
    id: str
    """ID of the file"""

    key: str
    """S3 upload location"""

    new_presigned_url: str = FieldInfo(alias="newPresignedUrl")
    """Presigned URL for upload"""

    type: Literal["new"]


class UnionMember2(BaseModel):
    id: str
    """ID of the file"""

    key: str
    """S3 upload location"""

    type: Literal["update"]

    update_presigned_url: str = FieldInfo(alias="updatePresignedUrl")
    """Presigned URL for upload"""


FileCreatePresignedURLResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2]
