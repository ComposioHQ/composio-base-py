# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ToolProxyParams",
    "CustomConnectionData",
    "CustomConnectionDataUnionMember0",
    "CustomConnectionDataUnionMember0Val",
    "CustomConnectionDataUnionMember0ValAuthedUser",
    "CustomConnectionDataUnionMember1",
    "CustomConnectionDataUnionMember1Val",
    "CustomConnectionDataUnionMember2",
    "CustomConnectionDataUnionMember2Val",
    "CustomConnectionDataUnionMember3",
    "CustomConnectionDataUnionMember3Val",
    "CustomConnectionDataUnionMember4",
    "CustomConnectionDataUnionMember4Val",
    "CustomConnectionDataUnionMember5",
    "CustomConnectionDataUnionMember5Val",
    "CustomConnectionDataUnionMember6",
    "CustomConnectionDataUnionMember6Val",
    "Parameter",
]


class ToolProxyParams(TypedDict, total=False):
    endpoint: Required[str]
    """
    The API endpoint to call (absolute URL or path relative to base URL of the
    connected account)
    """

    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD"]]
    """The HTTP method to use for the request"""

    body: object
    """The request body (for POST, PUT, and PATCH requests)"""

    connected_account_id: str
    """
    The ID of the connected account to use for authentication (if not provided, will
    use the default account for the project)
    """

    custom_connection_data: CustomConnectionData

    parameters: Iterable[Parameter]
    """Additional HTTP headers or query parameters to include in the request"""


class CustomConnectionDataUnionMember0ValAuthedUser(TypedDict, total=False):
    access_token: str

    scope: str


class CustomConnectionDataUnionMember0ValTyped(TypedDict, total=False):
    access_token: Required[str]

    account_id: str

    account_url: str

    api_url: str

    authed_user: CustomConnectionDataUnionMember0ValAuthedUser
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


CustomConnectionDataUnionMember0Val: TypeAlias = Union[
    CustomConnectionDataUnionMember0ValTyped, Dict[str, Optional[object]]
]


class CustomConnectionDataUnionMember0(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["OAUTH2"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember0Val]


class CustomConnectionDataUnionMember1ValTyped(TypedDict, total=False):
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


CustomConnectionDataUnionMember1Val: TypeAlias = Union[
    CustomConnectionDataUnionMember1ValTyped, Dict[str, Optional[object]]
]


class CustomConnectionDataUnionMember1(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["API_KEY"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember1Val]


class CustomConnectionDataUnionMember2ValTyped(TypedDict, total=False):
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


CustomConnectionDataUnionMember2Val: TypeAlias = Union[
    CustomConnectionDataUnionMember2ValTyped, Dict[str, Optional[object]]
]


class CustomConnectionDataUnionMember2(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["BASIC_WITH_JWT"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember2Val]


class CustomConnectionDataUnionMember3ValTyped(TypedDict, total=False):
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


CustomConnectionDataUnionMember3Val: TypeAlias = Union[
    CustomConnectionDataUnionMember3ValTyped, Dict[str, Optional[object]]
]


class CustomConnectionDataUnionMember3(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["BASIC"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember3Val]


class CustomConnectionDataUnionMember4ValTyped(TypedDict, total=False):
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


CustomConnectionDataUnionMember4Val: TypeAlias = Union[
    CustomConnectionDataUnionMember4ValTyped, Dict[str, Optional[object]]
]


class CustomConnectionDataUnionMember4(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["BEARER_TOKEN"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember4Val]


class CustomConnectionDataUnionMember5ValTyped(TypedDict, total=False):
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


CustomConnectionDataUnionMember5Val: TypeAlias = Union[
    CustomConnectionDataUnionMember5ValTyped, Dict[str, Optional[object]]
]


class CustomConnectionDataUnionMember5(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["OAUTH1"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember5Val]


class CustomConnectionDataUnionMember6ValTyped(TypedDict, total=False):
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


CustomConnectionDataUnionMember6Val: TypeAlias = Union[
    CustomConnectionDataUnionMember6ValTyped, Dict[str, Optional[object]]
]


class CustomConnectionDataUnionMember6(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["NO_AUTH"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember6Val]


CustomConnectionData: TypeAlias = Union[
    CustomConnectionDataUnionMember0,
    CustomConnectionDataUnionMember1,
    CustomConnectionDataUnionMember2,
    CustomConnectionDataUnionMember3,
    CustomConnectionDataUnionMember4,
    CustomConnectionDataUnionMember5,
    CustomConnectionDataUnionMember6,
]


class Parameter(TypedDict, total=False):
    name: Required[str]
    """Parameter name"""

    type: Required[Literal["header", "query"]]
    """Parameter type (header or query)"""

    value: Required[str]
    """Parameter value"""
