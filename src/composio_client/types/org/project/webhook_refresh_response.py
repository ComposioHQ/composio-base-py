# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["WebhookRefreshResponse"]


class WebhookRefreshResponse(BaseModel):
    message: str
    """Human-readable description of the refresh operation result"""

    success: bool
    """Indicates if the webhook secret was successfully refreshed"""

    webhook_secret: str
    """The new secret key that should be used to verify incoming webhook payloads"""
