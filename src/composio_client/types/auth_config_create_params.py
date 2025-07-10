# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AuthConfigCreateParams",
    "Toolkit",
    "AuthConfig",
    "AuthConfigUnionMember0",
    "AuthConfigUnionMember0ToolAccessConfig",
    "AuthConfigUnionMember1",
    "AuthConfigUnionMember1ProxyConfig",
    "AuthConfigUnionMember1ToolAccessConfig",
]


class AuthConfigCreateParams(TypedDict, total=False):
    toolkit: Required[Toolkit]

    auth_config: AuthConfig


class Toolkit(TypedDict, total=False):
    slug: Required[str]
    """Toolkit slug to create auth config for"""


class AuthConfigUnionMember0ToolAccessConfig(TypedDict, total=False):
    tools_for_connected_account_creation: List[str]
    """
    Tools used to generate the minimum required scopes for the auth config (only
    valid for OAuth). If passed, this will update the scopes.
    """


class AuthConfigUnionMember0(TypedDict, total=False):
    type: Required[Literal["use_composio_managed_auth"]]

    credentials: Dict[str, Union[str, bool, float]]

    name: str
    """The name of the integration"""

    tool_access_config: AuthConfigUnionMember0ToolAccessConfig


class AuthConfigUnionMember1ProxyConfig(TypedDict, total=False):
    proxy_url: Required[str]
    """The url of the auth proxy"""

    proxy_auth_key: str
    """The auth key for the auth proxy"""


class AuthConfigUnionMember1ToolAccessConfig(TypedDict, total=False):
    tools_for_connected_account_creation: List[str]
    """
    Tools used to generate the minimum required scopes for the auth config (only
    valid for OAuth). If passed, this will update the scopes.
    """


class AuthConfigUnionMember1(TypedDict, total=False):
    auth_scheme: Required[
        Annotated[
            Literal[
                "OAUTH2",
                "OAUTH1",
                "API_KEY",
                "BASIC",
                "BILLCOM_AUTH",
                "BEARER_TOKEN",
                "GOOGLE_SERVICE_ACCOUNT",
                "NO_AUTH",
                "BASIC_WITH_JWT",
                "COMPOSIO_LINK",
                "CALCOM_AUTH",
            ],
            PropertyInfo(alias="authScheme"),
        ]
    ]

    credentials: Required[Dict[str, Union[str, bool, float]]]

    type: Required[Literal["use_custom_auth"]]

    name: str
    """The name of the integration"""

    proxy_config: AuthConfigUnionMember1ProxyConfig

    tool_access_config: AuthConfigUnionMember1ToolAccessConfig


AuthConfig: TypeAlias = Union[AuthConfigUnionMember0, AuthConfigUnionMember1]
