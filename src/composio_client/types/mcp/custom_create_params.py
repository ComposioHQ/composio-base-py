# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["CustomCreateParams"]


class CustomCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    Human-readable name to identify this custom MCP server (4-30 characters,
    alphanumeric, spaces, and hyphens only)
    """

    toolkits: Required[List[str]]
    """List of application/toolkit identifiers to enable for this server"""

    auth_config_ids: List[str]
    """ID references to existing authentication configurations"""

    custom_tools: List[str]
    """
    Additional custom tool identifiers to enable that aren't part of standard
    toolkits
    """

    managed_auth_via_composio: bool
    """Whether to manage authentication via Composio"""
