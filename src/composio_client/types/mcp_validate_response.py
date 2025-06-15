# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["McpValidateResponse", "Client", "UserData"]


class Client(BaseModel):
    id: str
    """Project identifier that owns this MCP server"""

    org_id: str = FieldInfo(alias="orgId")
    """Organization identifier that owns the project"""


class UserData(BaseModel):
    id: str
    """User identifier for API access"""

    api_key: str = FieldInfo(alias="apiKey")
    """API key for authenticating requests to the Composio API"""

    email: str
    """Email address associated with the API key user"""


class McpValidateResponse(BaseModel):
    id: str
    """Unique identifier of the validated MCP server"""

    client: Client
    """Client information for the MCP server"""

    name: str
    """Human-readable name of the MCP server"""

    url: str
    """URL endpoint for connecting to this MCP server"""

    user_data: UserData = FieldInfo(alias="userData")
    """User authentication data for the MCP server"""

    allowed_tools: Optional[List[str]] = None
    """List of action identifiers enabled for this server"""

    custom_auth_headers: Optional[bool] = FieldInfo(alias="customAuthHeaders", default=None)
    """Flag indicating if this server uses custom authentication headers"""

    managed_auth_via_composio: Optional[bool] = None
    """Flag indicating if this server is managed by Composio and not by the user"""

    toolkits: Optional[List[str]] = None
    """List of application identifiers this server is configured for"""
