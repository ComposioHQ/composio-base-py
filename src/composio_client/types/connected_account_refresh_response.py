# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectedAccountRefreshResponse"]


class ConnectedAccountRefreshResponse(BaseModel):
    id: str
    """The id of the connected account"""

    redirect_url: Optional[str] = None
    """The redirect URL of the app (previously named redirect_uri)"""

    status: Literal["ACTIVE", "INACTIVE", "DELETED", "INITIATED", "EXPIRED", "FAILED"]
    """The status of the connected account"""
