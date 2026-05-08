# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionLinkParams"]


class SessionLinkParams(TypedDict, total=False):
    toolkit: Required[str]
    """The unique slug identifier of the toolkit to connect"""

    account_type: Literal["PRIVATE", "SHARED"]
    """Sharing model for this connected account.

    PRIVATE (default) is usable only by the owning user_id. SHARED is reachable from
    a tool-router session ONLY when explicitly pinned in the session config — at
    most one SHARED connection per toolkit per session. Sessions never use a SHARED
    connection implicitly. Set at creation time only — cannot be changed later.
    """

    alias: str
    """A human-readable alias for this connected account.

    Must be unique per entity and toolkit within the project.
    """

    callback_url: str
    """URL where users will be redirected after completing auth"""
