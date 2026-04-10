# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionLinkParams"]


class SessionLinkParams(TypedDict, total=False):
    toolkit: Required[str]
    """The unique slug identifier of the toolkit to connect"""

    alias: str
    """A human-readable alias for this connected account.

    Must be unique per entity and toolkit within the project.
    """

    callback_url: str
    """URL where users will be redirected after completing auth"""
