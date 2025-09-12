# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkSubmitResponse"]


class LinkSubmitResponse(BaseModel):
    status: Literal["ACTIVE", "FAILED", "INITIATED"]
    """The status of the connection attempt"""

    callback_url: Optional[str] = None
    """The user callback URL if applicable"""

    redirect_url: Optional[str] = None
    """The OAuth provider redirect URL if applicable.

    If initiated, redirect to this URL
    """
