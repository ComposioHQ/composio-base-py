# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["APIKeyListResponse", "Item"]


class Item(BaseModel):
    id: str
    """Unique identifier for the API key record"""

    created_at: datetime
    """UTC timestamp indicating when the API key was created"""

    key: str
    """The API key string that should be included in API requests for authentication"""

    name: str
    """Descriptive name assigned to the API key for identification purposes"""

    last_used: Optional[datetime] = None
    """UTC timestamp indicating when the API key was last used for authentication.

    Will be null if the key has never been used.
    """


class APIKeyListResponse(BaseModel):
    items: List[Item]
    """
    List of all API keys for the specified project, including their properties and
    usage information
    """
