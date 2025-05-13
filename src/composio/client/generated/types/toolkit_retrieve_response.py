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

    slug: str


class Meta(BaseModel):
    categories: List[MetaCategory]

    created_at: str

    description: str

    logo: str

    tools_count: float

    triggers_count: float

    updated_at: str


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

    connected_account_initiation: AuthConfigDetailFieldsConnectedAccountInitiation


class AuthConfigDetailProxy(BaseModel):
    base_url: str


class AuthConfigDetail(BaseModel):
    fields: AuthConfigDetailFields

    mode: str

    name: str

    proxy: Optional[AuthConfigDetailProxy] = None


class ToolkitRetrieveResponse(BaseModel):
    enabled: bool

    is_local_toolkit: bool

    meta: Meta

    name: str

    slug: str

    auth_config_details: Optional[List[AuthConfigDetail]] = None

    composio_managed_auth_schemes: Optional[List[str]] = None
