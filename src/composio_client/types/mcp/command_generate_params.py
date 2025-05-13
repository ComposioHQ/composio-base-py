# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CommandGenerateParams"]


class CommandGenerateParams(TypedDict, total=False):
    id: Required[str]
    """The ID of the MCP server"""

    mcp_client: Required[Literal["cursor", "claude", "windsurf"]]
    """MCP client to generate command for"""

    ttl: Literal["1d", "3d", "1 month", "no expiration"]
    """Time to live for the command"""
