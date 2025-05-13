# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TriggersTypeListResponse", "Item", "ItemToolkit"]


class ItemToolkit(BaseModel):
    name: str

    slug: str


class Item(BaseModel):
    config: Dict[str, Optional[object]]

    description: str

    name: str

    payload: Dict[str, Optional[object]]

    slug: str

    toolkit: ItemToolkit

    type: Literal["webhook", "poll"]


class TriggersTypeListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = None

    total_pages: float
