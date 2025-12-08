# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ConnectedAccountRetrieveResponse",
    "AuthConfig",
    "AuthConfigDeprecated",
    "State",
    "StateUnionMember0",
    "StateUnionMember0Val",
    "StateUnionMember0ValUnionMember0",
    "StateUnionMember0ValUnionMember1",
    "StateUnionMember0ValUnionMember2",
    "StateUnionMember0ValUnionMember3",
    "StateUnionMember0ValUnionMember4",
    "StateUnionMember0ValUnionMember5",
    "StateUnionMember1",
    "StateUnionMember1Val",
    "StateUnionMember1ValUnionMember0",
    "StateUnionMember1ValUnionMember1",
    "StateUnionMember1ValUnionMember2",
    "StateUnionMember1ValUnionMember2AuthedUser",
    "StateUnionMember1ValUnionMember3",
    "StateUnionMember1ValUnionMember3AuthedUser",
    "StateUnionMember1ValUnionMember4",
    "StateUnionMember1ValUnionMember5",
    "StateUnionMember2",
    "StateUnionMember2Val",
    "StateUnionMember2ValUnionMember0",
    "StateUnionMember2ValUnionMember1",
    "StateUnionMember2ValUnionMember2",
    "StateUnionMember2ValUnionMember3",
    "StateUnionMember3",
    "StateUnionMember3Val",
    "StateUnionMember3ValUnionMember0",
    "StateUnionMember3ValUnionMember1",
    "StateUnionMember3ValUnionMember2",
    "StateUnionMember3ValUnionMember3",
    "StateUnionMember4",
    "StateUnionMember4Val",
    "StateUnionMember4ValUnionMember0",
    "StateUnionMember4ValUnionMember1",
    "StateUnionMember4ValUnionMember2",
    "StateUnionMember4ValUnionMember3",
    "StateUnionMember5",
    "StateUnionMember5Val",
    "StateUnionMember5ValUnionMember0",
    "StateUnionMember5ValUnionMember1",
    "StateUnionMember5ValUnionMember2",
    "StateUnionMember5ValUnionMember3",
    "StateUnionMember6",
    "StateUnionMember6Val",
    "StateUnionMember6ValUnionMember0",
    "StateUnionMember6ValUnionMember1",
    "StateUnionMember6ValUnionMember2",
    "StateUnionMember6ValUnionMember3",
    "StateUnionMember6ValUnionMember4",
    "StateUnionMember6ValUnionMember5",
    "StateUnionMember7",
    "StateUnionMember7Val",
    "StateUnionMember7ValUnionMember0",
    "StateUnionMember7ValUnionMember1",
    "StateUnionMember7ValUnionMember2",
    "StateUnionMember7ValUnionMember3",
    "StateUnionMember7ValUnionMember4",
    "StateUnionMember7ValUnionMember5",
    "StateUnionMember8",
    "StateUnionMember8Val",
    "StateUnionMember8ValUnionMember0",
    "StateUnionMember8ValUnionMember1",
    "StateUnionMember8ValUnionMember2",
    "StateUnionMember8ValUnionMember3",
    "StateUnionMember8ValUnionMember4",
    "StateUnionMember8ValUnionMember5",
    "StateUnionMember9",
    "StateUnionMember9Val",
    "StateUnionMember9ValUnionMember0",
    "StateUnionMember9ValUnionMember1",
    "StateUnionMember9ValUnionMember2",
    "StateUnionMember9ValUnionMember3",
    "StateUnionMember9ValUnionMember4",
    "StateUnionMember9ValUnionMember5",
    "StateUnionMember10",
    "StateUnionMember10Val",
    "StateUnionMember10ValUnionMember0",
    "StateUnionMember10ValUnionMember1",
    "StateUnionMember10ValUnionMember2",
    "StateUnionMember10ValUnionMember3",
    "StateUnionMember11",
    "StateUnionMember11Val",
    "StateUnionMember11ValUnionMember0",
    "StateUnionMember11ValUnionMember1",
    "StateUnionMember11ValUnionMember2",
    "StateUnionMember11ValUnionMember3",
    "StateUnionMember11ValUnionMember4",
    "StateUnionMember11ValUnionMember5",
    "StateUnionMember12",
    "StateUnionMember12Val",
    "StateUnionMember12ValUnionMember0",
    "StateUnionMember12ValUnionMember1",
    "StateUnionMember12ValUnionMember2",
    "StateUnionMember12ValUnionMember3",
    "StateUnionMember12ValUnionMember4",
    "StateUnionMember12ValUnionMember5",
    "Toolkit",
    "Deprecated",
]


