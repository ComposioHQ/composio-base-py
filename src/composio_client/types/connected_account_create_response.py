# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ConnectedAccountCreateResponse", "Deprecated"]


class Deprecated(BaseModel):
    auth_config_uuid: str = FieldInfo(alias="authConfigUuid")
    """The uuid of the auth config"""

    uuid: str
    """The uuid of the connected account"""


class ConnectedAccountCreateResponse(BaseModel):
    id: str
    """The id of the connected account"""

    deprecated: Deprecated

    redirect_url: Optional[str] = None
    """The redirect URL of the app (previously named redirect_uri)"""

    status: Literal["ACTIVE", "INACTIVE", "DELETED", "INITIATED", "EXPIRED", "FAILED"]
    """The status of the connected account"""
