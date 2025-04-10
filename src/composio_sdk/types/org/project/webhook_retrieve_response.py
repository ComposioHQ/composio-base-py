# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["WebhookRetrieveResponse", "URL", "URLUnionMember0", "URLUnionMember1"]


class URLUnionMember0(BaseModel):
    type: Literal["trigger"]

    webhook_url: Optional[str] = None
    """Webhook URL"""


class URLUnionMember1(BaseModel):
    type: Literal["event"]

    event_webhook_url: Optional[str] = None
    """Event webhook URL"""


URL: TypeAlias = Union[URLUnionMember0, URLUnionMember1]


class WebhookRetrieveResponse(BaseModel):
    status: Literal["success", "not found"]
    """Status of the webhook"""

    url: URL

    webhook_secret: str
    """Webhook secret"""
