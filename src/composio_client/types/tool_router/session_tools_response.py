# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["SessionToolsResponse", "Item", "ItemToolkit"]


class ItemToolkit(BaseModel):
    name: str
    """Name of the toolkit"""

    slug: str
    """Slug of the toolkit this tool belongs to"""


class Item(BaseModel):
    description: str
    """Description of what the tool does"""

    input_parameters: Dict[str, Optional[object]]
    """JSON Schema for the tool input parameters"""

    name: str
    """Human-readable name of the tool"""

    output_parameters: Dict[str, Optional[object]]
    """JSON Schema for the tool output parameters"""

    slug: str
    """Unique identifier for the tool"""

    tags: List[str]
    """Tags associated with the tool"""

    toolkit: ItemToolkit


class SessionToolsResponse(BaseModel):
    items: List[Item]
    """List of meta tools with their complete schemas"""
