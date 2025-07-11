# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ConnectedAccountCreateResponse",
    "ConnectionData",
    "ConnectionDataUnionMember0",
    "ConnectionDataUnionMember0Val",
    "ConnectionDataUnionMember0ValUnionMember0",
    "ConnectionDataUnionMember0ValUnionMember1",
    "ConnectionDataUnionMember0ValUnionMember2",
    "ConnectionDataUnionMember0ValUnionMember3",
    "ConnectionDataUnionMember0ValUnionMember4",
    "ConnectionDataUnionMember0ValUnionMember5",
    "ConnectionDataUnionMember1",
    "ConnectionDataUnionMember1Val",
    "ConnectionDataUnionMember1ValUnionMember0",
    "ConnectionDataUnionMember1ValUnionMember1",
    "ConnectionDataUnionMember1ValUnionMember2",
    "ConnectionDataUnionMember1ValUnionMember2AuthedUser",
    "ConnectionDataUnionMember1ValUnionMember3",
    "ConnectionDataUnionMember1ValUnionMember3AuthedUser",
    "ConnectionDataUnionMember1ValUnionMember4",
    "ConnectionDataUnionMember1ValUnionMember5",
    "ConnectionDataUnionMember2",
    "ConnectionDataUnionMember2Val",
    "ConnectionDataUnionMember2ValUnionMember0",
    "ConnectionDataUnionMember2ValUnionMember1",
    "ConnectionDataUnionMember2ValUnionMember2",
    "ConnectionDataUnionMember2ValUnionMember3",
    "ConnectionDataUnionMember2ValUnionMember4",
    "ConnectionDataUnionMember2ValUnionMember5",
    "ConnectionDataUnionMember3",
    "ConnectionDataUnionMember3Val",
    "ConnectionDataUnionMember3ValUnionMember0",
    "ConnectionDataUnionMember3ValUnionMember1",
    "ConnectionDataUnionMember4",
    "ConnectionDataUnionMember4Val",
    "ConnectionDataUnionMember4ValUnionMember0",
    "ConnectionDataUnionMember4ValUnionMember1",
    "ConnectionDataUnionMember5",
    "ConnectionDataUnionMember5Val",
    "ConnectionDataUnionMember5ValUnionMember0",
    "ConnectionDataUnionMember5ValUnionMember1",
    "ConnectionDataUnionMember6",
    "ConnectionDataUnionMember6Val",
    "ConnectionDataUnionMember6ValUnionMember0",
    "ConnectionDataUnionMember6ValUnionMember1",
    "ConnectionDataUnionMember7",
    "ConnectionDataUnionMember7Val",
    "ConnectionDataUnionMember7ValUnionMember0",
    "ConnectionDataUnionMember7ValUnionMember1",
    "ConnectionDataUnionMember7ValUnionMember2",
    "ConnectionDataUnionMember7ValUnionMember3",
    "ConnectionDataUnionMember8",
    "ConnectionDataUnionMember8Val",
    "ConnectionDataUnionMember8ValUnionMember0",
    "ConnectionDataUnionMember8ValUnionMember1",
    "ConnectionDataUnionMember8ValUnionMember2",
    "ConnectionDataUnionMember8ValUnionMember3",
    "ConnectionDataUnionMember9",
    "ConnectionDataUnionMember9Val",
    "ConnectionDataUnionMember9ValUnionMember0",
    "ConnectionDataUnionMember9ValUnionMember1",
    "ConnectionDataUnionMember9ValUnionMember2",
    "ConnectionDataUnionMember9ValUnionMember3",
    "ConnectionDataUnionMember9ValUnionMember4",
    "ConnectionDataUnionMember9ValUnionMember5",
    "ConnectionDataUnionMember10",
    "ConnectionDataUnionMember10Val",
    "ConnectionDataUnionMember10ValUnionMember0",
    "ConnectionDataUnionMember10ValUnionMember1",
    "ConnectionDataUnionMember10ValUnionMember2",
    "ConnectionDataUnionMember10ValUnionMember3",
    "Deprecated",
]


