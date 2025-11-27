# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SessionLinkResponse"]


class SessionLinkResponse(BaseModel):
    connected_account_id: str
    """The unique identifier for the connected account"""

    link_token: str
    """Token used to complete the authentication flow"""

    redirect_url: str
    """The URL where users should be redirected to complete OAuth"""
