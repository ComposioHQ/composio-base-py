# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ConnectedAccountListResponse",
    "Item",
    "ItemAuthConfig",
    "ItemAuthConfigDeprecated",
    "ItemState",
    "ItemStateUnionMember0",
    "ItemStateUnionMember0Val",
    "ItemStateUnionMember0ValUnionMember0",
    "ItemStateUnionMember0ValUnionMember1",
    "ItemStateUnionMember0ValUnionMember2",
    "ItemStateUnionMember0ValUnionMember3",
    "ItemStateUnionMember0ValUnionMember4",
    "ItemStateUnionMember0ValUnionMember5",
    "ItemStateUnionMember1",
    "ItemStateUnionMember1Val",
    "ItemStateUnionMember1ValUnionMember0",
    "ItemStateUnionMember1ValUnionMember1",
    "ItemStateUnionMember1ValUnionMember2",
    "ItemStateUnionMember1ValUnionMember2AuthedUser",
    "ItemStateUnionMember1ValUnionMember3",
    "ItemStateUnionMember1ValUnionMember3AuthedUser",
    "ItemStateUnionMember1ValUnionMember4",
    "ItemStateUnionMember1ValUnionMember5",
    "ItemStateUnionMember2",
    "ItemStateUnionMember2Val",
    "ItemStateUnionMember2ValUnionMember0",
    "ItemStateUnionMember2ValUnionMember1",
    "ItemStateUnionMember2ValUnionMember2",
    "ItemStateUnionMember2ValUnionMember3",
    "ItemStateUnionMember2ValUnionMember4",
    "ItemStateUnionMember2ValUnionMember5",
    "ItemStateUnionMember3",
    "ItemStateUnionMember3Val",
    "ItemStateUnionMember3ValUnionMember0",
    "ItemStateUnionMember3ValUnionMember1",
    "ItemStateUnionMember4",
    "ItemStateUnionMember4Val",
    "ItemStateUnionMember4ValUnionMember0",
    "ItemStateUnionMember4ValUnionMember1",
    "ItemStateUnionMember5",
    "ItemStateUnionMember5Val",
    "ItemStateUnionMember5ValUnionMember0",
    "ItemStateUnionMember5ValUnionMember1",
    "ItemStateUnionMember6",
    "ItemStateUnionMember6Val",
    "ItemStateUnionMember6ValUnionMember0",
    "ItemStateUnionMember6ValUnionMember1",
    "ItemStateUnionMember7",
    "ItemStateUnionMember7Val",
    "ItemStateUnionMember7ValUnionMember0",
    "ItemStateUnionMember7ValUnionMember1",
    "ItemStateUnionMember7ValUnionMember2",
    "ItemStateUnionMember7ValUnionMember3",
    "ItemStateUnionMember8",
    "ItemStateUnionMember8Val",
    "ItemStateUnionMember8ValUnionMember0",
    "ItemStateUnionMember8ValUnionMember1",
    "ItemStateUnionMember8ValUnionMember2",
    "ItemStateUnionMember8ValUnionMember3",
    "ItemStateUnionMember9",
    "ItemStateUnionMember9Val",
    "ItemStateUnionMember9ValUnionMember0",
    "ItemStateUnionMember9ValUnionMember1",
    "ItemStateUnionMember9ValUnionMember2",
    "ItemStateUnionMember9ValUnionMember3",
    "ItemStateUnionMember9ValUnionMember4",
    "ItemStateUnionMember9ValUnionMember5",
    "ItemStateUnionMember10",
    "ItemStateUnionMember10Val",
    "ItemStateUnionMember10ValUnionMember0",
    "ItemStateUnionMember10ValUnionMember1",
    "ItemStateUnionMember10ValUnionMember2",
    "ItemStateUnionMember10ValUnionMember3",
    "ItemToolkit",
    "ItemDeprecated",
]


class ItemAuthConfigDeprecated(BaseModel):
    uuid: str
    """The uuid of the auth config"""


class ItemAuthConfig(BaseModel):
    id: str
    """The id of the auth config"""

    is_composio_managed: bool
    """Whether the auth config is managed by Composio"""

    is_disabled: bool
    """Whether the auth config is disabled"""

    deprecated: Optional[ItemAuthConfigDeprecated] = None


class ItemStateUnionMember0ValUnionMember0(BaseModel):
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


class ItemStateUnionMember0ValUnionMember1(BaseModel):
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


class ItemStateUnionMember0ValUnionMember2(BaseModel):
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


class ItemStateUnionMember0ValUnionMember3(BaseModel):
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


class ItemStateUnionMember0ValUnionMember4(BaseModel):
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


class ItemStateUnionMember0ValUnionMember5(BaseModel):
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


ItemStateUnionMember0Val: TypeAlias = Union[
    ItemStateUnionMember0ValUnionMember0,
    ItemStateUnionMember0ValUnionMember1,
    ItemStateUnionMember0ValUnionMember2,
    ItemStateUnionMember0ValUnionMember3,
    ItemStateUnionMember0ValUnionMember4,
    ItemStateUnionMember0ValUnionMember5,
]


