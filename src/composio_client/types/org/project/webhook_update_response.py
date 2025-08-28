# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["WebhookUpdateResponse"]


class WebhookUpdateResponse(BaseModel):
    message: str
    """Human-readable description of the update operation result"""

    success: bool
    """Indicates if the webhook URL update was completed successfully"""
