# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ProjectCreateResponse"]


class ProjectCreateResponse(BaseModel):
    id: str

    auto_id: float

    created_at: str

    deleted: bool

    email: str

    event_webhook_url: Optional[str] = None

    name: str

    org_id: str

    updated_at: str

    webhook_secret: Optional[str] = None

    webhook_url: Optional[str] = None

    is_new_webhook: Optional[bool] = None

    last_subscribed_at: Optional[datetime] = None

    triggers_enabled: Optional[bool] = None