class ItemStateUnionMember0(BaseModel):
    auth_scheme: Literal["OAUTH1"] = FieldInfo(alias="authScheme")

    val: ItemStateUnionMember0Val


class ItemStateUnionMember1ValUnionMember0(BaseModel):
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


class ItemStateUnionMember1ValUnionMember1(BaseModel):
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


class ItemStateUnionMember1ValUnionMember2AuthedUser(BaseModel):
    access_token: Optional[str] = None

    scope: Optional[str] = None


class ItemStateUnionMember1ValUnionMember2(BaseModel):
    access_token: str

    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    authed_user: Optional[ItemStateUnionMember1ValUnionMember2AuthedUser] = None
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


class ItemStateUnionMember1ValUnionMember3AuthedUser(BaseModel):
    access_token: Optional[str] = None

    scope: Optional[str] = None


class ItemStateUnionMember1ValUnionMember3(BaseModel):
    access_token: str

    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    authed_user: Optional[ItemStateUnionMember1ValUnionMember3AuthedUser] = None
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


class ItemStateUnionMember1ValUnionMember4(BaseModel):
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


class ItemStateUnionMember1ValUnionMember5(BaseModel):
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


ItemStateUnionMember1Val: TypeAlias = Union[
    ItemStateUnionMember1ValUnionMember0,
    ItemStateUnionMember1ValUnionMember1,
    ItemStateUnionMember1ValUnionMember2,
    ItemStateUnionMember1ValUnionMember3,
    ItemStateUnionMember1ValUnionMember4,
    ItemStateUnionMember1ValUnionMember5,
]


class ItemStateUnionMember1(BaseModel):
    auth_scheme: Literal["OAUTH2"] = FieldInfo(alias="authScheme")

    val: ItemStateUnionMember1Val


class ItemStateUnionMember2ValUnionMember0(BaseModel):
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


class ItemStateUnionMember2ValUnionMember1(BaseModel):
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


class ItemStateUnionMember2ValUnionMember2(BaseModel):
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


class ItemStateUnionMember2ValUnionMember3(BaseModel):
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


class ItemStateUnionMember2ValUnionMember4(BaseModel):
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


class ItemStateUnionMember2ValUnionMember5(BaseModel):
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


ItemStateUnionMember2Val: TypeAlias = Union[
    ItemStateUnionMember2ValUnionMember0,
    ItemStateUnionMember2ValUnionMember1,
    ItemStateUnionMember2ValUnionMember2,
    ItemStateUnionMember2ValUnionMember3,
    ItemStateUnionMember2ValUnionMember4,
    ItemStateUnionMember2ValUnionMember5,
]


class ItemStateUnionMember2(BaseModel):
    auth_scheme: Literal["COMPOSIO_LINK"] = FieldInfo(alias="authScheme")

    val: ItemStateUnionMember2Val


class ItemStateUnionMember3ValUnionMember0(BaseModel):
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


class ItemStateUnionMember3ValUnionMember1(BaseModel):
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


ItemStateUnionMember3Val: TypeAlias = Union[ItemStateUnionMember3ValUnionMember0, ItemStateUnionMember3ValUnionMember1]


class ItemStateUnionMember3(BaseModel):
    auth_scheme: Literal["API_KEY"] = FieldInfo(alias="authScheme")

    val: ItemStateUnionMember3Val


class ItemStateUnionMember4ValUnionMember0(BaseModel):
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


class ItemStateUnionMember4ValUnionMember1(BaseModel):
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


ItemStateUnionMember4Val: TypeAlias = Union[ItemStateUnionMember4ValUnionMember0, ItemStateUnionMember4ValUnionMember1]


class ItemStateUnionMember4(BaseModel):
    auth_scheme: Literal["BASIC"] = FieldInfo(alias="authScheme")

    val: ItemStateUnionMember4Val


class ItemStateUnionMember5ValUnionMember0(BaseModel):
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


class ItemStateUnionMember5ValUnionMember1(BaseModel):
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


ItemStateUnionMember5Val: TypeAlias = Union[ItemStateUnionMember5ValUnionMember0, ItemStateUnionMember5ValUnionMember1]


class ItemStateUnionMember5(BaseModel):
    auth_scheme: Literal["BEARER_TOKEN"] = FieldInfo(alias="authScheme")

    val: ItemStateUnionMember5Val


class ItemStateUnionMember6ValUnionMember0(BaseModel):
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


class ItemStateUnionMember6ValUnionMember1(BaseModel):
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


ItemStateUnionMember6Val: TypeAlias = Union[ItemStateUnionMember6ValUnionMember0, ItemStateUnionMember6ValUnionMember1]


class ItemStateUnionMember6(BaseModel):
    auth_scheme: Literal["GOOGLE_SERVICE_ACCOUNT"] = FieldInfo(alias="authScheme")

    val: ItemStateUnionMember6Val


