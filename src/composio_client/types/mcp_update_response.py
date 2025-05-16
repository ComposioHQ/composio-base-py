# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["McpUpdateResponse", "Commands"]


class Commands(BaseModel):
    claude: str
    """The claude command to connect to the MCP server"""

    cursor: str
    """The cursor command to connect to the MCP server"""

    windsurf: str
    """The windsurf command to connect to the MCP server"""


class McpUpdateResponse(BaseModel):
    id: str
    """The ID of the MCP server"""

    allowed_tools: List[str]
    """The allowed tools for this server"""

    auth_config_id: str
    """The auth configuration ID"""

    client_id: str
    """Client ID associated with the MCP server"""

    commands: Commands
    """Command to connect to the MCP server using different clients"""

    created_at: str
    """Creation timestamp of the MCP server"""

    deleted: bool
    """Whether the MCP server is deleted"""

    mcp_url: str
    """The SSE URL for the MCP server."""

    name: str
    """The name of the MCP server"""

    updated_at: str
    """Last update timestamp of the MCP server"""

    actions: Optional[Dict[str, Optional[object]]] = None
    """Actions available for the MCP server"""

    apps: Optional[List[str]] = None
    """App IDs associated with the server"""

    auth_configs: Optional[List[str]] = None
    """Auth config IDs associated with the server"""

    connected_account_ids: Optional[List[str]] = None
    """Connected account IDs associated with the server"""

    custom_auth_headers: Optional[bool] = None
    """Whether custom auth headers are enabled"""

    entity_ids: Optional[List[str]] = None
    """Entity IDs associated with the server"""
