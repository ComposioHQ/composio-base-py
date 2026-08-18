# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "AuthConfigUpdateParams",
    "CustomAuthConfigUpdate",
    "CustomAuthConfigUpdateCredentials",
    "CustomAuthConfigUpdateProxyConfig",
    "CustomAuthConfigUpdateToolAccessConfig",
    "DefaultAuthConfigUpdate",
    "DefaultAuthConfigUpdateToolAccessConfig",
]


class CustomAuthConfigUpdate(TypedDict, total=False):
    type: Required[Literal["custom"]]

    credentials: CustomAuthConfigUpdateCredentials

    is_enabled_for_tool_router: bool
    """Whether this auth config is enabled for tool router"""

    name: str
    """The display name of the authentication configuration"""

    proxy_config: Optional[CustomAuthConfigUpdateProxyConfig]

    restrict_to_following_tools: SequenceNotStr[str]
    """Use tool_access_config instead. This field will be deprecated in the future."""

    sealed_credentials: Dict[str, str]
    """
    [EXPERIMENTAL] Client-sealed secret fields to redeem through the organization
    keyring instance (GET /api/v3.1/keyring/transfer_keys). The plaintext must not
    also appear in credentials. Rotates the stored client_secret without Apollo ever
    holding it.
    """

    shared_credentials: Dict[str, Optional[object]]
    """Shared credentials inherited by all connected accounts using this auth config.

    Secret values are redacted in responses, so provide the real values when
    updating; omit this field to leave them unchanged.
    """

    tool_access_config: CustomAuthConfigUpdateToolAccessConfig


class CustomAuthConfigUpdateCredentials(TypedDict, total=False):
    scopes: Union[str, SequenceNotStr[str]]
    """OAuth scopes requested for the auth config."""

    user_scopes: Union[str, SequenceNotStr[str]]
    """OAuth user-token scopes requested for the auth config.

    This is primarily used by Slack OAuth v2.
    """


class CustomAuthConfigUpdateProxyConfig(TypedDict, total=False):
    proxy_url: Required[str]
    """The url of the auth proxy"""

    proxy_auth_key: str
    """The auth key for the auth proxy"""


class CustomAuthConfigUpdateToolAccessConfig(TypedDict, total=False):
    tools_available_for_execution: SequenceNotStr[str]
    """The actions that the user can perform on the auth config.

    If passed, this will update the actions that the user can perform on the auth
    config.
    """

    tools_for_connected_account_creation: SequenceNotStr[str]
    """
    Tools used to generate the minimum required scopes for the auth config (only
    valid for OAuth). If passed, this will update the scopes.
    """


class DefaultAuthConfigUpdate(TypedDict, total=False):
    type: Required[Literal["default"]]

    is_enabled_for_tool_router: bool
    """Whether this auth config is enabled for tool router"""

    name: str
    """The display name of the authentication configuration"""

    restrict_to_following_tools: SequenceNotStr[str]
    """Use tool_access_config instead. This field will be deprecated in the future."""

    scopes: Union[str, SequenceNotStr[str]]
    """OAuth scopes requested for the auth config."""

    shared_credentials: Dict[str, Optional[object]]
    """Shared credentials inherited by all connected accounts using this auth config.

    Secret values are redacted in responses, so provide the real values when
    updating; omit this field to leave them unchanged.
    """

    tool_access_config: DefaultAuthConfigUpdateToolAccessConfig

    user_scopes: Union[str, SequenceNotStr[str]]
    """OAuth user-token scopes requested for the auth config.

    This is primarily used by Slack OAuth v2.
    """


class DefaultAuthConfigUpdateToolAccessConfig(TypedDict, total=False):
    tools_available_for_execution: SequenceNotStr[str]
    """The actions that the user can perform on the auth config.

    If passed, this will update the actions that the user can perform on the auth
    config.
    """

    tools_for_connected_account_creation: SequenceNotStr[str]
    """
    Tools used to generate the minimum required scopes for the auth config (only
    valid for OAuth). If passed, this will update the scopes.
    """


AuthConfigUpdateParams: TypeAlias = Union[CustomAuthConfigUpdate, DefaultAuthConfigUpdate]
