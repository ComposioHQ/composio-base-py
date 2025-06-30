# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TriggerInstanceListActiveResponse", "Item", "ItemDeprecated"]


class ItemDeprecated(BaseModel):
    created_at: str = FieldInfo(alias="createdAt")
    """Deprecated created_at for the trigger instance"""


class Item(BaseModel):
    id: str
    """Nano ID of the trigger instance"""

    connected_account_id: str
    """ID of the connected account this trigger is associated with"""

    connected_account_uuid: str
    """UUID of the connected account this trigger is associated with"""

    disabled_at: Optional[str] = None
    """ISO 8601 timestamp when the trigger instance was disabled, if applicable"""

    disabled_at: Optional[str] = FieldInfo(alias="disabledAt", default=None)
    """ID of the user who disabled the trigger instance, if applicable"""

    state: Dict[str, Optional[object]]
    """State of the trigger instance"""

    trigger_config: Dict[str, Optional[object]]
    """Configuration for the trigger"""

    trigger_name: str
    """Name of the trigger"""

    updated_at: str
    """ISO 8601 timestamp when the trigger instance was updated"""

    user_id: str
    """ID of the user this trigger is associated with"""

    deprecated: Optional[ItemDeprecated] = None
    """Deprecated fields for the trigger instance"""

    trigger_data: Optional[str] = None
    """Additional data associated with the trigger instance"""

    uuid: Optional[str] = None
    """Unique identifier of the trigger instance"""


class TriggerInstanceListActiveResponse(BaseModel):
    current_page: float

    items: List[Item]

    total_items: float

    total_pages: float

    next_cursor: Optional[str] = None