class ConnectionDataUnionMember0ValUnionMember0(BaseModel):
    status: Literal["INITIALIZING"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember0ValUnionMember1(BaseModel):
    auth_uri: str = FieldInfo(alias="authUri")

    oauth_token: str

    oauth_token_secret: str

    redirect_url: str = FieldInfo(alias="redirectUrl")

    status: Literal["INITIATED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    callback_url: Optional[str] = FieldInfo(alias="callbackUrl", default=None)

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember0ValUnionMember2(BaseModel):
    oauth_token: str

    oauth_token_secret: str

    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    callback_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    consumer_key: Optional[str] = None

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    oauth_verifier: Optional[str] = None

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    redirect_url: Optional[str] = FieldInfo(alias="redirectUrl", default=None)

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember0ValUnionMember3(BaseModel):
    status: Literal["FAILED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    error: Optional[str] = None

    error_description: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember0ValUnionMember4(BaseModel):
    status: Literal["EXPIRED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    expired_at: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember0ValUnionMember5(BaseModel):
    oauth_token: str

    oauth_token_secret: str

    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    callback_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    consumer_key: Optional[str] = None

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    oauth_verifier: Optional[str] = None

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    redirect_url: Optional[str] = FieldInfo(alias="redirectUrl", default=None)

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


ConnectionDataUnionMember0Val: TypeAlias = Union[
    ConnectionDataUnionMember0ValUnionMember0,
    ConnectionDataUnionMember0ValUnionMember1,
    ConnectionDataUnionMember0ValUnionMember2,
    ConnectionDataUnionMember0ValUnionMember3,
    ConnectionDataUnionMember0ValUnionMember4,
    ConnectionDataUnionMember0ValUnionMember5,
]


class ConnectionDataUnionMember0(BaseModel):
    auth_scheme: Literal["OAUTH1"] = FieldInfo(alias="authScheme")

    val: ConnectionDataUnionMember0Val


class ConnectionDataUnionMember1ValUnionMember0(BaseModel):
    status: Literal["INITIALIZING"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    long_redirect_url: Optional[bool] = None
    """Whether to return the redirect url without shortening"""

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    state_prefix: Optional[str] = None
    """The oauth2 state prefix for the connection"""

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember1ValUnionMember1(BaseModel):
    redirect_url: str = FieldInfo(alias="redirectUrl")

    status: Literal["INITIATED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    callback_url: Optional[str] = None

    code_verifier: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    final_redirect_uri: Optional[str] = FieldInfo(alias="finalRedirectUri", default=None)

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    long_redirect_url: Optional[bool] = None
    """Whether to return the redirect url without shortening"""

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    state_prefix: Optional[str] = None
    """The oauth2 state prefix for the connection"""

    subdomain: Optional[str] = None

    version: Optional[str] = None

    webhook_signature: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember1ValUnionMember2AuthedUser(BaseModel):
    access_token: Optional[str] = None

    scope: Optional[str] = None


class ConnectionDataUnionMember1ValUnionMember2(BaseModel):
    access_token: str

    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    authed_user: Optional[ConnectionDataUnionMember1ValUnionMember2AuthedUser] = None
    """for slack user scopes"""

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    expires_in: Union[float, str, None] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    id_token: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    long_redirect_url: Optional[bool] = None
    """Whether to return the redirect url without shortening"""

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    refresh_token: Optional[str] = None

    region: Optional[str] = None

    scope: Union[str, List[str], None] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    state_prefix: Optional[str] = None
    """The oauth2 state prefix for the connection"""

    subdomain: Optional[str] = None

    token_type: Optional[str] = None

    version: Optional[str] = None

    webhook_signature: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember1ValUnionMember3AuthedUser(BaseModel):
    access_token: Optional[str] = None

    scope: Optional[str] = None


class ConnectionDataUnionMember1ValUnionMember3(BaseModel):
    access_token: str

    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    authed_user: Optional[ConnectionDataUnionMember1ValUnionMember3AuthedUser] = None
    """for slack user scopes"""

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    expires_in: Union[float, str, None] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    id_token: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    long_redirect_url: Optional[bool] = None
    """Whether to return the redirect url without shortening"""

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    refresh_token: Optional[str] = None

    region: Optional[str] = None

    scope: Union[str, List[str], None] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    state_prefix: Optional[str] = None
    """The oauth2 state prefix for the connection"""

    subdomain: Optional[str] = None

    token_type: Optional[str] = None

    version: Optional[str] = None

    webhook_signature: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember1ValUnionMember4(BaseModel):
    status: Literal["FAILED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    error: Optional[str] = None

    error_description: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    long_redirect_url: Optional[bool] = None
    """Whether to return the redirect url without shortening"""

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    state_prefix: Optional[str] = None
    """The oauth2 state prefix for the connection"""

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember1ValUnionMember5(BaseModel):
    status: Literal["EXPIRED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    expired_at: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    long_redirect_url: Optional[bool] = None
    """Whether to return the redirect url without shortening"""

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    state_prefix: Optional[str] = None
    """The oauth2 state prefix for the connection"""

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


ConnectionDataUnionMember1Val: TypeAlias = Union[
    ConnectionDataUnionMember1ValUnionMember0,
    ConnectionDataUnionMember1ValUnionMember1,
    ConnectionDataUnionMember1ValUnionMember2,
    ConnectionDataUnionMember1ValUnionMember3,
    ConnectionDataUnionMember1ValUnionMember4,
    ConnectionDataUnionMember1ValUnionMember5,
]


class ConnectionDataUnionMember1(BaseModel):
    auth_scheme: Literal["OAUTH2"] = FieldInfo(alias="authScheme")

    val: ConnectionDataUnionMember1Val


class ConnectionDataUnionMember2ValUnionMember0(BaseModel):
    status: Literal["INITIALIZING"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember2ValUnionMember1(BaseModel):
    redirect_url: str = FieldInfo(alias="redirectUrl")

    status: Literal["INITIATED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember2ValUnionMember2(BaseModel):
    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember2ValUnionMember3(BaseModel):
    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember2ValUnionMember4(BaseModel):
    status: Literal["FAILED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    error: Optional[str] = None

    error_description: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember2ValUnionMember5(BaseModel):
    status: Literal["EXPIRED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    expired_at: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


ConnectionDataUnionMember2Val: TypeAlias = Union[
    ConnectionDataUnionMember2ValUnionMember0,
    ConnectionDataUnionMember2ValUnionMember1,
    ConnectionDataUnionMember2ValUnionMember2,
    ConnectionDataUnionMember2ValUnionMember3,
    ConnectionDataUnionMember2ValUnionMember4,
    ConnectionDataUnionMember2ValUnionMember5,
]


class ConnectionDataUnionMember2(BaseModel):
    auth_scheme: Literal["COMPOSIO_LINK"] = FieldInfo(alias="authScheme")

    val: ConnectionDataUnionMember2Val


class ConnectionDataUnionMember3ValUnionMember0(BaseModel):
    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_key: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    basic_encoded: Optional[str] = None

    bearer_token: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    generic_api_key: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember3ValUnionMember1(BaseModel):
    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_key: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    basic_encoded: Optional[str] = None

    bearer_token: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    generic_api_key: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


ConnectionDataUnionMember3Val: TypeAlias = Union[
    ConnectionDataUnionMember3ValUnionMember0, ConnectionDataUnionMember3ValUnionMember1
]


class ConnectionDataUnionMember3(BaseModel):
    auth_scheme: Literal["API_KEY"] = FieldInfo(alias="authScheme")

    val: ConnectionDataUnionMember3Val


class ConnectionDataUnionMember4ValUnionMember0(BaseModel):
    password: str

    status: Literal["ACTIVE"]

    username: str

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember4ValUnionMember1(BaseModel):
    password: str

    status: Literal["INACTIVE"]

    username: str

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


ConnectionDataUnionMember4Val: TypeAlias = Union[
    ConnectionDataUnionMember4ValUnionMember0, ConnectionDataUnionMember4ValUnionMember1
]


class ConnectionDataUnionMember4(BaseModel):
    auth_scheme: Literal["BASIC"] = FieldInfo(alias="authScheme")

    val: ConnectionDataUnionMember4Val


class ConnectionDataUnionMember5ValUnionMember0(BaseModel):
    token: str

    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember5ValUnionMember1(BaseModel):
    token: str

    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


ConnectionDataUnionMember5Val: TypeAlias = Union[
    ConnectionDataUnionMember5ValUnionMember0, ConnectionDataUnionMember5ValUnionMember1
]


class ConnectionDataUnionMember5(BaseModel):
    auth_scheme: Literal["BEARER_TOKEN"] = FieldInfo(alias="authScheme")

    val: ConnectionDataUnionMember5Val


class ConnectionDataUnionMember6ValUnionMember0(BaseModel):
    credentials_json: str

    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember6ValUnionMember1(BaseModel):
    credentials_json: str

    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


ConnectionDataUnionMember6Val: TypeAlias = Union[
    ConnectionDataUnionMember6ValUnionMember0, ConnectionDataUnionMember6ValUnionMember1
]


class ConnectionDataUnionMember6(BaseModel):
    auth_scheme: Literal["GOOGLE_SERVICE_ACCOUNT"] = FieldInfo(alias="authScheme")

    val: ConnectionDataUnionMember6Val


class ConnectionDataUnionMember7ValUnionMember0(BaseModel):
    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember7ValUnionMember1(BaseModel):
    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember7ValUnionMember2(BaseModel):
    status: Literal["FAILED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    error: Optional[str] = None

    error_description: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember7ValUnionMember3(BaseModel):
    status: Literal["EXPIRED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    expired_at: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


ConnectionDataUnionMember7Val: TypeAlias = Union[
    ConnectionDataUnionMember7ValUnionMember0,
    ConnectionDataUnionMember7ValUnionMember1,
    ConnectionDataUnionMember7ValUnionMember2,
    ConnectionDataUnionMember7ValUnionMember3,
]


class ConnectionDataUnionMember7(BaseModel):
    auth_scheme: Literal["NO_AUTH"] = FieldInfo(alias="authScheme")

    val: ConnectionDataUnionMember7Val


class ConnectionDataUnionMember8ValUnionMember0(BaseModel):
    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember8ValUnionMember1(BaseModel):
    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember8ValUnionMember2(BaseModel):
    status: Literal["FAILED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    error: Optional[str] = None

    error_description: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember8ValUnionMember3(BaseModel):
    status: Literal["EXPIRED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    expired_at: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


ConnectionDataUnionMember8Val: TypeAlias = Union[
    ConnectionDataUnionMember8ValUnionMember0,
    ConnectionDataUnionMember8ValUnionMember1,
    ConnectionDataUnionMember8ValUnionMember2,
    ConnectionDataUnionMember8ValUnionMember3,
]


class ConnectionDataUnionMember8(BaseModel):
    auth_scheme: Literal["CALCOM_AUTH"] = FieldInfo(alias="authScheme")

    val: ConnectionDataUnionMember8Val


class ConnectionDataUnionMember9ValUnionMember0(BaseModel):
    status: Literal["INITIALIZING"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember9ValUnionMember1(BaseModel):
    redirect_url: str = FieldInfo(alias="redirectUrl")

    status: Literal["INITIATED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember9ValUnionMember2(BaseModel):
    dev_key: str = FieldInfo(alias="devKey")

    session_id: str = FieldInfo(alias="sessionId")

    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember9ValUnionMember3(BaseModel):
    dev_key: str = FieldInfo(alias="devKey")

    session_id: str = FieldInfo(alias="sessionId")

    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember9ValUnionMember4(BaseModel):
    status: Literal["FAILED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    error: Optional[str] = None

    error_description: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember9ValUnionMember5(BaseModel):
    status: Literal["EXPIRED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    expired_at: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


ConnectionDataUnionMember9Val: TypeAlias = Union[
    ConnectionDataUnionMember9ValUnionMember0,
    ConnectionDataUnionMember9ValUnionMember1,
    ConnectionDataUnionMember9ValUnionMember2,
    ConnectionDataUnionMember9ValUnionMember3,
    ConnectionDataUnionMember9ValUnionMember4,
    ConnectionDataUnionMember9ValUnionMember5,
]


class ConnectionDataUnionMember9(BaseModel):
    auth_scheme: Literal["BILLCOM_AUTH"] = FieldInfo(alias="authScheme")

    val: ConnectionDataUnionMember9Val


class ConnectionDataUnionMember10ValUnionMember0(BaseModel):
    password: str

    status: Literal["ACTIVE"]

    username: str

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember10ValUnionMember1(BaseModel):
    password: str

    status: Literal["INACTIVE"]

    username: str

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember10ValUnionMember2(BaseModel):
    password: str

    status: Literal["FAILED"]

    username: str

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    error: Optional[str] = None

    error_description: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class ConnectionDataUnionMember10ValUnionMember3(BaseModel):
    password: str

    status: Literal["EXPIRED"]

    username: str

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    dc: Optional[str] = None

    domain: Optional[str] = None

    expired_at: Optional[str] = None

    extension: Optional[str] = None

    form_api_base_url: Optional[str] = None

    instance_endpoint: Optional[str] = FieldInfo(alias="instanceEndpoint", default=None)

    instance_name: Optional[str] = FieldInfo(alias="instanceName", default=None)

    proxy_password: Optional[str] = None

    proxy_username: Optional[str] = None

    region: Optional[str] = None

    server_location: Optional[str] = None

    shop: Optional[str] = None

    site_name: Optional[str] = None

    subdomain: Optional[str] = None

    version: Optional[str] = None

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


ConnectionDataUnionMember10Val: TypeAlias = Union[
    ConnectionDataUnionMember10ValUnionMember0,
    ConnectionDataUnionMember10ValUnionMember1,
    ConnectionDataUnionMember10ValUnionMember2,
    ConnectionDataUnionMember10ValUnionMember3,
]


class ConnectionDataUnionMember10(BaseModel):
    auth_scheme: Literal["BASIC_WITH_JWT"] = FieldInfo(alias="authScheme")

    val: ConnectionDataUnionMember10Val


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
]


class Deprecated(BaseModel):
    auth_config_uuid: str = FieldInfo(alias="authConfigUuid")
    """The uuid of the auth config"""

    uuid: str
    """The uuid of the connected account"""


class ConnectedAccountCreateResponse(BaseModel):
    id: str
    """The id of the connected account"""

    connection_data: ConnectionData = FieldInfo(alias="connectionData")
    """The connection data of the connected account"""

    deprecated: Deprecated
