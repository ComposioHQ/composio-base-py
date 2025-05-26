# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["TeamMemberListResponse", "Item"]


class Item(BaseModel):
    id: str

    created_at: str

    email: str

    name: str

    role: str

    updated_at: str


class TeamMemberListResponse(BaseModel):
    items: List[Item]
