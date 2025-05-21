# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ToolkitRetrieveResponse",
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
    "AuthConfigDetailProxy",
]


class MetaCategory(BaseModel):
    name: str
    """Human-readable category name"""

    slug: str
    """URL-friendly identifier for the category"""


class Meta(BaseModel):
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

    app_url: Optional[str] = None
    """Link to the toolkit's main application or service website"""


class AuthConfigDetailFieldsAuthConfigCreationOptional(BaseModel):
    description: str

    display_name: str = FieldInfo(alias="displayName")

    name: str

    required: bool

    type: str

    default: Optional[str] = None


class AuthConfigDetailFieldsAuthConfigCreationRequired(BaseModel):
    description: str

    display_name: str = FieldInfo(alias="displayName")

    name: str

    required: bool

    type: str

    default: Optional[str] = None


class AuthConfigDetailFieldsAuthConfigCreation(BaseModel):
    optional: List[AuthConfigDetailFieldsAuthConfigCreationOptional]

    required: List[AuthConfigDetailFieldsAuthConfigCreationRequired]


class AuthConfigDetailFieldsConnectedAccountInitiationOptional(BaseModel):
    description: str

    display_name: str = FieldInfo(alias="displayName")

    name: str

    required: bool

    type: str

    default: Optional[str] = None


class AuthConfigDetailFieldsConnectedAccountInitiationRequired(BaseModel):
    description: str

    display_name: str = FieldInfo(alias="displayName")

    name: str

    required: bool

    type: str

    default: Optional[str] = None


class AuthConfigDetailFieldsConnectedAccountInitiation(BaseModel):
    optional: List[AuthConfigDetailFieldsConnectedAccountInitiationOptional]

    required: List[AuthConfigDetailFieldsConnectedAccountInitiationRequired]


class AuthConfigDetailFields(BaseModel):
    auth_config_creation: AuthConfigDetailFieldsAuthConfigCreation
    """Form fields needed when creating an authentication configuration"""

    connected_account_initiation: AuthConfigDetailFieldsConnectedAccountInitiation
    """
    Form fields needed when connecting a user account with this authentication
    method
    """


class AuthConfigDetailProxy(BaseModel):
    base_url: str
    """URL to which authentication requests will be proxied"""


class AuthConfigDetail(BaseModel):
    fields: AuthConfigDetailFields
    """Field groups required for different authentication stages"""

    mode: str
    """The type of authentication mode (e.g., oauth2, basic_auth, api_key)"""

    name: str
    """Display name for this authentication method"""

    proxy: Optional[AuthConfigDetailProxy] = None
    """Configuration for proxying authentication requests to external services"""


class ToolkitRetrieveResponse(BaseModel):
    enabled: bool
    """Indicates if this toolkit is currently enabled and available for use"""

    is_local_toolkit: bool
    """
    Indicates if this toolkit is specific to the current project or globally
    available
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

    composio_managed_auth_schemes: Optional[List[str]] = None
    """List of authentication methods that Composio manages for this toolkit"""
