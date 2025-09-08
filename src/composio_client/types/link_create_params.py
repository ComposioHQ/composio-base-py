# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LinkCreateParams"]


class LinkCreateParams(TypedDict, total=False):
    auth_config_id: Required[str]
    """The auth config id to create a link for"""

    user_id: Required[str]
    """The user id to create a link for"""

    callback_url: str
    """The callback url to create a link for"""
