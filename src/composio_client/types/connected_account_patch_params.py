# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "ConnectedAccountPatchParams",
    "Connection",
    "ConnectionState",
    "ConnectionStateVal",
    "Experimental",
    "ExperimentalACLConfigForShared",
]


class ConnectedAccountPatchParams(TypedDict, total=False):
    alias: str
    """A human-readable alias for this connected account.

    Pass an empty string to clear the alias. Must be unique per entity and toolkit
    within the project.
    """

    connection: Connection

    experimental: Experimental
    """
    Experimental features - not stable, may be modified or removed in future
    versions.
    """


class ConnectionStateVal(TypedDict, total=False):
    """Credential fields to update.

    Only provided fields are changed — omitted fields are preserved. Set a field to null to remove it.
    """

    token: Optional[str]

    api_key: Optional[str]

    api_key_prefix: Optional[str]

    application_id: Optional[str]

    basic_encoded: Optional[str]

    bearer_token: Optional[str]

    credentials_json: Optional[str]

    generic_api_key: Optional[str]

    generic_id: Optional[str]

    generic_secret: Optional[str]

    generic_token: Optional[str]

    installation_id: Optional[str]

    password: Optional[str]

    private_key: Optional[str]

    user_agent: Optional[str]

    username: Optional[str]


class ConnectionState(TypedDict, total=False):
    auth_scheme: Required[
        Annotated[
            Literal["BEARER_TOKEN", "API_KEY", "BASIC", "BASIC_WITH_JWT", "GOOGLE_SERVICE_ACCOUNT", "SERVICE_ACCOUNT"],
            PropertyInfo(alias="authScheme"),
        ]
    ]
    """The auth scheme of the connected account.

    Must match the connection's actual auth scheme.
    """

    val: Required[ConnectionStateVal]
    """Credential fields to update.

    Only provided fields are changed — omitted fields are preserved. Set a field to
    null to remove it.
    """


class Connection(TypedDict, total=False):
    state: Required[ConnectionState]


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

    acl_config_for_shared: ExperimentalACLConfigForShared
    """Access control for SHARED connections.

    Resolution rule (only fires when caller != creator): user in
    not_allowed_user_ids → DENY; allow_all_users=true → ALLOW; user in
    allowed_user_ids → ALLOW; else DENY. Default state (omitted or {}) is
    deny-by-default — only the creator can use.
    """
