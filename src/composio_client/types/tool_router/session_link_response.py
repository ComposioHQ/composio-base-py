# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SessionLinkResponse", "Experimental", "ExperimentalACLConfigForShared"]


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


class SessionLinkResponse(BaseModel):
    connected_account_id: str
    """The unique identifier for the connected account"""

    link_token: str
    """Token used to complete the authentication flow"""

    redirect_url: str
    """The URL where users should be redirected to complete OAuth"""

    experimental: Optional[Experimental] = None
    """
    Experimental features - not stable, may be modified or removed in future
    versions.
    """
