# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["McpRetrieveResponse"]


class McpRetrieveResponse(BaseModel):
    id: str
    """The ID of the MCP server"""

    apps: List[str]
    """The app IDs associated with the server"""

    client_id: str
    """Client ID associated with the MCP server"""

    created_at: str
    """Creation timestamp of the MCP server"""

    deleted: bool
    """Whether the MCP server is deleted"""

    member_id: str
    """The member ID who created the server"""

    name: str
    """The name of the MCP server"""

    updated_at: str
    """Last update timestamp of the MCP server"""

    url: str
    """The URL of the MCP server"""

    actions: Optional[Dict[str, Optional[object]]] = None
    """Actions available for the MCP server"""

    auth_configs: Optional[Dict[str, Optional[object]]] = None
    """Auth configuration"""

    connected_account_ids: Optional[List[str]] = None
    """Connected account IDs"""

    custom_auth_headers: Optional[bool] = None
    """Whether custom auth headers are enabled"""

    entity_ids: Optional[List[str]] = None
    """Entity IDs associated with the server"""
