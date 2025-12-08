# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
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
]


class LinkCreateParams(TypedDict, total=False):
    auth_config_id: Required[str]
    """The auth config id to create a link for"""

    user_id: Required[str]
    """The user id to create a link for"""

    callback_url: str
    """The callback url to create a link for"""

    connection_data: ConnectionData
    """Optional data to pre-fill connection fields with default values"""


class ConnectionDataUnionMember0Typed(TypedDict, total=False):
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


ConnectionDataUnionMember0: TypeAlias = Union[ConnectionDataUnionMember0Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember1Typed(TypedDict, total=False):
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


ConnectionDataUnionMember1: TypeAlias = Union[ConnectionDataUnionMember1Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember2Typed(TypedDict, total=False):
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


ConnectionDataUnionMember2: TypeAlias = Union[ConnectionDataUnionMember2Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember3Typed(TypedDict, total=False):
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


ConnectionDataUnionMember3: TypeAlias = Union[ConnectionDataUnionMember3Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember4Typed(TypedDict, total=False):
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


ConnectionDataUnionMember4: TypeAlias = Union[ConnectionDataUnionMember4Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember5Typed(TypedDict, total=False):
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


ConnectionDataUnionMember5: TypeAlias = Union[ConnectionDataUnionMember5Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember6Typed(TypedDict, total=False):
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


ConnectionDataUnionMember6: TypeAlias = Union[ConnectionDataUnionMember6Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember7Typed(TypedDict, total=False):
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


ConnectionDataUnionMember7: TypeAlias = Union[ConnectionDataUnionMember7Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember8AuthedUser(TypedDict, total=False):
    """for slack user scopes"""

    access_token: str

    scope: str


class ConnectionDataUnionMember8Typed(TypedDict, total=False):
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


ConnectionDataUnionMember8: TypeAlias = Union[ConnectionDataUnionMember8Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember9AuthedUser(TypedDict, total=False):
    """for slack user scopes"""

    access_token: str

    scope: str


class ConnectionDataUnionMember9Typed(TypedDict, total=False):
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


ConnectionDataUnionMember9: TypeAlias = Union[ConnectionDataUnionMember9Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember10Typed(TypedDict, total=False):
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


ConnectionDataUnionMember10: TypeAlias = Union[ConnectionDataUnionMember10Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember11Typed(TypedDict, total=False):
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


ConnectionDataUnionMember11: TypeAlias = Union[ConnectionDataUnionMember11Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember12Typed(TypedDict, total=False):
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


ConnectionDataUnionMember12: TypeAlias = Union[ConnectionDataUnionMember12Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember13Typed(TypedDict, total=False):
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


ConnectionDataUnionMember13: TypeAlias = Union[ConnectionDataUnionMember13Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember14Typed(TypedDict, total=False):
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


ConnectionDataUnionMember14: TypeAlias = Union[ConnectionDataUnionMember14Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember15Typed(TypedDict, total=False):
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


ConnectionDataUnionMember15: TypeAlias = Union[ConnectionDataUnionMember15Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember16Typed(TypedDict, total=False):
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


ConnectionDataUnionMember16: TypeAlias = Union[ConnectionDataUnionMember16Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember17Typed(TypedDict, total=False):
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


ConnectionDataUnionMember17: TypeAlias = Union[ConnectionDataUnionMember17Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember18Typed(TypedDict, total=False):
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


ConnectionDataUnionMember18: TypeAlias = Union[ConnectionDataUnionMember18Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember19Typed(TypedDict, total=False):
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


ConnectionDataUnionMember19: TypeAlias = Union[ConnectionDataUnionMember19Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember20Typed(TypedDict, total=False):
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


ConnectionDataUnionMember20: TypeAlias = Union[ConnectionDataUnionMember20Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember21Typed(TypedDict, total=False):
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


ConnectionDataUnionMember21: TypeAlias = Union[ConnectionDataUnionMember21Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember22Typed(TypedDict, total=False):
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


ConnectionDataUnionMember22: TypeAlias = Union[ConnectionDataUnionMember22Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember23Typed(TypedDict, total=False):
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


ConnectionDataUnionMember23: TypeAlias = Union[ConnectionDataUnionMember23Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember24Typed(TypedDict, total=False):
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


ConnectionDataUnionMember24: TypeAlias = Union[ConnectionDataUnionMember24Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember25Typed(TypedDict, total=False):
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


ConnectionDataUnionMember25: TypeAlias = Union[ConnectionDataUnionMember25Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember26Typed(TypedDict, total=False):
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


ConnectionDataUnionMember26: TypeAlias = Union[ConnectionDataUnionMember26Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember27Typed(TypedDict, total=False):
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


ConnectionDataUnionMember27: TypeAlias = Union[ConnectionDataUnionMember27Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember28Typed(TypedDict, total=False):
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


ConnectionDataUnionMember28: TypeAlias = Union[ConnectionDataUnionMember28Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember29Typed(TypedDict, total=False):
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


ConnectionDataUnionMember29: TypeAlias = Union[ConnectionDataUnionMember29Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember30Typed(TypedDict, total=False):
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


ConnectionDataUnionMember30: TypeAlias = Union[ConnectionDataUnionMember30Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember31Typed(TypedDict, total=False):
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


ConnectionDataUnionMember31: TypeAlias = Union[ConnectionDataUnionMember31Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember32Typed(TypedDict, total=False):
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


ConnectionDataUnionMember32: TypeAlias = Union[ConnectionDataUnionMember32Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember33Typed(TypedDict, total=False):
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


ConnectionDataUnionMember33: TypeAlias = Union[ConnectionDataUnionMember33Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember34Typed(TypedDict, total=False):
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


ConnectionDataUnionMember34: TypeAlias = Union[ConnectionDataUnionMember34Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember35Typed(TypedDict, total=False):
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


ConnectionDataUnionMember35: TypeAlias = Union[ConnectionDataUnionMember35Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember36Typed(TypedDict, total=False):
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


ConnectionDataUnionMember36: TypeAlias = Union[ConnectionDataUnionMember36Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember37Typed(TypedDict, total=False):
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


ConnectionDataUnionMember37: TypeAlias = Union[ConnectionDataUnionMember37Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember38Typed(TypedDict, total=False):
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


ConnectionDataUnionMember38: TypeAlias = Union[ConnectionDataUnionMember38Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember39Typed(TypedDict, total=False):
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


ConnectionDataUnionMember39: TypeAlias = Union[ConnectionDataUnionMember39Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember40Typed(TypedDict, total=False):
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


ConnectionDataUnionMember40: TypeAlias = Union[ConnectionDataUnionMember40Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember41Typed(TypedDict, total=False):
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


ConnectionDataUnionMember41: TypeAlias = Union[ConnectionDataUnionMember41Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember42Typed(TypedDict, total=False):
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


ConnectionDataUnionMember42: TypeAlias = Union[ConnectionDataUnionMember42Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember43Typed(TypedDict, total=False):
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


ConnectionDataUnionMember43: TypeAlias = Union[ConnectionDataUnionMember43Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember44Typed(TypedDict, total=False):
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


ConnectionDataUnionMember44: TypeAlias = Union[ConnectionDataUnionMember44Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember45Typed(TypedDict, total=False):
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


ConnectionDataUnionMember45: TypeAlias = Union[ConnectionDataUnionMember45Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember46Typed(TypedDict, total=False):
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


ConnectionDataUnionMember46: TypeAlias = Union[ConnectionDataUnionMember46Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember47Typed(TypedDict, total=False):
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


ConnectionDataUnionMember47: TypeAlias = Union[ConnectionDataUnionMember47Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember48Typed(TypedDict, total=False):
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


ConnectionDataUnionMember48: TypeAlias = Union[ConnectionDataUnionMember48Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember49Typed(TypedDict, total=False):
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


ConnectionDataUnionMember49: TypeAlias = Union[ConnectionDataUnionMember49Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember50Typed(TypedDict, total=False):
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


ConnectionDataUnionMember50: TypeAlias = Union[ConnectionDataUnionMember50Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember51Typed(TypedDict, total=False):
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


ConnectionDataUnionMember51: TypeAlias = Union[ConnectionDataUnionMember51Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember52Typed(TypedDict, total=False):
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


ConnectionDataUnionMember52: TypeAlias = Union[ConnectionDataUnionMember52Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember53Typed(TypedDict, total=False):
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


ConnectionDataUnionMember53: TypeAlias = Union[ConnectionDataUnionMember53Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember54Typed(TypedDict, total=False):
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


ConnectionDataUnionMember54: TypeAlias = Union[ConnectionDataUnionMember54Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember55Typed(TypedDict, total=False):
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


ConnectionDataUnionMember55: TypeAlias = Union[ConnectionDataUnionMember55Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember56Typed(TypedDict, total=False):
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


ConnectionDataUnionMember56: TypeAlias = Union[ConnectionDataUnionMember56Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember57Typed(TypedDict, total=False):
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


ConnectionDataUnionMember57: TypeAlias = Union[ConnectionDataUnionMember57Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember58Typed(TypedDict, total=False):
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


ConnectionDataUnionMember58: TypeAlias = Union[ConnectionDataUnionMember58Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember59Typed(TypedDict, total=False):
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


ConnectionDataUnionMember59: TypeAlias = Union[ConnectionDataUnionMember59Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember60Typed(TypedDict, total=False):
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


ConnectionDataUnionMember60: TypeAlias = Union[ConnectionDataUnionMember60Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember61Typed(TypedDict, total=False):
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


ConnectionDataUnionMember61: TypeAlias = Union[ConnectionDataUnionMember61Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember62Typed(TypedDict, total=False):
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


ConnectionDataUnionMember62: TypeAlias = Union[ConnectionDataUnionMember62Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember63Typed(TypedDict, total=False):
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


ConnectionDataUnionMember63: TypeAlias = Union[ConnectionDataUnionMember63Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember64Typed(TypedDict, total=False):
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


ConnectionDataUnionMember64: TypeAlias = Union[ConnectionDataUnionMember64Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember65Typed(TypedDict, total=False):
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


ConnectionDataUnionMember65: TypeAlias = Union[ConnectionDataUnionMember65Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember66Typed(TypedDict, total=False):
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


ConnectionDataUnionMember66: TypeAlias = Union[ConnectionDataUnionMember66Typed, Dict[str, Optional[object]]]


class ConnectionDataUnionMember67Typed(TypedDict, total=False):
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


ConnectionDataUnionMember67: TypeAlias = Union[ConnectionDataUnionMember67Typed, Dict[str, Optional[object]]]

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
]
