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
    items: List[Item]

    next_cursor: Optional[str] = None

    total_pages: float
