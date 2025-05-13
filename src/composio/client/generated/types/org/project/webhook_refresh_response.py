# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["WebhookRefreshResponse"]


class WebhookRefreshResponse(BaseModel):
    message: str
    """Status message"""

    success: bool
    """Whether the operation was successful"""

    webhook_secret: str
    """Webhook secret"""
