# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LinkRetrieveResponse", "ConnectedAccount", "ConnectedAccountExpectedInputField", "Project", "Toolkit"]


class ConnectedAccountExpectedInputField(BaseModel):
    display_name: str = FieldInfo(alias="displayName")

    name: str

    required: bool

    type: str

    default: Optional[str] = None

    description: Optional[str] = None

    legacy_template_name: Optional[str] = None


class ConnectedAccount(BaseModel):
    id: str
    """The connected account ID"""

    mode: Literal[
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
    ]

    status: Literal["INITIATED", "ACTIVE", "FAILED"]

    callback_url: Optional[str] = None
    """The user callback URL if applicable. If active, redirect to this URL"""

    expected_input_fields: Optional[List[ConnectedAccountExpectedInputField]] = None

    redirect_url: Optional[str] = None
    """The OAuth provider redirect URL if applicable. If active, redirect to this URL"""


class Project(BaseModel):
    logo: Optional[str] = None
    """The project logo URL"""

    name: Optional[str] = None
    """The project name"""


class Toolkit(BaseModel):
    logo: str
    """The toolkit logo"""

    name: str
    """The toolkit display name"""

    slug: str
    """The toolkit slug"""


class LinkRetrieveResponse(BaseModel):
    connected_account: ConnectedAccount

    project: Project

    toolkit: Toolkit
