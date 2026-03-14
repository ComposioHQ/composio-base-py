# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "ToolExecuteParams",
    "CustomAuthParams",
    "CustomAuthParamsParameter",
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
    "CustomConnectionDataUnionMember7",
    "CustomConnectionDataUnionMember7Val",
    "CustomConnectionDataUnionMember8",
    "CustomConnectionDataUnionMember8Val",
    "CustomConnectionDataUnionMember9",
    "CustomConnectionDataUnionMember9Val",
    "CustomConnectionDataUnionMember10",
    "CustomConnectionDataUnionMember10Val",
]


class ToolExecuteParams(TypedDict, total=False):
    allow_tracing: Optional[bool]
    """Deprecated. Enable debug tracing for tool execution (useful for debugging)"""

    arguments: Dict[str, Optional[object]]
    """
    Key-value pairs of arguments required by the tool (mutually exclusive with text)
    """

    connected_account_id: str
    """Unique identifier for the connected account to use for authentication"""

    custom_auth_params: CustomAuthParams
    """
    Custom authentication parameters for tools that support parameterized
    authentication
    """

    custom_connection_data: CustomConnectionData
    """Custom connection data for tools that support custom connection data"""

    entity_id: str
    """Deprecated: please use user_id instead.

    Entity identifier for multi-entity connected accounts (e.g. multiple
    repositories, organizations)
    """

    text: str
    """
    Natural language description of the task to perform (mutually exclusive with
    arguments)
    """

    user_id: str
    """User id for multi-user connected accounts (e.g. multiple users, organizations)"""

    version: str
    """Tool version to execute (defaults to "00000000_00" if not specified)"""

    x_llm_gateway_headers: Annotated[str, PropertyInfo(alias="x-llm-gateway-headers")]
    """
    JSON object containing custom headers to pass to LLM providers (OpenAI, Bedrock,
    etc.)
    """


_CustomAuthParamsParameterReservedKeywords = TypedDict(
    "_CustomAuthParamsParameterReservedKeywords",
    {
        "in": Literal["query", "header"],
    },
    total=False,
)


class CustomAuthParamsParameter(_CustomAuthParamsParameterReservedKeywords, total=False):
    name: Required[str]
    """The name of the parameter. For example, 'x-api-key', 'Content-Type', etc."""

    value: Required[Union[str, float]]
    """The value of the parameter. For example, '1234567890', 'application/json', etc."""


class CustomAuthParams(TypedDict, total=False):
    """
    Custom authentication parameters for tools that support parameterized authentication
    """

    base_url: str
    """
    The base URL (root address) what you should use while making http requests to
    the connected account. For example, for gmail, it would be
    'https://gmail.googleapis.com'
    """

    body: Dict[str, Optional[object]]
    """The body to be sent to the endpoint for authentication.

    This is a JSON object. Note: This is very rarely needed and is only required by
    very few apps.
    """

    parameters: Iterable[CustomAuthParamsParameter]


class CustomConnectionDataUnionMember0ValAuthedUser(TypedDict, total=False):
    """for slack user scopes"""

    access_token: str

    scope: str


class CustomConnectionDataUnionMember0Val(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
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


class CustomConnectionDataUnionMember0(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["OAUTH2"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember0Val]


class CustomConnectionDataUnionMember1Val(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
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


class CustomConnectionDataUnionMember1(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["DCR_OAUTH"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember1Val]


class CustomConnectionDataUnionMember2Val(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
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


class CustomConnectionDataUnionMember2(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["API_KEY"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember2Val]


class CustomConnectionDataUnionMember3Val(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
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


class CustomConnectionDataUnionMember3(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["BASIC_WITH_JWT"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember3Val]


class CustomConnectionDataUnionMember4Val(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
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


class CustomConnectionDataUnionMember4(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["BASIC"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember4Val]


class CustomConnectionDataUnionMember5Val(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
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


class CustomConnectionDataUnionMember5(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["BEARER_TOKEN"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember5Val]


class CustomConnectionDataUnionMember6Val(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
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


class CustomConnectionDataUnionMember6(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["OAUTH1"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember6Val]


class CustomConnectionDataUnionMember7Val(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
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


class CustomConnectionDataUnionMember7(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["NO_AUTH"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember7Val]


class CustomConnectionDataUnionMember8Val(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
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


class CustomConnectionDataUnionMember8(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["SERVICE_ACCOUNT"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember8Val]


class CustomConnectionDataUnionMember9Val(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
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


class CustomConnectionDataUnionMember9(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["GOOGLE_SERVICE_ACCOUNT"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember9Val]


class CustomConnectionDataUnionMember10Val(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
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


class CustomConnectionDataUnionMember10(TypedDict, total=False):
    auth_scheme: Required[Annotated[Literal["S2S_OAUTH2"], PropertyInfo(alias="authScheme")]]

    toolkit_slug: Required[Annotated[str, PropertyInfo(alias="toolkitSlug")]]

    val: Required[CustomConnectionDataUnionMember10Val]


CustomConnectionData: TypeAlias = Union[
    CustomConnectionDataUnionMember0,
    CustomConnectionDataUnionMember1,
    CustomConnectionDataUnionMember2,
    CustomConnectionDataUnionMember3,
    CustomConnectionDataUnionMember4,
    CustomConnectionDataUnionMember5,
    CustomConnectionDataUnionMember6,
    CustomConnectionDataUnionMember7,
    CustomConnectionDataUnionMember8,
    CustomConnectionDataUnionMember9,
    CustomConnectionDataUnionMember10,
]
