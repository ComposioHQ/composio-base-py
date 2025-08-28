# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["WebhookRetrieveResponse", "URL", "URLUnionMember0", "URLUnionMember1"]


class URLUnionMember0(BaseModel):
    type: Literal["trigger"]
    """Identifies this as a trigger webhook response"""

    webhook_url: Optional[str] = None
    """The URL endpoint where trigger notifications will be delivered"""


class URLUnionMember1(BaseModel):
    type: Literal["event"]
    """Identifies this as an event webhook response"""

    event_webhook_url: Optional[str] = None
    """The URL endpoint where event notifications will be delivered"""


URL: TypeAlias = Union[URLUnionMember0, URLUnionMember1]


class WebhookRetrieveResponse(BaseModel):
    status: Literal["success", "not found"]
    """Indicates whether the webhook was found and retrieved successfully"""

    url: URL
    """The webhook configuration containing either trigger or event webhook URL"""

    webhook_secret: str
    """The secret key that should be used to verify webhook signatures"""
