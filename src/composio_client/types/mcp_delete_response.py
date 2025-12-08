# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["McpDeleteResponse"]


class McpDeleteResponse(BaseModel):
    """Response indicating the success of the delete operation"""

    id: str
    """Unique identifier of the MCP server to retrieve, update, or delete"""

    deleted: bool
    """Indicates whether the MCP server was successfully deleted"""
