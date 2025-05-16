# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["McpRetrieveAppResponse", "Item", "ItemCommands"]


class ItemCommands(BaseModel):
    claude: str
    """The claude command to connect to the MCP server"""

    cursor: str
    """The cursor command to connect to the MCP server"""

    windsurf: str
    """The windsurf command to connect to the MCP server"""


class Item(BaseModel):
    id: str
    """The ID of the MCP server"""

    allowed_tools: List[str]
    """The allowed tools for this server"""

    auth_config_id: str
    """The auth configuration ID"""

    commands: ItemCommands
    """Command to connect to the MCP server using different clients"""

    created_at: str
    """Creation timestamp of the MCP server"""

    mcp_url: str
    """The SSE URL for the MCP server."""

    name: str
    """The name of the MCP server"""

    updated_at: str
    """Last update timestamp of the MCP server"""


class McpRetrieveAppResponse(BaseModel):
    current_page: str
    """Current page number"""

    items: List[Item]
    """List of MCP servers"""

    total_pages: str
    """Total number of pages"""
