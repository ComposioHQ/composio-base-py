# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["McpRetrieveAppResponse", "Item", "ItemCommands"]


class ItemCommands(BaseModel):
    """
    Set of command line instructions for connecting various clients to this MCP server
    """

    claude: str
    """Command line instruction for Claude client setup"""

    cursor: str
    """Command line instruction for Cursor client setup"""

    windsurf: str
    """Command line instruction for Windsurf client setup"""


class Item(BaseModel):
    """MCP server configuration and connection details"""

    id: str
    """UUID of the MCP server instance"""

    allowed_tools: List[str]
    """Array of tool slugs that this MCP server is allowed to use"""

    auth_config_ids: List[str]
    """ID references to the auth configurations used by this server"""

    commands: ItemCommands
    """
    Set of command line instructions for connecting various clients to this MCP
    server
    """

    created_at: str
    """Date and time when this server was initially created"""

    managed_auth_via_composio: bool
    """Whether the MCP server is managed by Composio"""

    mcp_url: str
    """
    [DEPRECATED] Please use the URL with user_id or connected_account_id query param
    """

    name: str
    """User-defined descriptive name for this MCP server"""

    server_instance_count: float
    """Total count of active user instances connected to this server"""

    toolkit_icons: Dict[str, str]
    """Object mapping each toolkit slug to its icon/logo URL for display purposes"""

    toolkits: List[str]
    """Array of toolkit slugs that this MCP server is allowed to use"""

    updated_at: str
    """Date and time when this server configuration was last modified"""


class McpRetrieveAppResponse(BaseModel):
    """Paginated response containing MCP servers"""

    current_page: float
    """Current page number being returned"""

    items: List[Item]
    """Array of MCP server configurations"""

    total_pages: float
    """Total number of pages in the paginated response"""
