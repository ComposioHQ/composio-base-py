# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkCreateResponse"]


class LinkCreateResponse(BaseModel):
    account_type: Literal["PRIVATE", "SHARED"]
    """The persisted sharing model for this connected account (PRIVATE | SHARED).

    Echoes back the value supplied at creation time so callers can confirm what
    landed without a follow-up GET.
    """

    connected_account_id: str
    """The connected account ID that was created"""

    expires_at: str
    """ISO timestamp when the link expires"""

    link_token: str
    """The generated link token for the auth session"""

    redirect_url: str
    """The redirect URI to send users to for authentication"""
