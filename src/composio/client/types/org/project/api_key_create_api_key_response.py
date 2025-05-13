# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["APIKeyCreateAPIKeyResponse"]


class APIKeyCreateAPIKeyResponse(BaseModel):
    id: str
    """API key ID"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation timestamp"""

    key: str
    """API key value"""

    name: str
    """API key name"""

    last_used: Optional[datetime] = FieldInfo(alias="lastUsed", default=None)
    """Last used timestamp"""
