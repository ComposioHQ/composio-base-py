# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["McpRetrieveAppResponse", "Item"]


class Item(BaseModel):
    id: str
    """The ID of the MCP server"""

    apps: List[str]
    """The app IDs associated with the server"""

    member_id: str
    """The member ID who created the server"""

    name: str
    """The name of the MCP server"""

    updated_at: str
    """Last update timestamp of the MCP server"""

    url: str
    """The URL of the MCP server"""

    actions: Optional[List[str]] = None
    """Actions available for the MCP server"""

    auth_configs: Optional[Dict[str, Optional[object]]] = None
    """Auth configuration"""

    connected_account_ids: Optional[List[str]] = None
    """Connected account IDs"""


class McpRetrieveAppResponse(BaseModel):
    items: List[Item]
