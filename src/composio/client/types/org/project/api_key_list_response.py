# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["APIKeyListResponse", "Item"]


class Item(BaseModel):
    id: str
    """API key ID"""

    created_at: datetime
    """Creation timestamp"""

    key: str
    """API key value"""

    name: str
    """API key name"""

    last_used: Optional[datetime] = None
    """Last used timestamp"""


class APIKeyListResponse(BaseModel):
    items: List[Item]
    """List of API keys"""
