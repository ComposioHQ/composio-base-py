# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolListResponse", "Item", "ItemDeprecated", "ItemDeprecatedToolkit", "ItemToolkit"]


class ItemDeprecatedToolkit(BaseModel):
    logo: str
    """URL to the toolkit logo image"""


class ItemDeprecated(BaseModel):
    available_versions: List[str]
    """List of all available versions for this tool"""

    display_name: str = FieldInfo(alias="displayName")
    """The display name of the tool"""

    is_deprecated: bool
    """Indicates if this tool is deprecated and may be removed in the future"""

    toolkit: ItemDeprecatedToolkit

    version: str
    """Current version identifier of the tool"""


class ItemToolkit(BaseModel):
    logo: str
    """URL to the toolkit logo image"""

    name: str
    """Human-readable name of the parent toolkit"""

    slug: str
    """Unique identifier of the parent toolkit"""


class Item(BaseModel):
    available_versions: List[str]
    """List of all available versions for this tool"""

    deprecated: ItemDeprecated

    description: str
    """Detailed explanation of the tool's functionality and purpose"""

    input_parameters: Dict[str, Optional[object]]
    """Schema definition of required input parameters for the tool"""

    name: str
    """Human-readable display name of the tool"""

    no_auth: bool
    """Indicates if the tool can be used without authentication"""

    output_parameters: Dict[str, Optional[object]]
    """Schema definition of return values from the tool"""

    scopes: List[str]
    """List of scopes associated with the tool"""

    slug: str
    """Unique identifier for the tool"""

    tags: List[str]
    """List of tags associated with the tool for categorization and filtering"""

    toolkit: ItemToolkit

    version: str
    """Current version of the tool"""


class ToolListResponse(BaseModel):
    current_page: float

    items: List[Item]

    total_items: float

    total_pages: float

    next_cursor: Optional[str] = None
