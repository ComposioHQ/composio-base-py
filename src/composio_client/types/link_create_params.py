# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "LinkCreateParams",
    "ConnectionData",
    "ConnectionDataUnionMember0",
    "ConnectionDataUnionMember1",
    "ConnectionDataUnionMember2",
    "ConnectionDataUnionMember3",
    "ConnectionDataUnionMember4",
    "ConnectionDataUnionMember5",
    "ConnectionDataUnionMember6",
    "ConnectionDataUnionMember7",
    "ConnectionDataUnionMember8",
    "ConnectionDataUnionMember8AuthedUser",
    "ConnectionDataUnionMember9",
    "ConnectionDataUnionMember9AuthedUser",
    "ConnectionDataUnionMember10",
    "ConnectionDataUnionMember11",
    "ConnectionDataUnionMember12",
    "ConnectionDataUnionMember13",
    "ConnectionDataUnionMember14",
    "ConnectionDataUnionMember15",
    "ConnectionDataUnionMember16",
    "ConnectionDataUnionMember17",
    "ConnectionDataUnionMember18",
    "ConnectionDataUnionMember19",
    "ConnectionDataUnionMember20",
    "ConnectionDataUnionMember21",
    "ConnectionDataUnionMember22",
    "ConnectionDataUnionMember23",
    "ConnectionDataUnionMember24",
    "ConnectionDataUnionMember25",
    "ConnectionDataUnionMember26",
    "ConnectionDataUnionMember27",
    "ConnectionDataUnionMember28",
    "ConnectionDataUnionMember29",
    "ConnectionDataUnionMember30",
    "ConnectionDataUnionMember31",
    "ConnectionDataUnionMember32",
    "ConnectionDataUnionMember33",
    "ConnectionDataUnionMember34",
    "ConnectionDataUnionMember35",
    "ConnectionDataUnionMember36",
    "ConnectionDataUnionMember37",
    "ConnectionDataUnionMember38",
    "ConnectionDataUnionMember39",
    "ConnectionDataUnionMember40",
    "ConnectionDataUnionMember41",
    "ConnectionDataUnionMember42",
    "ConnectionDataUnionMember43",
    "ConnectionDataUnionMember44",
    "ConnectionDataUnionMember45",
    "ConnectionDataUnionMember46",
    "ConnectionDataUnionMember47",
    "ConnectionDataUnionMember48",
    "ConnectionDataUnionMember49",
    "ConnectionDataUnionMember50",
    "ConnectionDataUnionMember51",
    "ConnectionDataUnionMember52",
    "ConnectionDataUnionMember53",
    "ConnectionDataUnionMember54",
    "ConnectionDataUnionMember55",
    "ConnectionDataUnionMember56",
    "ConnectionDataUnionMember57",
    "ConnectionDataUnionMember58",
    "ConnectionDataUnionMember59",
    "ConnectionDataUnionMember60",
    "ConnectionDataUnionMember61",
    "ConnectionDataUnionMember62",
    "ConnectionDataUnionMember63",
    "ConnectionDataUnionMember64",
    "ConnectionDataUnionMember65",
    "ConnectionDataUnionMember66",
    "ConnectionDataUnionMember67",
    "ConnectionDataUnionMember68",
    "ConnectionDataUnionMember69",
    "ConnectionDataUnionMember70",
    "ConnectionDataUnionMember71",
    "ConnectionDataUnionMember72",
    "ConnectionDataUnionMember73",
]


class LinkCreateParams(TypedDict, total=False):
    auth_config_id: Required[str]
    """The auth config id to create a link for"""

    user_id: Required[str]
    """The user id to create a link for"""

    alias: str
    """A human-readable alias for this connected account.

    Must be unique per entity and toolkit within the project.
    """

    callback_url: str
    """The callback url to create a link for"""

    connection_data: ConnectionData
    """Optional data to pre-fill connection fields with default values"""


