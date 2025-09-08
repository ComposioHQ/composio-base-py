# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkSubmitResponse"]


class LinkSubmitResponse(BaseModel):
    status: Literal["ACTIVE", "FAILED"]
    """The status of the connection attempt"""

    user_callback_url: Optional[str] = None
    """The user callback URL if applicable"""