class ItemStateUnionMember7ValUnionMember0(BaseModel):
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


class ItemStateUnionMember7ValUnionMember1(BaseModel):
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


class ItemStateUnionMember7ValUnionMember2(BaseModel):
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


class ItemStateUnionMember7ValUnionMember3(BaseModel):
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


ItemStateUnionMember7Val: TypeAlias = Union[
    ItemStateUnionMember7ValUnionMember0,
    ItemStateUnionMember7ValUnionMember1,
    ItemStateUnionMember7ValUnionMember2,
    ItemStateUnionMember7ValUnionMember3,
]


class ItemStateUnionMember7(BaseModel):
    auth_scheme: Literal["NO_AUTH"] = FieldInfo(alias="authScheme")

    val: ItemStateUnionMember7Val


class ItemStateUnionMember8ValUnionMember0(BaseModel):
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


class ItemStateUnionMember8ValUnionMember1(BaseModel):
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


class ItemStateUnionMember8ValUnionMember2(BaseModel):
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


class ItemStateUnionMember8ValUnionMember3(BaseModel):
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


ItemStateUnionMember8Val: TypeAlias = Union[
    ItemStateUnionMember8ValUnionMember0,
    ItemStateUnionMember8ValUnionMember1,
    ItemStateUnionMember8ValUnionMember2,
    ItemStateUnionMember8ValUnionMember3,
]


class ItemStateUnionMember8(BaseModel):
    auth_scheme: Literal["CALCOM_AUTH"] = FieldInfo(alias="authScheme")

    val: ItemStateUnionMember8Val


class ItemStateUnionMember9ValUnionMember0(BaseModel):
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


class ItemStateUnionMember9ValUnionMember1(BaseModel):
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


class ItemStateUnionMember9ValUnionMember2(BaseModel):
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


class ItemStateUnionMember9ValUnionMember3(BaseModel):
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


class ItemStateUnionMember9ValUnionMember4(BaseModel):
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


class ItemStateUnionMember9ValUnionMember5(BaseModel):
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


ItemStateUnionMember9Val: TypeAlias = Union[
    ItemStateUnionMember9ValUnionMember0,
    ItemStateUnionMember9ValUnionMember1,
    ItemStateUnionMember9ValUnionMember2,
    ItemStateUnionMember9ValUnionMember3,
    ItemStateUnionMember9ValUnionMember4,
    ItemStateUnionMember9ValUnionMember5,
]


class ItemStateUnionMember9(BaseModel):
    auth_scheme: Literal["BILLCOM_AUTH"] = FieldInfo(alias="authScheme")

    val: ItemStateUnionMember9Val


class ItemStateUnionMember10ValUnionMember0(BaseModel):
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


class ItemStateUnionMember10ValUnionMember1(BaseModel):
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


class ItemStateUnionMember10ValUnionMember2(BaseModel):
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


class ItemStateUnionMember10ValUnionMember3(BaseModel):
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


ItemStateUnionMember10Val: TypeAlias = Union[
    ItemStateUnionMember10ValUnionMember0,
    ItemStateUnionMember10ValUnionMember1,
    ItemStateUnionMember10ValUnionMember2,
    ItemStateUnionMember10ValUnionMember3,
]


class ItemStateUnionMember10(BaseModel):
    auth_scheme: Literal["BASIC_WITH_JWT"] = FieldInfo(alias="authScheme")

    val: ItemStateUnionMember10Val


ItemState: TypeAlias = Union[
    ItemStateUnionMember0,
    ItemStateUnionMember1,
    ItemStateUnionMember2,
    ItemStateUnionMember3,
    ItemStateUnionMember4,
    ItemStateUnionMember5,
    ItemStateUnionMember6,
    ItemStateUnionMember7,
    ItemStateUnionMember8,
    ItemStateUnionMember9,
    ItemStateUnionMember10,
]


class ItemToolkit(BaseModel):
    slug: str
    """The slug of the toolkit"""


class ItemDeprecated(BaseModel):
    labels: List[str]
    """The labels of the connection"""

    uuid: str
    """The uuid of the connection"""


class Item(BaseModel):
    id: str
    """The id of the connection"""

    auth_config: ItemAuthConfig

    created_at: str
    """The created at of the connection"""

    is_disabled: bool
    """Whether the connection is disabled"""

    state: ItemState
    """The state of the connection"""

    status: Literal["INITIALIZING", "INITIATED", "ACTIVE", "FAILED", "EXPIRED", "INACTIVE"]
    """The status of the connection"""

    status_reason: Optional[str] = None
    """The reason the connection is disabled"""

    toolkit: ItemToolkit

    updated_at: str
    """The updated at of the connection"""

    deprecated: Optional[ItemDeprecated] = None

    test_request_endpoint: Optional[str] = None
    """The endpoint to make test request for verification"""


class ConnectedAccountListResponse(BaseModel):
    current_page: float

    items: List[Item]

    total_items: float

    total_pages: float

    next_cursor: Optional[str] = None
