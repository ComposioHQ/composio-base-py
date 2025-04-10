# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TeamMemberListResponse", "Item"]


class Item(BaseModel):
    id: str

    created_at: str = FieldInfo(alias="createdAt")

    email: str

    name: str

    role: str

    updated_at: str = FieldInfo(alias="updatedAt")


class TeamMemberListResponse(BaseModel):
    items: List[Item]
