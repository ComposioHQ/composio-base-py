# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthConfigRetrieveResponse", "ToolAccessConfig", "Toolkit", "DeprecatedParams", "ProxyConfig"]


class ToolAccessConfig(BaseModel):
    tools_available_for_execution: Optional[List[str]] = None
    """The actions that the user can perform on the auth config.

    If passed, this will update the actions that the user can perform on the auth
    config.
    """

    tools_for_connected_account_creation: Optional[List[str]] = None
    """
    Tools used to generate the minimum required scopes for the auth config (only
    valid for OAuth). If passed, this will update the scopes.
    """


class Toolkit(BaseModel):
    """Information about the associated integration"""

    logo: str
    """The URL to the integration app's logo image"""

    slug: str
    """The unique identifier of the integration app"""


class DeprecatedParams(BaseModel):
    """DEPRECATED: This parameter will be removed in a future version."""

    default_connector_id: Optional[str] = None
    """Deprecated: Default connector ID"""

    expected_input_fields: Optional[List[Dict[str, Optional[object]]]] = None
    """Deprecated: Fields expected during connection initialization"""

    member_uuid: Optional[str] = None
    """Deprecated: Member UUID"""

    toolkit_id: Optional[str] = None
    """Deprecated: Toolkit ID"""


class ProxyConfig(BaseModel):
    proxy_url: str
    """The url of the auth proxy"""

    proxy_auth_key: Optional[str] = None
    """The auth key for the auth proxy"""


class AuthConfigRetrieveResponse(BaseModel):
    id: str
    """The unique ID of the authentication configuration"""

    name: str
    """The display name of the authentication configuration"""

    no_of_connections: float
    """The number of active connections using this auth config"""

    status: Literal["ENABLED", "DISABLED"]
    """Current status of the authentication configuration"""

    tool_access_config: ToolAccessConfig

    toolkit: Toolkit
    """Information about the associated integration"""

    type: Literal["default", "custom"]
    """The type of the authentication configuration (custom or default)"""

    uuid: str
    """The UUID of the authentication configuration (for backward compatibility)"""

    auth_scheme: Optional[
        Literal[
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
    ] = None
    """The authentication scheme used (e.g., OAuth2, API Key, etc.)"""

    created_at: Optional[str] = None
    """ISO 8601 date-time when the auth config was created"""

    created_by: Optional[str] = None
    """The identifier of the user who created the auth config"""

    credentials: Optional[Dict[str, Optional[object]]] = None
    """
    The authentication credentials (tokens, keys, etc.) - may be partially hidden
    for security
    """

    deprecated_params: Optional[DeprecatedParams] = None
    """DEPRECATED: This parameter will be removed in a future version."""

    expected_input_fields: Optional[List[Optional[object]]] = None
    """Fields expected during connection initialization"""

    is_composio_managed: Optional[bool] = None
    """Whether this authentication configuration is managed by Composio or the user"""

    last_updated_at: Optional[str] = None
    """ISO 8601 date-time when the auth config was last updated"""

    proxy_config: Optional[ProxyConfig] = None

    restrict_to_following_tools: Optional[List[str]] = None
    """Use tool_access_config instead. This field will be deprecated in the future."""

    shared_credentials: Optional[Dict[str, Optional[object]]] = None
    """
    [EXPERIMENTAL] Shared credentials that will be inherited by all connected
    accounts using this auth config
    """
