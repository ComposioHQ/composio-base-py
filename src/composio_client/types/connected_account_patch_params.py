# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConnectedAccountPatchParams", "Connection", "ConnectionState", "ConnectionStateVal"]


class ConnectedAccountPatchParams(TypedDict, total=False):
    alias: str
    """A human-readable alias for this connected account.

    Pass an empty string to clear the alias. Must be unique per entity and toolkit
    within the project.
    """

    connection: Connection


class ConnectionStateVal(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    """Credential fields to update.

    Only provided fields are changed — omitted fields are preserved. Set a field to null to remove it.
    """

    token: Optional[str]

    account_id: Optional[str]

    account_url: Optional[str]

    api_key: Optional[str]

    api_url: Optional[str]

    application_id: Optional[str]

    base_url: Optional[str]

    basic_encoded: Optional[str]

    bearer_token: Optional[str]

    borneo_dashboard_url: Optional[str]

    companydomain: Annotated[Optional[str], PropertyInfo(alias="COMPANYDOMAIN")]

    credentials_json: Optional[str]

    dc: Optional[str]

    domain: Optional[str]

    extension: Optional[str]

    form_api_base_url: Optional[str]

    generic_api_key: Optional[str]

    installation_id: Optional[str]

    instance_endpoint: Annotated[Optional[str], PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[Optional[str], PropertyInfo(alias="instanceName")]

    password: Optional[str]

    private_key: Optional[str]

    proxy_password: Optional[str]

    proxy_username: Optional[str]

    region: Optional[str]

    server_location: Optional[str]

    shop: Optional[str]

    site_name: Optional[str]

    subdomain: Optional[str]

    username: Optional[str]

    version: Optional[str]

    your_server: Optional[str]

    your_domain: Annotated[Optional[str], PropertyInfo(alias="your-domain")]


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
