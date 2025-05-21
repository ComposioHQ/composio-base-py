# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["McpUpdateResponse", "Commands"]


class Commands(BaseModel):
    claude: str
    """Command line instruction for Claude client setup"""

    cursor: str
    """Command line instruction for Cursor client setup"""

    windsurf: str
    """Command line instruction for Windsurf client setup"""


class McpUpdateResponse(BaseModel):
    id: str
    """UUID of the MCP server instance"""

    allowed_tools: List[str]
    """Array of tool slugs that this MCP server is allowed to use"""

    auth_config_id: str
    """ID reference to the auth configuration used by this server"""

    client_id: str
    """Project identifier that owns this MCP server instance"""

    commands: Commands
    """
    Set of command line instructions for connecting various clients to this MCP
    server
    """

    created_at: str
    """ISO timestamp of when this server was initially created"""

    deleted: bool
    """Flag indicating if this server has been soft-deleted"""

    mcp_url: str
    """URL endpoint for establishing SSE connection to this MCP server"""

    name: str
    """User-defined descriptive name for this MCP server"""

    updated_at: str
    """ISO timestamp of when this server configuration was last modified"""

    actions: Optional[Dict[str, Optional[object]]] = None
    """
    Dictionary of action configurations and permissions available for this MCP
    server
    """

    apps: Optional[List[str]] = None
    """List of application identifiers this server is configured to work with"""

    auth_configs: Optional[List[str]] = None
    """List of authentication configuration identifiers used by this server"""

    connected_account_ids: Optional[List[str]] = None
    """List of connected account identifiers this server can use for authentication"""

    custom_auth_headers: Optional[bool] = None
    """Flag indicating if this server uses custom authentication headers"""

    entity_ids: Optional[List[str]] = None
    """List of entity identifiers this MCP server can interact with"""
