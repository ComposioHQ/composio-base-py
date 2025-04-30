# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConnectedAccountCreateParams", "AuthConfig", "Connection"]


class ConnectedAccountCreateParams(TypedDict, total=False):
    auth_config: Required[AuthConfig]

    connection: Required[Connection]


class AuthConfig(TypedDict, total=False):
    id: Required[str]
    """The auth config id of the app (must be a valid auth config id)"""


class Connection(TypedDict, total=False):
    callback_url: str
    """The URL to redirect to after connection completion"""

    data: Dict[str, Optional[object]]
    """Initial data to pass to the connected account"""

    redirect_uri: str
    """DEPRECATED: This parameter will be removed in a future version.

    Please use callback_url instead.
    """

    user_id: str
    """The user id of the connected account"""
