# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["SessionLinkParams", "Experimental", "ExperimentalACLConfigForShared"]


class SessionLinkParams(TypedDict, total=False):
    toolkit: Required[str]
    """The unique slug identifier of the toolkit to connect"""

    alias: str
    """A human-readable alias for this connected account.

    Must be unique per entity and toolkit within the project.
    """

    callback_url: str
    """URL where users will be redirected after completing auth"""

    experimental: Experimental
    """
    Experimental features - not stable, may be modified or removed in future
    versions.
    """


class ExperimentalACLConfigForShared(TypedDict, total=False):
    """Access control for SHARED connections.

    Resolution rule (only fires when caller != creator): user in not_allowed_user_ids → DENY; allow_all_users=true → ALLOW; user in allowed_user_ids → ALLOW; else DENY. Default state (omitted or {}) is deny-by-default — only the creator can use.
    """

    allow_all_users: bool
    """Wildcard "any user_id in the project" allow toggle.

    Only valid on SHARED connections.
    """

    allowed_user_ids: SequenceNotStr[str]
    """Explicit allow list of user_ids who can use this SHARED connection."""

    not_allowed_user_ids: SequenceNotStr[str]
    """Explicit deny list. Wins on conflict with allow_all_users and allowed_user_ids."""


class Experimental(TypedDict, total=False):
    """
    Experimental features - not stable, may be modified or removed in future versions.
    """

    account_type: Literal["PRIVATE", "SHARED"]
    """Sharing model for this connected account.

    PRIVATE (default) is usable only by the owning user_id. SHARED is reachable from
    a tool-router session ONLY when explicitly pinned in the session config — at
    most one SHARED connection per toolkit per session. Sessions never use a SHARED
    connection implicitly.
    """

    acl_config_for_shared: ExperimentalACLConfigForShared
    """Access control for SHARED connections.

    Resolution rule (only fires when caller != creator): user in
    not_allowed_user_ids → DENY; allow_all_users=true → ALLOW; user in
    allowed_user_ids → ALLOW; else DENY. Default state (omitted or {}) is
    deny-by-default — only the creator can use.
    """
