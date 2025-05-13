# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CommandGenerateResponse"]


class CommandGenerateResponse(BaseModel):
    command: Optional[str] = None
    """The generated command to run"""

    url: Optional[str] = None
    """The URL for the MCP server"""
