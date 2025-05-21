# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ProjectListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier for the project"""

    created_at: str
    """ISO timestamp when the project was created"""

    deleted: bool
    """Whether this project has been soft-deleted"""

    email: str
    """Email address associated with the project"""

    event_webhook_url: Optional[str] = None
    """URL where event webhook notifications will be sent (can be null)"""

    name: str
    """Name of the project"""

    org_id: str
    """Identifier of the organization that owns this project"""

    updated_at: str
    """ISO timestamp when the project was last updated"""

    webhook_secret: Optional[str] = None
    """Secret key used to sign webhook payloads for verification"""

    webhook_url: Optional[str] = None
    """URL where webhook events will be sent (can be null)"""

    is_new_webhook: Optional[bool] = None
    """Indicates if the webhook configuration is using the new format"""

    last_subscribed_at: Optional[datetime] = None
    """ISO timestamp when the project last subscribed to updates"""

    triggers_enabled: Optional[bool] = None
    """Whether triggers are enabled for this project"""


class ProjectListResponse(BaseModel):
    data: List[Data]
    """Array of projects belonging to the organization"""
