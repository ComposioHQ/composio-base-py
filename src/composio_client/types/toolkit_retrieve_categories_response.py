# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ToolkitRetrieveCategoriesResponse", "Item"]


class Item(BaseModel):
    id: str
    """URL-friendly unique identifier for the category, used for filtering toolkits"""

    name: str
    """Display name of the toolkit category"""


class ToolkitRetrieveCategoriesResponse(BaseModel):
    current_page: float

    items: List[Item]

    total_items: float

    total_pages: float

    next_cursor: Optional[str] = None
