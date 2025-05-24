# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["APIKeyCreateAPIKeyResponse"]


class APIKeyCreateAPIKeyResponse(BaseModel):
    id: str
    """Database record identifier for the API key"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """UTC timestamp indicating when the API key was created"""

    key: str
    """The API key string value that should be included in API requests.

    This value is only shown once.
    """

    name: str
    """Name assigned to help identify the key's purpose.

    For auto-generated keys, this will be a random name.
    """

    last_used: Optional[datetime] = FieldInfo(alias="lastUsed", default=None)
    """UTC timestamp indicating when the API key was last used for authentication.

    Will be null for newly created keys.
    """