class AuthConfigDeprecated(BaseModel):
    uuid: str
    """The uuid of the auth config"""


class AuthConfig(BaseModel):
    id: str
    """The id of the auth config"""

    auth_scheme: Literal[
        "OAUTH2",
        "OAUTH1",
        "API_KEY",
        "BASIC",
        "BILLCOM_AUTH",
        "BEARER_TOKEN",
        "GOOGLE_SERVICE_ACCOUNT",
        "NO_AUTH",
        "BASIC_WITH_JWT",
        "CALCOM_AUTH",
        "SERVICE_ACCOUNT",
        "SAML",
        "DCR_OAUTH",
    ]
    """the authScheme is part of the connection state use it there"""

    is_composio_managed: bool
    """Whether the auth config is managed by Composio"""

    is_disabled: bool
    """Whether the auth config is disabled"""

    deprecated: Optional[AuthConfigDeprecated] = None


class StateUnionMember0ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember0ValUnionMember1(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember0ValUnionMember2(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember0ValUnionMember3(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember0ValUnionMember4(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember0ValUnionMember5(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember0Val: TypeAlias = Union[
    StateUnionMember0ValUnionMember0,
    StateUnionMember0ValUnionMember1,
    StateUnionMember0ValUnionMember2,
    StateUnionMember0ValUnionMember3,
    StateUnionMember0ValUnionMember4,
    StateUnionMember0ValUnionMember5,
]


class StateUnionMember0(BaseModel):
    auth_scheme: Literal["OAUTH1"] = FieldInfo(alias="authScheme")

    val: StateUnionMember0Val


class StateUnionMember1ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember1ValUnionMember1(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember1ValUnionMember2AuthedUser(BaseModel):
    """for slack user scopes"""

    access_token: Optional[str] = None

    scope: Optional[str] = None


class StateUnionMember1ValUnionMember2(BaseModel):
    access_token: str

    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    authed_user: Optional[StateUnionMember1ValUnionMember2AuthedUser] = None
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember1ValUnionMember3AuthedUser(BaseModel):
    """for slack user scopes"""

    access_token: Optional[str] = None

    scope: Optional[str] = None


class StateUnionMember1ValUnionMember3(BaseModel):
    access_token: str

    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    authed_user: Optional[StateUnionMember1ValUnionMember3AuthedUser] = None
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember1ValUnionMember4(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember1ValUnionMember5(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember1Val: TypeAlias = Union[
    StateUnionMember1ValUnionMember0,
    StateUnionMember1ValUnionMember1,
    StateUnionMember1ValUnionMember2,
    StateUnionMember1ValUnionMember3,
    StateUnionMember1ValUnionMember4,
    StateUnionMember1ValUnionMember5,
]


class StateUnionMember1(BaseModel):
    auth_scheme: Literal["OAUTH2"] = FieldInfo(alias="authScheme")

    val: StateUnionMember1Val


class StateUnionMember2ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember2ValUnionMember1(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember2ValUnionMember2(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember2ValUnionMember3(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember2Val: TypeAlias = Union[
    StateUnionMember2ValUnionMember0,
    StateUnionMember2ValUnionMember1,
    StateUnionMember2ValUnionMember2,
    StateUnionMember2ValUnionMember3,
]


class StateUnionMember2(BaseModel):
    auth_scheme: Literal["API_KEY"] = FieldInfo(alias="authScheme")

    val: StateUnionMember2Val


class StateUnionMember3ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember3ValUnionMember1(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember3ValUnionMember2(BaseModel):
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

    password: Optional[str] = None

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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember3ValUnionMember3(BaseModel):
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

    password: Optional[str] = None

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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember3Val: TypeAlias = Union[
    StateUnionMember3ValUnionMember0,
    StateUnionMember3ValUnionMember1,
    StateUnionMember3ValUnionMember2,
    StateUnionMember3ValUnionMember3,
]


class StateUnionMember3(BaseModel):
    auth_scheme: Literal["BASIC"] = FieldInfo(alias="authScheme")

    val: StateUnionMember3Val


class StateUnionMember4ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember4ValUnionMember1(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember4ValUnionMember2(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember4ValUnionMember3(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember4Val: TypeAlias = Union[
    StateUnionMember4ValUnionMember0,
    StateUnionMember4ValUnionMember1,
    StateUnionMember4ValUnionMember2,
    StateUnionMember4ValUnionMember3,
]


class StateUnionMember4(BaseModel):
    auth_scheme: Literal["BEARER_TOKEN"] = FieldInfo(alias="authScheme")

    val: StateUnionMember4Val


class StateUnionMember5ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember5ValUnionMember1(BaseModel):
    redirect_url: str = FieldInfo(alias="redirectUrl")

    status: Literal["INITIATED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    companydomain: Optional[str] = FieldInfo(alias="COMPANYDOMAIN", default=None)

    composio_link_redirect_url: Optional[str] = None

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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember5ValUnionMember2(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember5ValUnionMember3(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember5Val: TypeAlias = Union[
    StateUnionMember5ValUnionMember0,
    StateUnionMember5ValUnionMember1,
    StateUnionMember5ValUnionMember2,
    StateUnionMember5ValUnionMember3,
]


class StateUnionMember5(BaseModel):
    auth_scheme: Literal["GOOGLE_SERVICE_ACCOUNT"] = FieldInfo(alias="authScheme")

    val: StateUnionMember5Val


class StateUnionMember6ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember6ValUnionMember1(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember6ValUnionMember2(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember6ValUnionMember3(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember6ValUnionMember4(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember6ValUnionMember5(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember6Val: TypeAlias = Union[
    StateUnionMember6ValUnionMember0,
    StateUnionMember6ValUnionMember1,
    StateUnionMember6ValUnionMember2,
    StateUnionMember6ValUnionMember3,
    StateUnionMember6ValUnionMember4,
    StateUnionMember6ValUnionMember5,
]


class StateUnionMember6(BaseModel):
    auth_scheme: Literal["NO_AUTH"] = FieldInfo(alias="authScheme")

    val: StateUnionMember6Val


class StateUnionMember7ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember7ValUnionMember1(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember7ValUnionMember2(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember7ValUnionMember3(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember7ValUnionMember4(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember7ValUnionMember5(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember7Val: TypeAlias = Union[
    StateUnionMember7ValUnionMember0,
    StateUnionMember7ValUnionMember1,
    StateUnionMember7ValUnionMember2,
    StateUnionMember7ValUnionMember3,
    StateUnionMember7ValUnionMember4,
    StateUnionMember7ValUnionMember5,
]


class StateUnionMember7(BaseModel):
    auth_scheme: Literal["CALCOM_AUTH"] = FieldInfo(alias="authScheme")

    val: StateUnionMember7Val


class StateUnionMember8ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember8ValUnionMember1(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember8ValUnionMember2(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember8ValUnionMember3(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember8ValUnionMember4(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember8ValUnionMember5(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember8Val: TypeAlias = Union[
    StateUnionMember8ValUnionMember0,
    StateUnionMember8ValUnionMember1,
    StateUnionMember8ValUnionMember2,
    StateUnionMember8ValUnionMember3,
    StateUnionMember8ValUnionMember4,
    StateUnionMember8ValUnionMember5,
]


class StateUnionMember8(BaseModel):
    auth_scheme: Literal["BILLCOM_AUTH"] = FieldInfo(alias="authScheme")

    val: StateUnionMember8Val


class StateUnionMember9ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember9ValUnionMember1(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember9ValUnionMember2(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember9ValUnionMember3(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember9ValUnionMember4(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember9ValUnionMember5(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember9Val: TypeAlias = Union[
    StateUnionMember9ValUnionMember0,
    StateUnionMember9ValUnionMember1,
    StateUnionMember9ValUnionMember2,
    StateUnionMember9ValUnionMember3,
    StateUnionMember9ValUnionMember4,
    StateUnionMember9ValUnionMember5,
]


class StateUnionMember9(BaseModel):
    auth_scheme: Literal["BASIC_WITH_JWT"] = FieldInfo(alias="authScheme")

    val: StateUnionMember9Val


class StateUnionMember10ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember10ValUnionMember1(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember10ValUnionMember2(BaseModel):
    application_id: str

    installation_id: str

    private_key: str

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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember10ValUnionMember3(BaseModel):
    application_id: str

    installation_id: str

    private_key: str

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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember10Val: TypeAlias = Union[
    StateUnionMember10ValUnionMember0,
    StateUnionMember10ValUnionMember1,
    StateUnionMember10ValUnionMember2,
    StateUnionMember10ValUnionMember3,
]


class StateUnionMember10(BaseModel):
    auth_scheme: Literal["SERVICE_ACCOUNT"] = FieldInfo(alias="authScheme")

    val: StateUnionMember10Val


class StateUnionMember11ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember11ValUnionMember1(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember11ValUnionMember2(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember11ValUnionMember3(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember11ValUnionMember4(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember11ValUnionMember5(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember11Val: TypeAlias = Union[
    StateUnionMember11ValUnionMember0,
    StateUnionMember11ValUnionMember1,
    StateUnionMember11ValUnionMember2,
    StateUnionMember11ValUnionMember3,
    StateUnionMember11ValUnionMember4,
    StateUnionMember11ValUnionMember5,
]


class StateUnionMember11(BaseModel):
    auth_scheme: Literal["SAML"] = FieldInfo(alias="authScheme")

    val: StateUnionMember11Val


class StateUnionMember12ValUnionMember0(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember12ValUnionMember1(BaseModel):
    client_id: str
    """Dynamically registered client ID"""

    redirect_url: str = FieldInfo(alias="redirectUrl")

    status: Literal["INITIATED"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    callback_url: Optional[str] = None

    client_id_issued_at: Optional[float] = None

    client_secret: Optional[str] = None
    """Dynamically registered client secret"""

    client_secret_expires_at: Optional[float] = None

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

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember12ValUnionMember2(BaseModel):
    access_token: str

    client_id: str
    """Dynamically registered client ID"""

    status: Literal["ACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    client_id_issued_at: Optional[float] = None

    client_secret: Optional[str] = None
    """Dynamically registered client secret"""

    client_secret_expires_at: Optional[float] = None

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

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember12ValUnionMember3(BaseModel):
    access_token: str

    client_id: str
    """Dynamically registered client ID"""

    status: Literal["INACTIVE"]

    account_id: Optional[str] = None

    account_url: Optional[str] = None

    api_url: Optional[str] = None

    base_url: Optional[str] = None

    borneo_dashboard_url: Optional[str] = None

    client_id_issued_at: Optional[float] = None

    client_secret: Optional[str] = None
    """Dynamically registered client secret"""

    client_secret_expires_at: Optional[float] = None

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

    your_server: Optional[str] = None

    your_domain: Optional[str] = FieldInfo(alias="your-domain", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember12ValUnionMember4(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class StateUnionMember12ValUnionMember5(BaseModel):
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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


StateUnionMember12Val: TypeAlias = Union[
    StateUnionMember12ValUnionMember0,
    StateUnionMember12ValUnionMember1,
    StateUnionMember12ValUnionMember2,
    StateUnionMember12ValUnionMember3,
    StateUnionMember12ValUnionMember4,
    StateUnionMember12ValUnionMember5,
]


class StateUnionMember12(BaseModel):
    auth_scheme: Literal["DCR_OAUTH"] = FieldInfo(alias="authScheme")

    val: StateUnionMember12Val


State: TypeAlias = Union[
    StateUnionMember0,
    StateUnionMember1,
    StateUnionMember2,
    StateUnionMember3,
    StateUnionMember4,
    StateUnionMember5,
    StateUnionMember6,
    StateUnionMember7,
    StateUnionMember8,
    StateUnionMember9,
    StateUnionMember10,
    StateUnionMember11,
    StateUnionMember12,
]


class Toolkit(BaseModel):
    slug: str
    """The slug of the toolkit"""


class Deprecated(BaseModel):
    labels: List[str]
    """The labels of the connection"""

    uuid: str
    """The uuid of the connection"""


class ConnectedAccountRetrieveResponse(BaseModel):
    id: str
    """The id of the connection"""

    auth_config: AuthConfig

    created_at: str
    """The created at of the connection"""

    data: Dict[str, Optional[object]]
    """This is deprecated, use `state` instead"""

    is_disabled: bool
    """Whether the connection is disabled"""

    params: Dict[str, Optional[object]]
    """The initialization data of the connection, including configuration parameters"""

    state: State
    """The state of the connection"""

    status: Literal["INITIALIZING", "INITIATED", "ACTIVE", "FAILED", "EXPIRED", "INACTIVE"]
    """The status of the connection"""

    status_reason: Optional[str] = None
    """The reason the connection is disabled"""

    toolkit: Toolkit

    updated_at: str
    """The updated at of the connection"""

    user_id: str
    """
    This is deprecated, we will not be providing userId from this api anymore, you
    will only be able to read via userId not get it back
    """

    deprecated: Optional[Deprecated] = None

    test_request_endpoint: Optional[str] = None
    """The endpoint to make test request for verification"""
