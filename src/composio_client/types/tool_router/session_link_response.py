# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SessionLinkResponse"]


class SessionLinkResponse(BaseModel):
    account_type: Literal["PRIVATE", "SHARED"]
    """PRIVATE (default) is usable only by the owning user_id.

    SHARED is reachable from a tool-router session ONLY when explicitly pinned, with
    at most one SHARED per toolkit per session.
    """

    connected_account_id: str
    """The unique identifier for the connected account"""

    link_token: str
    """Token used to complete the authentication flow"""

    redirect_url: str
    """The URL where users should be redirected to complete OAuth"""
