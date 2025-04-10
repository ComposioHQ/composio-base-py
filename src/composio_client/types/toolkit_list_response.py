# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ToolkitListResponse", "Item", "ItemMeta", "ItemMetaCategory"]


class ItemMetaCategory(BaseModel):
    id: str

    name: str


class ItemMeta(BaseModel):
    categories: List[ItemMetaCategory]

    created_at: str

    description: str

    logo: str

    tools_count: float

    triggers_count: float

    updated_at: str


class Item(BaseModel):
    is_local_toolkit: bool

    meta: ItemMeta

    name: str

    slug: str

    auth_schemes: Optional[List[str]] = None

    composio_managed_auth_schemes: Optional[List[str]] = None

    no_auth: Optional[bool] = None


class ToolkitListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = None

    total_pages: float
