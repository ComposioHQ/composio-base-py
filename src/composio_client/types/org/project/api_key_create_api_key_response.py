# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["APIKeyCreateAPIKeyResponse"]


class APIKeyCreateAPIKeyResponse(BaseModel):
    id: str
    """Database record identifier for the API key"""

    created_at: datetime
    """UTC timestamp indicating when the API key was created"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """UTC timestamp indicating when the API key was created. Use created_at instead."""

    key: str
    """The API key string value that should be included in API requests.

    This value is only shown once.
    """

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")
    """UTC timestamp indicating when the API key was created.

    Use last_used_at instead.
    """

    name: str
    """Name assigned to help identify the key's purpose.

    For auto-generated keys, this will be a random name.
    """

    last_used_at: Optional[datetime] = None
    """UTC timestamp indicating when the API key was last used for authentication.

    Will be null for newly created keys.
    """
