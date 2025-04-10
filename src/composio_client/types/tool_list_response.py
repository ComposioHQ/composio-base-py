# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ToolListResponse", "Item", "ItemToolkit"]


class ItemToolkit(BaseModel):
    name: str
    """The name of the toolkit"""

    slug: str
    """The slug of the toolkit"""


class Item(BaseModel):
    description: str
    """The description of the tool"""

    input_parameters: Dict[str, Optional[object]]
    """The input parameters of the tool"""

    name: str
    """The name of the tool"""

    output_parameters: Dict[str, Optional[object]]
    """The output parameters of the tool"""

    slug: str
    """The slug of the tool"""

    tags: List[str]
    """The tags of the tool"""

    toolkit: ItemToolkit


class ToolListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = None

    total_pages: float
