# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ConnectedAccountCreateParams",
    "AuthConfig",
    "Connection",
    "ConnectionState",
    "ConnectionStateUnionMember0",
    "ConnectionStateUnionMember0Val",
    "ConnectionStateUnionMember0ValUnionMember0",
    "ConnectionStateUnionMember0ValUnionMember1",
    "ConnectionStateUnionMember0ValUnionMember2",
    "ConnectionStateUnionMember0ValUnionMember3",
    "ConnectionStateUnionMember0ValUnionMember4",
    "ConnectionStateUnionMember0ValUnionMember5",
    "ConnectionStateUnionMember1",
    "ConnectionStateUnionMember1Val",
    "ConnectionStateUnionMember1ValUnionMember0",
    "ConnectionStateUnionMember1ValUnionMember1",
    "ConnectionStateUnionMember1ValUnionMember2",
    "ConnectionStateUnionMember1ValUnionMember2AuthedUser",
    "ConnectionStateUnionMember1ValUnionMember3",
    "ConnectionStateUnionMember1ValUnionMember3AuthedUser",
    "ConnectionStateUnionMember1ValUnionMember4",
    "ConnectionStateUnionMember1ValUnionMember5",
    "ConnectionStateUnionMember2",
    "ConnectionStateUnionMember2Val",
    "ConnectionStateUnionMember2ValUnionMember0",
    "ConnectionStateUnionMember2ValUnionMember1",
    "ConnectionStateUnionMember2ValUnionMember2",
    "ConnectionStateUnionMember2ValUnionMember3",
    "ConnectionStateUnionMember2ValUnionMember4",
    "ConnectionStateUnionMember2ValUnionMember5",
    "ConnectionStateUnionMember3",
    "ConnectionStateUnionMember3Val",
    "ConnectionStateUnionMember3ValUnionMember0",
    "ConnectionStateUnionMember3ValUnionMember1",
    "ConnectionStateUnionMember4",
    "ConnectionStateUnionMember4Val",
    "ConnectionStateUnionMember4ValUnionMember0",
    "ConnectionStateUnionMember4ValUnionMember1",
    "ConnectionStateUnionMember5",
    "ConnectionStateUnionMember5Val",
    "ConnectionStateUnionMember5ValUnionMember0",
    "ConnectionStateUnionMember5ValUnionMember1",
    "ConnectionStateUnionMember6",
    "ConnectionStateUnionMember6Val",
    "ConnectionStateUnionMember6ValUnionMember0",
    "ConnectionStateUnionMember6ValUnionMember1",
    "ConnectionStateUnionMember7",
    "ConnectionStateUnionMember7Val",
    "ConnectionStateUnionMember7ValUnionMember0",
    "ConnectionStateUnionMember7ValUnionMember1",
    "ConnectionStateUnionMember7ValUnionMember2",
    "ConnectionStateUnionMember7ValUnionMember3",
    "ConnectionStateUnionMember8",
    "ConnectionStateUnionMember8Val",
    "ConnectionStateUnionMember8ValUnionMember0",
    "ConnectionStateUnionMember8ValUnionMember1",
    "ConnectionStateUnionMember8ValUnionMember2",
    "ConnectionStateUnionMember8ValUnionMember3",
    "ConnectionStateUnionMember9",
    "ConnectionStateUnionMember9Val",
    "ConnectionStateUnionMember9ValUnionMember0",
    "ConnectionStateUnionMember9ValUnionMember1",
    "ConnectionStateUnionMember9ValUnionMember2",
    "ConnectionStateUnionMember9ValUnionMember3",
    "ConnectionStateUnionMember9ValUnionMember4",
    "ConnectionStateUnionMember9ValUnionMember5",
    "ConnectionStateUnionMember10",
    "ConnectionStateUnionMember10Val",
    "ConnectionStateUnionMember10ValUnionMember0",
    "ConnectionStateUnionMember10ValUnionMember1",
    "ConnectionStateUnionMember10ValUnionMember2",
    "ConnectionStateUnionMember10ValUnionMember3",
]


