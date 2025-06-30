# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolkitListResponse", "Item", "ItemDeprecated", "ItemMeta", "ItemMetaCategory"]


class ItemDeprecated(BaseModel):
    toolkit_id: str = FieldInfo(alias="toolkitId")


class ItemMetaCategory(BaseModel):
    id: str
    """Category identifier"""

    name: str
    """Human-readable category name"""


class ItemMeta(BaseModel):
    categories: List[ItemMetaCategory]
    """List of categories associated with this toolkit"""

    created_at: str
    """Creation date and time of the toolkit"""

    description: str
    """Human-readable description explaining the toolkit's purpose and functionality"""

    logo: str
    """Image URL for the toolkit's branding"""

    tools_count: float
    """Count of available tools in this toolkit"""

    triggers_count: float
    """Count of available triggers in this toolkit"""

    updated_at: str
    """Last modification date and time of the toolkit"""

    app_url: Optional[str] = None
    """Link to the toolkit's main application or service website"""


class Item(BaseModel):
    deprecated: ItemDeprecated
    """Deprecated toolkit ID"""

    is_local_toolkit: bool
    """
    Indicates if this toolkit is specific to the current project or globally
    available
    """

    meta: ItemMeta
    """Additional metadata about the toolkit"""

    name: str
    """Human-readable name of the toolkit"""

    slug: str
    """URL-friendly unique identifier for the toolkit"""

    auth_schemes: Optional[List[str]] = None
    """List of authentication methods supported by this toolkit"""

    composio_managed_auth_schemes: Optional[List[str]] = None
    """List of authentication methods that Composio manages for this toolkit"""

    no_auth: Optional[bool] = None
    """When true, this toolkit can be used without authentication"""


class ToolkitListResponse(BaseModel):
    current_page: float

    items: List[Item]

    total_items: float

    total_pages: float

    next_cursor: Optional[str] = None
