# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "AuthConfigCreateParams",
    "Toolkit",
    "AuthConfig",
    "AuthConfigComposioManagedAuthConfigCreate",
    "AuthConfigComposioManagedAuthConfigCreateCredentials",
    "AuthConfigComposioManagedAuthConfigCreateToolAccessConfig",
    "AuthConfigCustomAuthConfigCreate",
    "AuthConfigCustomAuthConfigCreateCredentials",
    "AuthConfigCustomAuthConfigCreateProxyConfig",
    "AuthConfigCustomAuthConfigCreateToolAccessConfig",
]


class AuthConfigCreateParams(TypedDict, total=False):
    toolkit: Required[Toolkit]

    auth_config: AuthConfig


class Toolkit(TypedDict, total=False):
    slug: Required[str]
    """Toolkit slug to create auth config for"""


class AuthConfigComposioManagedAuthConfigCreateCredentials(TypedDict, total=False):
    scopes: Union[str, SequenceNotStr[str]]
    """OAuth scopes requested for the managed auth config."""

    user_scopes: Union[str, SequenceNotStr[str]]
    """OAuth user-token scopes requested for the managed auth config.

    This is primarily used by Slack OAuth v2.
    """


class AuthConfigComposioManagedAuthConfigCreateToolAccessConfig(TypedDict, total=False):
    tools_for_connected_account_creation: SequenceNotStr[str]
    """
    Tools used to generate the minimum required scopes for the auth config (only
    valid for OAuth). If passed, this will update the scopes.
    """


class AuthConfigComposioManagedAuthConfigCreate(TypedDict, total=False):
    type: Required[Literal["use_composio_managed_auth"]]

    credentials: AuthConfigComposioManagedAuthConfigCreateCredentials

    is_enabled_for_tool_router: bool
    """Whether this auth config is enabled for tool router"""

    name: str
    """The name of the integration"""

    restrict_to_following_tools: SequenceNotStr[str]
    """Use tool_access_config instead. This field will be deprecated in the future."""

    shared_credentials: Dict[str, Optional[object]]
    """
    [EXPERIMENTAL] Shared credentials that will be inherited by all connected
    accounts using this auth config
    """

    tool_access_config: AuthConfigComposioManagedAuthConfigCreateToolAccessConfig


class AuthConfigCustomAuthConfigCreateCredentials(TypedDict, total=False):
    scopes: Union[str, SequenceNotStr[str]]
    """OAuth scopes requested for the custom auth config."""

    user_scopes: Union[str, SequenceNotStr[str]]
    """OAuth user-token scopes requested for the custom auth config.

    This is primarily used by Slack OAuth v2.
    """


class AuthConfigCustomAuthConfigCreateProxyConfig(TypedDict, total=False):
    proxy_url: Required[str]
    """The url of the auth proxy"""

    proxy_auth_key: str
    """The auth key for the auth proxy"""


class AuthConfigCustomAuthConfigCreateToolAccessConfig(TypedDict, total=False):
    tools_for_connected_account_creation: SequenceNotStr[str]
    """
    Tools used to generate the minimum required scopes for the auth config (only
    valid for OAuth). If passed, this will update the scopes.
    """


class AuthConfigCustomAuthConfigCreate(TypedDict, total=False):
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
                "CALCOM_AUTH",
                "SERVICE_ACCOUNT",
                "SAML",
                "DCR_OAUTH",
                "S2S_OAUTH2",
            ],
            PropertyInfo(alias="authScheme"),
        ]
    ]

    type: Required[Literal["use_custom_auth"]]

    credentials: AuthConfigCustomAuthConfigCreateCredentials

    is_enabled_for_tool_router: bool
    """Whether this auth config is enabled for tool router"""

    name: str
    """The name of the integration"""

    proxy_config: Optional[AuthConfigCustomAuthConfigCreateProxyConfig]

    restrict_to_following_tools: SequenceNotStr[str]
    """Use tool_access_config instead. This field will be deprecated in the future."""

    sealed_credentials: Dict[str, str]
    """
    [EXPERIMENTAL] Client-sealed secret fields to redeem through the organization
    keyring instance (GET /api/v3.1/keyring/transfer_keys). The plaintext must not
    also appear in credentials.
    """

    shared_credentials: Dict[str, Optional[object]]
    """
    [EXPERIMENTAL] Shared credentials that will be inherited by all connected
    accounts using this auth config
    """

    tool_access_config: AuthConfigCustomAuthConfigCreateToolAccessConfig


AuthConfig: TypeAlias = Union[AuthConfigComposioManagedAuthConfigCreate, AuthConfigCustomAuthConfigCreate]