class ConnectedAccountCreateParams(TypedDict, total=False):
    auth_config: Required[AuthConfig]

    connection: Required[Connection]


class AuthConfig(TypedDict, total=False):
    id: Required[str]
    """The auth config id of the app (must be a valid auth config id)"""


class ConnectionStateUnionMember0ValUnionMember0Typed(TypedDict, total=False):
    status: Required[Literal["INITIALIZING"]]

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


ConnectionStateUnionMember0ValUnionMember0: TypeAlias = Union[
    ConnectionStateUnionMember0ValUnionMember0Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember0ValUnionMember1Typed(TypedDict, total=False):
    auth_uri: Required[Annotated[str, PropertyInfo(alias="authUri")]]

    oauth_token: Required[str]

    oauth_token_secret: Required[str]

    redirect_url: Required[Annotated[str, PropertyInfo(alias="redirectUrl")]]

    status: Required[Literal["INITIATED"]]

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


ConnectionStateUnionMember0ValUnionMember1: TypeAlias = Union[
    ConnectionStateUnionMember0ValUnionMember1Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember0ValUnionMember2Typed(TypedDict, total=False):
    oauth_token: Required[str]

    oauth_token_secret: Required[str]

    status: Required[Literal["ACTIVE"]]

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


ConnectionStateUnionMember0ValUnionMember2: TypeAlias = Union[
    ConnectionStateUnionMember0ValUnionMember2Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember0ValUnionMember3Typed(TypedDict, total=False):
    status: Required[Literal["FAILED"]]

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


ConnectionStateUnionMember0ValUnionMember3: TypeAlias = Union[
    ConnectionStateUnionMember0ValUnionMember3Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember0ValUnionMember4Typed(TypedDict, total=False):
    status: Required[Literal["EXPIRED"]]

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


ConnectionStateUnionMember0ValUnionMember4: TypeAlias = Union[
    ConnectionStateUnionMember0ValUnionMember4Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember0ValUnionMember5Typed(TypedDict, total=False):
    oauth_token: Required[str]

    oauth_token_secret: Required[str]

    status: Required[Literal["INACTIVE"]]

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


ConnectionStateUnionMember0ValUnionMember5: TypeAlias = Union[
    ConnectionStateUnionMember0ValUnionMember5Typed, Dict[str, Optional[object]]
]

ConnectionStateUnionMember0Val: TypeAlias = Union[
    ConnectionStateUnionMember0ValUnionMember0,
    ConnectionStateUnionMember0ValUnionMember1,
    ConnectionStateUnionMember0ValUnionMember2,
    ConnectionStateUnionMember0ValUnionMember3,
    ConnectionStateUnionMember0ValUnionMember4,
    ConnectionStateUnionMember0ValUnionMember5,
]


class ConnectionStateUnionMember0(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["OAUTH1"], PropertyInfo(alias="authScheme")]]

    val: Required[ConnectionStateUnionMember0Val]


class ConnectionStateUnionMember1ValUnionMember0Typed(TypedDict, total=False):
    status: Required[Literal["INITIALIZING"]]

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


ConnectionStateUnionMember1ValUnionMember0: TypeAlias = Union[
    ConnectionStateUnionMember1ValUnionMember0Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember1ValUnionMember1Typed(TypedDict, total=False):
    redirect_url: Required[Annotated[str, PropertyInfo(alias="redirectUrl")]]

    status: Required[Literal["INITIATED"]]

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


ConnectionStateUnionMember1ValUnionMember1: TypeAlias = Union[
    ConnectionStateUnionMember1ValUnionMember1Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember1ValUnionMember2AuthedUser(TypedDict, total=False):
    access_token: str

    scope: str


class ConnectionStateUnionMember1ValUnionMember2Typed(TypedDict, total=False):
    access_token: Required[str]

    status: Required[Literal["ACTIVE"]]

    account_id: str

    account_url: str

    api_url: str

    authed_user: ConnectionStateUnionMember1ValUnionMember2AuthedUser
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

    scope: Union[str, List[str], None]

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


ConnectionStateUnionMember1ValUnionMember2: TypeAlias = Union[
    ConnectionStateUnionMember1ValUnionMember2Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember1ValUnionMember3AuthedUser(TypedDict, total=False):
    access_token: str

    scope: str


class ConnectionStateUnionMember1ValUnionMember3Typed(TypedDict, total=False):
    access_token: Required[str]

    status: Required[Literal["INACTIVE"]]

    account_id: str

    account_url: str

    api_url: str

    authed_user: ConnectionStateUnionMember1ValUnionMember3AuthedUser
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

    scope: Union[str, List[str], None]

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


ConnectionStateUnionMember1ValUnionMember3: TypeAlias = Union[
    ConnectionStateUnionMember1ValUnionMember3Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember1ValUnionMember4Typed(TypedDict, total=False):
    status: Required[Literal["FAILED"]]

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


ConnectionStateUnionMember1ValUnionMember4: TypeAlias = Union[
    ConnectionStateUnionMember1ValUnionMember4Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember1ValUnionMember5Typed(TypedDict, total=False):
    status: Required[Literal["EXPIRED"]]

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


ConnectionStateUnionMember1ValUnionMember5: TypeAlias = Union[
    ConnectionStateUnionMember1ValUnionMember5Typed, Dict[str, Optional[object]]
]

ConnectionStateUnionMember1Val: TypeAlias = Union[
    ConnectionStateUnionMember1ValUnionMember0,
    ConnectionStateUnionMember1ValUnionMember1,
    ConnectionStateUnionMember1ValUnionMember2,
    ConnectionStateUnionMember1ValUnionMember3,
    ConnectionStateUnionMember1ValUnionMember4,
    ConnectionStateUnionMember1ValUnionMember5,
]


class ConnectionStateUnionMember1(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["OAUTH2"], PropertyInfo(alias="authScheme")]]

    val: Required[ConnectionStateUnionMember1Val]


class ConnectionStateUnionMember2ValUnionMember0Typed(TypedDict, total=False):
    status: Required[Literal["INITIALIZING"]]

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


ConnectionStateUnionMember2ValUnionMember0: TypeAlias = Union[
    ConnectionStateUnionMember2ValUnionMember0Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember2ValUnionMember1Typed(TypedDict, total=False):
    redirect_url: Required[Annotated[str, PropertyInfo(alias="redirectUrl")]]

    status: Required[Literal["INITIATED"]]

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


ConnectionStateUnionMember2ValUnionMember1: TypeAlias = Union[
    ConnectionStateUnionMember2ValUnionMember1Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember2ValUnionMember2Typed(TypedDict, total=False):
    status: Required[Literal["ACTIVE"]]

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


ConnectionStateUnionMember2ValUnionMember2: TypeAlias = Union[
    ConnectionStateUnionMember2ValUnionMember2Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember2ValUnionMember3Typed(TypedDict, total=False):
    status: Required[Literal["INACTIVE"]]

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


ConnectionStateUnionMember2ValUnionMember3: TypeAlias = Union[
    ConnectionStateUnionMember2ValUnionMember3Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember2ValUnionMember4Typed(TypedDict, total=False):
    status: Required[Literal["FAILED"]]

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


ConnectionStateUnionMember2ValUnionMember4: TypeAlias = Union[
    ConnectionStateUnionMember2ValUnionMember4Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember2ValUnionMember5Typed(TypedDict, total=False):
    status: Required[Literal["EXPIRED"]]

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


ConnectionStateUnionMember2ValUnionMember5: TypeAlias = Union[
    ConnectionStateUnionMember2ValUnionMember5Typed, Dict[str, Optional[object]]
]

ConnectionStateUnionMember2Val: TypeAlias = Union[
    ConnectionStateUnionMember2ValUnionMember0,
    ConnectionStateUnionMember2ValUnionMember1,
    ConnectionStateUnionMember2ValUnionMember2,
    ConnectionStateUnionMember2ValUnionMember3,
    ConnectionStateUnionMember2ValUnionMember4,
    ConnectionStateUnionMember2ValUnionMember5,
]


class ConnectionStateUnionMember2(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["COMPOSIO_LINK"], PropertyInfo(alias="authScheme")]]

    val: Required[ConnectionStateUnionMember2Val]


class ConnectionStateUnionMember3ValUnionMember0Typed(TypedDict, total=False):
    status: Required[Literal["ACTIVE"]]

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


ConnectionStateUnionMember3ValUnionMember0: TypeAlias = Union[
    ConnectionStateUnionMember3ValUnionMember0Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember3ValUnionMember1Typed(TypedDict, total=False):
    status: Required[Literal["INACTIVE"]]

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


ConnectionStateUnionMember3ValUnionMember1: TypeAlias = Union[
    ConnectionStateUnionMember3ValUnionMember1Typed, Dict[str, Optional[object]]
]

ConnectionStateUnionMember3Val: TypeAlias = Union[
    ConnectionStateUnionMember3ValUnionMember0, ConnectionStateUnionMember3ValUnionMember1
]


class ConnectionStateUnionMember3(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["API_KEY"], PropertyInfo(alias="authScheme")]]

    val: Required[ConnectionStateUnionMember3Val]


class ConnectionStateUnionMember4ValUnionMember0Typed(TypedDict, total=False):
    password: Required[str]

    status: Required[Literal["ACTIVE"]]

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


ConnectionStateUnionMember4ValUnionMember0: TypeAlias = Union[
    ConnectionStateUnionMember4ValUnionMember0Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember4ValUnionMember1Typed(TypedDict, total=False):
    password: Required[str]

    status: Required[Literal["INACTIVE"]]

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


ConnectionStateUnionMember4ValUnionMember1: TypeAlias = Union[
    ConnectionStateUnionMember4ValUnionMember1Typed, Dict[str, Optional[object]]
]

ConnectionStateUnionMember4Val: TypeAlias = Union[
    ConnectionStateUnionMember4ValUnionMember0, ConnectionStateUnionMember4ValUnionMember1
]


class ConnectionStateUnionMember4(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["BASIC"], PropertyInfo(alias="authScheme")]]

    val: Required[ConnectionStateUnionMember4Val]


class ConnectionStateUnionMember5ValUnionMember0Typed(TypedDict, total=False):
    token: Required[str]

    status: Required[Literal["ACTIVE"]]

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


ConnectionStateUnionMember5ValUnionMember0: TypeAlias = Union[
    ConnectionStateUnionMember5ValUnionMember0Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember5ValUnionMember1Typed(TypedDict, total=False):
    token: Required[str]

    status: Required[Literal["INACTIVE"]]

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


ConnectionStateUnionMember5ValUnionMember1: TypeAlias = Union[
    ConnectionStateUnionMember5ValUnionMember1Typed, Dict[str, Optional[object]]
]

ConnectionStateUnionMember5Val: TypeAlias = Union[
    ConnectionStateUnionMember5ValUnionMember0, ConnectionStateUnionMember5ValUnionMember1
]


class ConnectionStateUnionMember5(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["BEARER_TOKEN"], PropertyInfo(alias="authScheme")]]

    val: Required[ConnectionStateUnionMember5Val]


class ConnectionStateUnionMember6ValUnionMember0Typed(TypedDict, total=False):
    credentials_json: Required[str]

    status: Required[Literal["ACTIVE"]]

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


ConnectionStateUnionMember6ValUnionMember0: TypeAlias = Union[
    ConnectionStateUnionMember6ValUnionMember0Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember6ValUnionMember1Typed(TypedDict, total=False):
    credentials_json: Required[str]

    status: Required[Literal["INACTIVE"]]

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


ConnectionStateUnionMember6ValUnionMember1: TypeAlias = Union[
    ConnectionStateUnionMember6ValUnionMember1Typed, Dict[str, Optional[object]]
]

ConnectionStateUnionMember6Val: TypeAlias = Union[
    ConnectionStateUnionMember6ValUnionMember0, ConnectionStateUnionMember6ValUnionMember1
]


class ConnectionStateUnionMember6(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["GOOGLE_SERVICE_ACCOUNT"], PropertyInfo(alias="authScheme")]]

    val: Required[ConnectionStateUnionMember6Val]


class ConnectionStateUnionMember7ValUnionMember0Typed(TypedDict, total=False):
    status: Required[Literal["ACTIVE"]]

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


ConnectionStateUnionMember7ValUnionMember0: TypeAlias = Union[
    ConnectionStateUnionMember7ValUnionMember0Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember7ValUnionMember1Typed(TypedDict, total=False):
    status: Required[Literal["INACTIVE"]]

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


ConnectionStateUnionMember7ValUnionMember1: TypeAlias = Union[
    ConnectionStateUnionMember7ValUnionMember1Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember7ValUnionMember2Typed(TypedDict, total=False):
    status: Required[Literal["FAILED"]]

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


ConnectionStateUnionMember7ValUnionMember2: TypeAlias = Union[
    ConnectionStateUnionMember7ValUnionMember2Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember7ValUnionMember3Typed(TypedDict, total=False):
    status: Required[Literal["EXPIRED"]]

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


ConnectionStateUnionMember7ValUnionMember3: TypeAlias = Union[
    ConnectionStateUnionMember7ValUnionMember3Typed, Dict[str, Optional[object]]
]

ConnectionStateUnionMember7Val: TypeAlias = Union[
    ConnectionStateUnionMember7ValUnionMember0,
    ConnectionStateUnionMember7ValUnionMember1,
    ConnectionStateUnionMember7ValUnionMember2,
    ConnectionStateUnionMember7ValUnionMember3,
]


class ConnectionStateUnionMember7(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["NO_AUTH"], PropertyInfo(alias="authScheme")]]

    val: Required[ConnectionStateUnionMember7Val]


class ConnectionStateUnionMember8ValUnionMember0Typed(TypedDict, total=False):
    status: Required[Literal["ACTIVE"]]

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


ConnectionStateUnionMember8ValUnionMember0: TypeAlias = Union[
    ConnectionStateUnionMember8ValUnionMember0Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember8ValUnionMember1Typed(TypedDict, total=False):
    status: Required[Literal["INACTIVE"]]

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


ConnectionStateUnionMember8ValUnionMember1: TypeAlias = Union[
    ConnectionStateUnionMember8ValUnionMember1Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember8ValUnionMember2Typed(TypedDict, total=False):
    status: Required[Literal["FAILED"]]

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


ConnectionStateUnionMember8ValUnionMember2: TypeAlias = Union[
    ConnectionStateUnionMember8ValUnionMember2Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember8ValUnionMember3Typed(TypedDict, total=False):
    status: Required[Literal["EXPIRED"]]

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


ConnectionStateUnionMember8ValUnionMember3: TypeAlias = Union[
    ConnectionStateUnionMember8ValUnionMember3Typed, Dict[str, Optional[object]]
]

ConnectionStateUnionMember8Val: TypeAlias = Union[
    ConnectionStateUnionMember8ValUnionMember0,
    ConnectionStateUnionMember8ValUnionMember1,
    ConnectionStateUnionMember8ValUnionMember2,
    ConnectionStateUnionMember8ValUnionMember3,
]


class ConnectionStateUnionMember8(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["CALCOM_AUTH"], PropertyInfo(alias="authScheme")]]

    val: Required[ConnectionStateUnionMember8Val]


class ConnectionStateUnionMember9ValUnionMember0Typed(TypedDict, total=False):
    status: Required[Literal["INITIALIZING"]]

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


ConnectionStateUnionMember9ValUnionMember0: TypeAlias = Union[
    ConnectionStateUnionMember9ValUnionMember0Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember9ValUnionMember1Typed(TypedDict, total=False):
    redirect_url: Required[Annotated[str, PropertyInfo(alias="redirectUrl")]]

    status: Required[Literal["INITIATED"]]

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


ConnectionStateUnionMember9ValUnionMember1: TypeAlias = Union[
    ConnectionStateUnionMember9ValUnionMember1Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember9ValUnionMember2Typed(TypedDict, total=False):
    dev_key: Required[Annotated[str, PropertyInfo(alias="devKey")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]

    status: Required[Literal["ACTIVE"]]

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


ConnectionStateUnionMember9ValUnionMember2: TypeAlias = Union[
    ConnectionStateUnionMember9ValUnionMember2Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember9ValUnionMember3Typed(TypedDict, total=False):
    dev_key: Required[Annotated[str, PropertyInfo(alias="devKey")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]

    status: Required[Literal["INACTIVE"]]

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


ConnectionStateUnionMember9ValUnionMember3: TypeAlias = Union[
    ConnectionStateUnionMember9ValUnionMember3Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember9ValUnionMember4Typed(TypedDict, total=False):
    status: Required[Literal["FAILED"]]

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


ConnectionStateUnionMember9ValUnionMember4: TypeAlias = Union[
    ConnectionStateUnionMember9ValUnionMember4Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember9ValUnionMember5Typed(TypedDict, total=False):
    status: Required[Literal["EXPIRED"]]

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


ConnectionStateUnionMember9ValUnionMember5: TypeAlias = Union[
    ConnectionStateUnionMember9ValUnionMember5Typed, Dict[str, Optional[object]]
]

ConnectionStateUnionMember9Val: TypeAlias = Union[
    ConnectionStateUnionMember9ValUnionMember0,
    ConnectionStateUnionMember9ValUnionMember1,
    ConnectionStateUnionMember9ValUnionMember2,
    ConnectionStateUnionMember9ValUnionMember3,
    ConnectionStateUnionMember9ValUnionMember4,
    ConnectionStateUnionMember9ValUnionMember5,
]


class ConnectionStateUnionMember9(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["BILLCOM_AUTH"], PropertyInfo(alias="authScheme")]]

    val: Required[ConnectionStateUnionMember9Val]


class ConnectionStateUnionMember10ValUnionMember0Typed(TypedDict, total=False):
    password: Required[str]

    status: Required[Literal["ACTIVE"]]

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


ConnectionStateUnionMember10ValUnionMember0: TypeAlias = Union[
    ConnectionStateUnionMember10ValUnionMember0Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember10ValUnionMember1Typed(TypedDict, total=False):
    password: Required[str]

    status: Required[Literal["INACTIVE"]]

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


ConnectionStateUnionMember10ValUnionMember1: TypeAlias = Union[
    ConnectionStateUnionMember10ValUnionMember1Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember10ValUnionMember2Typed(TypedDict, total=False):
    password: Required[str]

    status: Required[Literal["FAILED"]]

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


ConnectionStateUnionMember10ValUnionMember2: TypeAlias = Union[
    ConnectionStateUnionMember10ValUnionMember2Typed, Dict[str, Optional[object]]
]


class ConnectionStateUnionMember10ValUnionMember3Typed(TypedDict, total=False):
    password: Required[str]

    status: Required[Literal["EXPIRED"]]

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


ConnectionStateUnionMember10ValUnionMember3: TypeAlias = Union[
    ConnectionStateUnionMember10ValUnionMember3Typed, Dict[str, Optional[object]]
]

ConnectionStateUnionMember10Val: TypeAlias = Union[
    ConnectionStateUnionMember10ValUnionMember0,
    ConnectionStateUnionMember10ValUnionMember1,
    ConnectionStateUnionMember10ValUnionMember2,
    ConnectionStateUnionMember10ValUnionMember3,
]


class ConnectionStateUnionMember10(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["BASIC_WITH_JWT"], PropertyInfo(alias="authScheme")]]

    val: Required[ConnectionStateUnionMember10Val]


ConnectionState: TypeAlias = Union[
    ConnectionStateUnionMember0,
    ConnectionStateUnionMember1,
    ConnectionStateUnionMember2,
    ConnectionStateUnionMember3,
    ConnectionStateUnionMember4,
    ConnectionStateUnionMember5,
    ConnectionStateUnionMember6,
    ConnectionStateUnionMember7,
    ConnectionStateUnionMember8,
    ConnectionStateUnionMember9,
    ConnectionStateUnionMember10,
]


class Connection(TypedDict, total=False):
    callback_url: str
    """The URL to redirect to after connection completion"""

    state: ConnectionState
    """The state of the connected account"""

    user_id: str
    """The user id of the connected account"""
