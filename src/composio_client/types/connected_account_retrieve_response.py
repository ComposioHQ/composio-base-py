# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectedAccountRetrieveResponse", "AuthConfig", "AuthConfigDeprecated", "Toolkit", "Deprecated"]


class AuthConfigDeprecated(BaseModel):
    uuid: str
    """The uuid of the auth config"""


class AuthConfig(BaseModel):
    id: str
    """The id of the auth config"""

    auth_scheme: Literal[
        "OAUTH2",
        "OAUTH1",
        "OAUTH1A",
        "API_KEY",
        "BASIC",
        "BILLCOM_AUTH",
        "BEARER_TOKEN",
        "GOOGLE_SERVICE_ACCOUNT",
        "NO_AUTH",
        "BASIC_WITH_JWT",
        "COMPOSIO_LINK",
        "CALCOM_AUTH",
        "SNOWFLAKE",
    ]
    """The auth scheme of the auth config"""

    is_composio_managed: bool
    """Whether the auth config is managed by Composio"""

    is_disabled: bool
    """Whether the auth config is disabled"""

    deprecated: Optional[AuthConfigDeprecated] = None


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
    """The data of the connection"""

    is_disabled: bool
    """Whether the connected account is disabled"""

    params: Dict[str, Optional[object]]
    """The init data of the connection"""

    status: Literal["ACTIVE", "INACTIVE", "DELETED", "INITIATED", "EXPIRED", "FAILED"]
    """The status of the connection"""

    status_reason: Optional[str] = None
    """The reason the connected account is disabled"""

    toolkit: Toolkit

    updated_at: str
    """The updated at of the connection"""

    user_id: str
    """The user id of the connection"""

    deprecated: Optional[Deprecated] = None

    test_request_endpoint: Optional[str] = None
    """The endpoint to make test request for verification"""
