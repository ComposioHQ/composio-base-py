# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["CustomCreateResponse", "Commands"]


class Commands(BaseModel):
    claude: str
    """Command line instruction for Claude client setup"""

    cursor: str
    """Command line instruction for Cursor client setup"""

    windsurf: str
    """Command line instruction for Windsurf client setup"""


class CustomCreateResponse(BaseModel):
    id: str
    """Unique identifier for the newly created custom MCP server"""

    allowed_tools: List[str]
    """List of tool identifiers that are enabled for this server"""

    auth_config_ids: List[str]
    """ID references to the auth configurations used by this server"""

    commands: Commands
    """
    Set of command line instructions for connecting various clients to this MCP
    server
    """

    mcp_url: str
    """
    URL endpoint for establishing Server-Sent Events (SSE) connection to this MCP
    server
    """

    name: str
    """Human-readable name of the custom MCP server"""
