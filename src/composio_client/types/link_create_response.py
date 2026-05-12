# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkCreateResponse", "Experimental", "ExperimentalACLConfigForShared"]


class ExperimentalACLConfigForShared(BaseModel):
    """Access control for SHARED connections.

    Visible only to the connection creator and project/org API key callers; non-creator cookie callers receive the response without this block.
    """

    allow_all_users: bool

    allowed_user_ids: List[str]

    not_allowed_user_ids: List[str]


class Experimental(BaseModel):
    """
    Experimental features - not stable, may be modified or removed in future versions.
    """

    account_type: Literal["PRIVATE", "SHARED"]
    """Sharing model for this connected account.

    PRIVATE is usable only by the owning user_id. SHARED is reachable from a
    tool-router session only when explicitly pinned in the session config.
    """

    acl_config_for_shared: Optional[ExperimentalACLConfigForShared] = None
    """Access control for SHARED connections.

    Visible only to the connection creator and project/org API key callers;
    non-creator cookie callers receive the response without this block.
    """


class LinkCreateResponse(BaseModel):
    connected_account_id: str
    """The connected account ID that was created"""

    expires_at: str
    """ISO timestamp when the link expires"""

    link_token: str
    """The generated link token for the auth session"""

    redirect_url: str
    """The redirect URI to send users to for authentication"""

    experimental: Optional[Experimental] = None
    """
    Experimental features - not stable, may be modified or removed in future
    versions.
    """
