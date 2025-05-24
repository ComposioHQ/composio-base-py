# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TriggersTypeListResponse", "Item", "ItemToolkit"]


class ItemToolkit(BaseModel):
    name: str
    """Name of the parent toolkit"""

    slug: str
    """Unique identifier for the parent toolkit"""


class Item(BaseModel):
    config: Dict[str, Optional[object]]
    """Configuration schema required to set up this trigger"""

    description: str
    """Detailed description of what the trigger does"""

    name: str
    """Human-readable name of the trigger"""

    payload: Dict[str, Optional[object]]
    """Schema of the data payload this trigger will deliver when it fires"""

    slug: str
    """Unique identifier for the trigger type"""

    toolkit: ItemToolkit
    """Information about the toolkit that provides this trigger"""

    type: Literal["webhook", "poll"]
    """The trigger mechanism - either webhook (event-based) or poll (scheduled check)"""


class TriggersTypeListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = None

    total_pages: float
