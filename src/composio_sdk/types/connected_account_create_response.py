# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectedAccountCreateResponse"]


class ConnectedAccountCreateResponse(BaseModel):
    id: str
    """The id of the connected account"""

    redirect_uri: Optional[str] = None
    """The redirect uri of the app"""

    status: Literal["ACTIVE", "INACTIVE", "DELETED", "INITIATED", "EXPIRED", "FAILED"]
    """The status of the connected account"""