class ConnectionDataUnionMember0(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember1(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    auth_uri: Required[Annotated[str, PropertyInfo(alias="authUri")]]

    oauth_token: Required[str]

    oauth_token_secret: Required[str]

    redirect_url: Required[Annotated[str, PropertyInfo(alias="redirectUrl")]]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember2(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    oauth_token: Required[str]

    oauth_token_secret: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    callback_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    consumer_key: str

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    oauth_verifier: str

    proxy_password: str

    proxy_username: str

    redirect_url: Annotated[str, PropertyInfo(alias="redirectUrl")]

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember3(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    error: str

    error_description: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember4(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expired_at: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember5(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    oauth_token: Required[str]

    oauth_token_secret: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    callback_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    consumer_key: str

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    oauth_verifier: str

    proxy_password: str

    proxy_username: str

    redirect_url: Annotated[str, PropertyInfo(alias="redirectUrl")]

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember6(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember7(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    redirect_url: Required[Annotated[str, PropertyInfo(alias="redirectUrl")]]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    callback_url: str

    code_verifier: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    final_redirect_uri: Annotated[str, PropertyInfo(alias="finalRedirectUri")]

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    version: str

    webhook_signature: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember8AuthedUser(TypedDict, total=False):
    """for slack user scopes"""

    access_token: str

    scope: str


class ConnectionDataUnionMember8(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    access_token: Required[str]

    account_id: str

    account_url: str

    api_url: str

    authed_user: ConnectionDataUnionMember8AuthedUser
    """for slack user scopes"""

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expires_in: Union[float, str, None]

    extension: str

    form_api_base_url: str

    id_token: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    refresh_token: Optional[str]

    region: str

    scope: Union[str, SequenceNotStr[str], None]

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    token_type: str

    version: str

    webhook_signature: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember9AuthedUser(TypedDict, total=False):
    """for slack user scopes"""

    access_token: str

    scope: str


class ConnectionDataUnionMember9(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    access_token: Required[str]

    account_id: str

    account_url: str

    api_url: str

    authed_user: ConnectionDataUnionMember9AuthedUser
    """for slack user scopes"""

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expires_in: Union[float, str, None]

    extension: str

    form_api_base_url: str

    id_token: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    refresh_token: Optional[str]

    region: str

    scope: Union[str, SequenceNotStr[str], None]

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    token_type: str

    version: str

    webhook_signature: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember10(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    error: str

    error_description: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember11(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expired_at: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember12(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember13(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember14(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_key: str

    api_url: str

    base_url: str

    basic_encoded: str

    bearer_token: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    generic_api_key: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember15(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_key: str

    api_url: str

    base_url: str

    basic_encoded: str

    bearer_token: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    generic_api_key: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember16(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember17(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember18(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    username: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    password: str

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember19(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    username: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    password: str

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember20(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember21(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember22(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    token: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember23(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    token: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember24(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember25(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    redirect_url: Required[Annotated[str, PropertyInfo(alias="redirectUrl")]]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    composio_link_redirect_url: str

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember26(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    credentials_json: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember27(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    credentials_json: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember28(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember29(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember30(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember31(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember32(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    error: str

    error_description: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember33(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expired_at: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember34(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember35(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember36(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember37(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember38(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    error: str

    error_description: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember39(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expired_at: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember40(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember41(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    redirect_url: Required[Annotated[str, PropertyInfo(alias="redirectUrl")]]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember42(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    dev_key: Required[Annotated[str, PropertyInfo(alias="devKey")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember43(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    dev_key: Required[Annotated[str, PropertyInfo(alias="devKey")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember44(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    error: str

    error_description: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember45(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expired_at: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember46(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember47(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember48(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    password: Required[str]

    username: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember49(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    password: Required[str]

    username: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember50(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    password: Required[str]

    username: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    error: str

    error_description: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember51(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    password: Required[str]

    username: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expired_at: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember52(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember53(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember54(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    application_id: Required[str]

    installation_id: Required[str]

    private_key: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember55(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    application_id: Required[str]

    installation_id: Required[str]

    private_key: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember56(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember57(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember58(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember59(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember60(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    error: str

    error_description: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember61(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expired_at: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember62(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember63(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    client_id: Required[str]
    """Dynamically registered client ID"""

    redirect_url: Required[Annotated[str, PropertyInfo(alias="redirectUrl")]]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    callback_url: str

    client_id_issued_at: float

    client_secret: str
    """Dynamically registered client secret"""

    client_secret_expires_at: float

    code_verifier: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    final_redirect_uri: Annotated[str, PropertyInfo(alias="finalRedirectUri")]

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember64(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    access_token: Required[str]

    client_id: Required[str]
    """Dynamically registered client ID"""

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    client_id_issued_at: float

    client_secret: str
    """Dynamically registered client secret"""

    client_secret_expires_at: float

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expires_in: Union[float, str, None]

    extension: str

    form_api_base_url: str

    id_token: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    refresh_token: Optional[str]

    region: str

    scope: Union[str, SequenceNotStr[str], None]

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    token_type: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember65(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    access_token: Required[str]

    client_id: Required[str]
    """Dynamically registered client ID"""

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    client_id_issued_at: float

    client_secret: str
    """Dynamically registered client secret"""

    client_secret_expires_at: float

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expires_in: Union[float, str, None]

    extension: str

    form_api_base_url: str

    id_token: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    refresh_token: Optional[str]

    region: str

    scope: Union[str, SequenceNotStr[str], None]

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    token_type: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember66(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    error: str

    error_description: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember67(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expired_at: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    long_redirect_url: bool
    """Whether to return the redirect url without shortening"""

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    state_prefix: str
    """The oauth2 state prefix for the connection"""

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember68(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember69(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember70(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    access_token: Required[str]

    client_id: Required[str]

    client_secret: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expires_at: str

    expires_in: Union[float, str, None]

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    scope: Union[str, SequenceNotStr[str], None]

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    token_type: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember71(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    access_token: Required[str]

    client_id: Required[str]

    client_secret: Required[str]

    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expires_at: str

    expires_in: Union[float, str, None]

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    scope: Union[str, SequenceNotStr[str], None]

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    token_type: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember72(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    error: str

    error_description: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


class ConnectionDataUnionMember73(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    account_id: str

    account_url: str

    api_url: str

    base_url: str

    borneo_dashboard_url: str

    companydomain: Annotated[str, PropertyInfo(alias="COMPANYDOMAIN")]

    dc: str

    domain: str

    expired_at: str

    extension: str

    form_api_base_url: str

    instance_endpoint: Annotated[str, PropertyInfo(alias="instanceEndpoint")]

    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    proxy_password: str

    proxy_username: str

    region: str

    server_location: str

    shop: str

    site_name: str

    subdomain: str

    version: str

    your_server: str

    your_domain: Annotated[str, PropertyInfo(alias="your-domain")]


ConnectionData: TypeAlias = Union[
    ConnectionDataUnionMember0,
    ConnectionDataUnionMember1,
    ConnectionDataUnionMember2,
    ConnectionDataUnionMember3,
    ConnectionDataUnionMember4,
    ConnectionDataUnionMember5,
    ConnectionDataUnionMember6,
    ConnectionDataUnionMember7,
    ConnectionDataUnionMember8,
    ConnectionDataUnionMember9,
    ConnectionDataUnionMember10,
    ConnectionDataUnionMember11,
    ConnectionDataUnionMember12,
    ConnectionDataUnionMember13,
    ConnectionDataUnionMember14,
    ConnectionDataUnionMember15,
    ConnectionDataUnionMember16,
    ConnectionDataUnionMember17,
    ConnectionDataUnionMember18,
    ConnectionDataUnionMember19,
    ConnectionDataUnionMember20,
    ConnectionDataUnionMember21,
    ConnectionDataUnionMember22,
    ConnectionDataUnionMember23,
    ConnectionDataUnionMember24,
    ConnectionDataUnionMember25,
    ConnectionDataUnionMember26,
    ConnectionDataUnionMember27,
    ConnectionDataUnionMember28,
    ConnectionDataUnionMember29,
    ConnectionDataUnionMember30,
    ConnectionDataUnionMember31,
    ConnectionDataUnionMember32,
    ConnectionDataUnionMember33,
    ConnectionDataUnionMember34,
    ConnectionDataUnionMember35,
    ConnectionDataUnionMember36,
    ConnectionDataUnionMember37,
    ConnectionDataUnionMember38,
    ConnectionDataUnionMember39,
    ConnectionDataUnionMember40,
    ConnectionDataUnionMember41,
    ConnectionDataUnionMember42,
    ConnectionDataUnionMember43,
    ConnectionDataUnionMember44,
    ConnectionDataUnionMember45,
    ConnectionDataUnionMember46,
    ConnectionDataUnionMember47,
    ConnectionDataUnionMember48,
    ConnectionDataUnionMember49,
    ConnectionDataUnionMember50,
    ConnectionDataUnionMember51,
    ConnectionDataUnionMember52,
    ConnectionDataUnionMember53,
    ConnectionDataUnionMember54,
    ConnectionDataUnionMember55,
    ConnectionDataUnionMember56,
    ConnectionDataUnionMember57,
    ConnectionDataUnionMember58,
    ConnectionDataUnionMember59,
    ConnectionDataUnionMember60,
    ConnectionDataUnionMember61,
    ConnectionDataUnionMember62,
    ConnectionDataUnionMember63,
    ConnectionDataUnionMember64,
    ConnectionDataUnionMember65,
    ConnectionDataUnionMember66,
    ConnectionDataUnionMember67,
    ConnectionDataUnionMember68,
    ConnectionDataUnionMember69,
    ConnectionDataUnionMember70,
    ConnectionDataUnionMember71,
    ConnectionDataUnionMember72,
    ConnectionDataUnionMember73,
]
