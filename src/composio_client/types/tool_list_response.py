# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolListResponse", "Item", "ItemDepracated", "ItemDepracatedToolkit", "ItemToolkit"]


class ItemDepracatedToolkit(BaseModel):
    logo: str
    """The logo of the toolkit"""


class ItemDepracated(BaseModel):
    available_versions: List[str]
    """The available versions of the tool"""

    display_name: str = FieldInfo(alias="displayName")
    """The display name of the tool"""

    toolkit: ItemDepracatedToolkit

    version: str
    """The version of the tool"""


class ItemToolkit(BaseModel):
    name: str
    """The name of the toolkit"""

    slug: str
    """The slug of the toolkit"""


class Item(BaseModel):
    depracated: ItemDepracated

    description: str
    """The description of the tool"""

    input_parameters: Dict[str, Optional[object]]
    """The input parameters of the tool"""

    name: str
    """The name of the tool"""

    no_auth: bool
    """Whether the tool requires authentication"""

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
