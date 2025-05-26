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

    disabled_at: Optional[str] = None
    """ISO 8601 timestamp when the trigger instance was disabled, if applicable"""

    state: Dict[str, Optional[object]]
    """State of the trigger instance"""

    trigger_config: Dict[str, Optional[object]]
    """Configuration for the trigger"""

    trigger_name: str
    """Name of the trigger"""

    updated_at: str
    """ISO 8601 timestamp when the trigger instance was updated"""

    deprecated: Optional[ItemDeprecated] = None
    """Deprecated fields for the trigger instance"""

    trigger_data: Optional[str] = None
    """Additional data associated with the trigger instance"""

    uuid: Optional[str] = None
    """Unique identifier of the trigger instance"""


class TriggerInstanceListActiveResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = None

    total_pages: float
