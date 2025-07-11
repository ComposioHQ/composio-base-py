# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["McpListResponse", "Item", "ItemCommands"]


class ItemCommands(BaseModel):
    claude: str
    """Command line instruction for Claude client setup"""

    cursor: str
    """Command line instruction for Cursor client setup"""

    windsurf: str
    """Command line instruction for Windsurf client setup"""


class Item(BaseModel):
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
    """URL endpoint for establishing SSE connection to this MCP server"""

    name: str
    """User-defined descriptive name for this MCP server"""

    toolkits: List[str]
    """Array of toolkit slugs that this MCP server is allowed to use"""

    updated_at: str
    """Date and time when this server configuration was last modified"""


class McpListResponse(BaseModel):
    current_page: float
    """Current page number being returned"""

    items: List[Item]
    """Array of MCP server configurations"""

    total_pages: float
    """Total number of pages in the paginated response"""
