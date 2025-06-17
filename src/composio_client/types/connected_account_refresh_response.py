# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectedAccountRefreshResponse"]


class ConnectedAccountRefreshResponse(BaseModel):
    id: str
    """The unique identifier of the connected account"""

    redirect_url: Optional[str] = None
    """
    The URL to which the user should be redirected to complete the authentication
    process (null for auth schemes that do not require redirection)
    """

    status: Literal["INITIALIZING", "INITIATED", "ACTIVE", "FAILED", "EXPIRED", "INACTIVE"]
    """The current status of the connected account (e.g., active, pending, failed)"""
