# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthConfigRetrieveResponse", "DeprecatedParams", "Toolkit"]


class DeprecatedParams(BaseModel):
    default_connector_id: Optional[str] = None

    expected_input_fields: Optional[List[Dict[str, Optional[object]]]] = None

    member_uuid: Optional[str] = None

    toolkit_id: Optional[str] = None


class Toolkit(BaseModel):
    logo: str
    """The logo of the app"""

    slug: str
    """The unique key of the app"""


class AuthConfigRetrieveResponse(BaseModel):
    id: str
    """The unique id of the auth config"""

    deprecated_params: DeprecatedParams

    name: str
    """The name of the auth config"""

    no_of_connections: float
    """The number of connections for the auth config"""

    status: Literal["ENABLED", "DISABLED"]

    toolkit: Toolkit

    type: Literal["default", "custom"]
    """The type of the auth config"""

    uuid: str
    """The unique id of the auth config"""

    auth_scheme: Optional[
        Literal[
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
    ] = None

    created_at: Optional[str] = None
    """The date and time the auth config was created"""

    created_by: Optional[str] = None
    """The user who created the auth config"""

    credentials: Optional[Dict[str, Optional[object]]] = None

    expected_input_fields: Optional[List[Optional[object]]] = None

    is_composio_managed: Optional[bool] = None

    last_updated_at: Optional[str] = None
    """The date and time the auth config was last updated"""

    restrict_to_following_tools: Optional[List[str]] = None
