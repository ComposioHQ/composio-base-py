# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ToolkitRetrieveResponse",
    "Deprecated",
    "Meta",
    "MetaCategory",
    "AuthConfigDetail",
    "AuthConfigDetailFields",
    "AuthConfigDetailFieldsAuthConfigCreation",
    "AuthConfigDetailFieldsAuthConfigCreationOptional",
    "AuthConfigDetailFieldsAuthConfigCreationRequired",
    "AuthConfigDetailFieldsConnectedAccountInitiation",
    "AuthConfigDetailFieldsConnectedAccountInitiationOptional",
    "AuthConfigDetailFieldsConnectedAccountInitiationRequired",
    "AuthConfigDetailDeprecatedAuthProviderDetails",
    "AuthConfigDetailProxy",
]


class Deprecated(BaseModel):
    raw_proxy_info_by_auth_schemes: List[Dict[str, Optional[object]]] = FieldInfo(alias="rawProxyInfoByAuthSchemes")

    toolkit_id: str = FieldInfo(alias="toolkitId")

    get_current_user_endpoint: Optional[str] = FieldInfo(alias="getCurrentUserEndpoint", default=None)


class MetaCategory(BaseModel):
    name: str
    """Human-readable category name"""

    slug: str
    """URL-friendly identifier for the category"""


class Meta(BaseModel):
    """
    Comprehensive metadata for the toolkit including dates, descriptions, and statistics
    """

    available_versions: List[str]
    """Available versions of the toolkit"""

    categories: List[MetaCategory]
    """List of categories associated with this toolkit"""

    created_at: str
    """Creation date and time of the toolkit"""

    description: str
    """Human-readable description explaining the toolkit's purpose and functionality"""

    logo: str
    """Image URL for the toolkit's branding"""

    tools_count: float
    """Count of available tools in this toolkit"""

    triggers_count: float
    """Count of available triggers in this toolkit"""

    updated_at: str
    """Last modification date and time of the toolkit"""

    version: str
    """Version of the toolkit"""

    app_url: Optional[str] = None
    """Link to the toolkit's main application or service website"""


class AuthConfigDetailFieldsAuthConfigCreationOptional(BaseModel):
    description: str

    display_name: str = FieldInfo(alias="displayName")

    name: str

    required: bool

    type: str

    default: Optional[str] = None

    legacy_template_name: Optional[str] = None


class AuthConfigDetailFieldsAuthConfigCreationRequired(BaseModel):
    description: str

    display_name: str = FieldInfo(alias="displayName")

    name: str

    required: bool

    type: str

    default: Optional[str] = None

    legacy_template_name: Optional[str] = None


class AuthConfigDetailFieldsAuthConfigCreation(BaseModel):
    """Form fields needed when creating an authentication configuration"""

    optional: List[AuthConfigDetailFieldsAuthConfigCreationOptional]

    required: List[AuthConfigDetailFieldsAuthConfigCreationRequired]


class AuthConfigDetailFieldsConnectedAccountInitiationOptional(BaseModel):
    description: str

    display_name: str = FieldInfo(alias="displayName")

    name: str

    required: bool

    type: str

    default: Optional[str] = None

    legacy_template_name: Optional[str] = None


class AuthConfigDetailFieldsConnectedAccountInitiationRequired(BaseModel):
    description: str

    display_name: str = FieldInfo(alias="displayName")

    name: str

    required: bool

    type: str

    default: Optional[str] = None

    legacy_template_name: Optional[str] = None


class AuthConfigDetailFieldsConnectedAccountInitiation(BaseModel):
    """
    Form fields needed when connecting a user account with this authentication method
    """

    optional: List[AuthConfigDetailFieldsConnectedAccountInitiationOptional]

    required: List[AuthConfigDetailFieldsConnectedAccountInitiationRequired]


class AuthConfigDetailFields(BaseModel):
    """Field groups required for different authentication stages"""

    auth_config_creation: AuthConfigDetailFieldsAuthConfigCreation
    """Form fields needed when creating an authentication configuration"""

    connected_account_initiation: AuthConfigDetailFieldsConnectedAccountInitiation
    """
    Form fields needed when connecting a user account with this authentication
    method
    """


class AuthConfigDetailDeprecatedAuthProviderDetails(BaseModel):
    """Authentication URL fields for OAuth 2.0 and OAuth 1.0.

    We don't recommend using this field for authentication and might break post Aug 31 2025.
    """

    authorization_url: Optional[str] = None

    token_url: Optional[str] = None


class AuthConfigDetailProxy(BaseModel):
    """Configuration for proxying authentication requests to external services"""

    base_url: str
    """URL to which authentication requests will be proxied"""


class AuthConfigDetail(BaseModel):
    """Detailed configuration for an authentication method"""

    fields: AuthConfigDetailFields
    """Field groups required for different authentication stages"""

    mode: str
    """The type of authentication mode (e.g., oauth2, basic_auth, api_key)"""

    name: str
    """Display name for this authentication method"""

    deprecated_auth_provider_details: Optional[AuthConfigDetailDeprecatedAuthProviderDetails] = None
    """Authentication URL fields for OAuth 2.0 and OAuth 1.0.

    We don't recommend using this field for authentication and might break post Aug
    31 2025.
    """

    proxy: Optional[AuthConfigDetailProxy] = None
    """Configuration for proxying authentication requests to external services"""


class ToolkitRetrieveResponse(BaseModel):
    """Detailed information about a single toolkit"""

    deprecated: Deprecated

    enabled: bool
    """Indicates if this toolkit is currently enabled and available for use"""

    is_local_toolkit: bool
    """DEPRECATED: This field is no longer meaningful and will always return false.

    It was previously used to indicate if a toolkit is specific to the current
    project.
    """

    meta: Meta
    """
    Comprehensive metadata for the toolkit including dates, descriptions, and
    statistics
    """

    name: str
    """Human-readable name of the toolkit"""

    slug: str
    """URL-friendly unique identifier for the toolkit"""

    auth_config_details: Optional[List[AuthConfigDetail]] = None
    """Complete authentication configuration details for each supported auth method"""

    base_url: Optional[str] = None
    """
    If evaluation of base URL needs some connection info (like shopify), please
    create the connection and get the base URL from there
    """

    composio_managed_auth_schemes: Optional[List[str]] = None
    """List of authentication methods that Composio manages for this toolkit"""

    get_current_user_endpoint: Optional[str] = None
    """Endpoint to get the current user"""
