# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ToolRouterCreateSessionResponse"]


class ToolRouterCreateSessionResponse(BaseModel):
    chat_session_mcp_url: str
    """MCP server endpoint URL for this specific chat session"""

    session_id: str
    """Generated session identifier"""

    tool_router_instance_mcp_url: str
    """MCP server endpoint URL for this specific tool router instance"""
