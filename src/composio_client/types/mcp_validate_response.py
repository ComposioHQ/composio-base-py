# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["McpValidateResponse", "Client", "UserData"]


class Client(BaseModel):
    id: str
    """The client ID"""

    org_id: str = FieldInfo(alias="orgId")
    """The organization ID"""


class UserData(BaseModel):
    id: str
    """The user ID"""

    api_key: str = FieldInfo(alias="apiKey")
    """The API key"""

    email: str
    """The user email"""


class McpValidateResponse(BaseModel):
    id: str
    """The ID of the MCP server"""

    client: Client

    name: str
    """The name of the MCP server"""

    url: str
    """The URL of the MCP server"""

    user_data: UserData = FieldInfo(alias="userData")

    actions: Optional[List[str]] = None

    apps: Optional[List[str]] = None

    connected_account_ids: Optional[List[str]] = FieldInfo(alias="connectedAccountIds", default=None)

    custom_auth_headers: Optional[bool] = FieldInfo(alias="customAuthHeaders", default=None)

    entity_ids: Optional[List[str]] = FieldInfo(alias="entityIds", default=None)
