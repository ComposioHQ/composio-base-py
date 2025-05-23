# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

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

    commands: Commands
    """
    Set of command line instructions for connecting various clients to this MCP
    server
    """

    created_at: str
    """Date and time when this server was initially created"""

    deleted: bool
    """Whether the MCP server is deleted"""

    mcp_url: str
    """URL endpoint for establishing SSE connection to this MCP server"""

    name: str
    """User-defined descriptive name for this MCP server"""

    updated_at: str
    """Date and time when this server configuration was last modified"""
