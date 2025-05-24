# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["WebhookDeleteResponse"]


class WebhookDeleteResponse(BaseModel):
    status: Literal["success"]
    """Indicates the webhook URL was successfully removed"""
