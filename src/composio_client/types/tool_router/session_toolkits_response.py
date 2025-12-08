# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SessionToolkitsResponse", "Item", "ItemConnectedAccount", "ItemConnectedAccountAuthConfig", "ItemMeta"]


class ItemConnectedAccountAuthConfig(BaseModel):
    """Auth config details"""

    id: str
    """Auth config identifier"""

    auth_scheme: str
    """Authentication scheme type"""

    is_composio_managed: bool
    """Whether this is a Composio-managed auth config"""


class ItemConnectedAccount(BaseModel):
    """Connected account if available"""

    id: str
    """Connected account identifier"""

    auth_config: ItemConnectedAccountAuthConfig
    """Auth config details"""

    created_at: datetime
    """Creation timestamp"""

    status: str
    """Connection status"""

    user_id: str
    """User identifier"""


class ItemMeta(BaseModel):
    """Toolkit metadata"""

    description: str
    """Description of the toolkit"""

    logo: str
    """URL to the toolkit logo"""


class Item(BaseModel):
    composio_managed_auth_schemes: List[str]
    """Available Composio-managed auth schemes"""

    connected_account: Optional[ItemConnectedAccount] = None
    """Connected account if available"""

    enabled: bool
    """Whether the toolkit is enabled"""

    is_no_auth: bool
    """Whether the toolkit is no-auth"""

    meta: ItemMeta
    """Toolkit metadata"""

    name: str
    """Display name of the toolkit"""

    slug: str
    """Unique slug identifier"""


class SessionToolkitsResponse(BaseModel):
    current_page: float

    items: List[Item]

    total_items: float

    total_pages: float

    next_cursor: Optional[str] = None
