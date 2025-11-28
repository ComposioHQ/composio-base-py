# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CustomCreateParams"]


class CustomCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    Human-readable name to identify this custom MCP server (4-30 characters,
    alphanumeric, spaces, and hyphens only)
    """

    allowed_tools: SequenceNotStr[str]
    """Tool identifiers to enable that aren't part of standard toolkits"""

    auth_config_ids: SequenceNotStr[str]
    """ID references to existing authentication configurations"""

    custom_tools: SequenceNotStr[str]
    """DEPRECATED: Use allowed_tools instead.

    Tool identifiers to enable that aren't part of standard toolkits
    """

    managed_auth_via_composio: bool
    """Whether to manage authentication via Composio"""

    toolkits: SequenceNotStr[str]
    """List of application/toolkit identifiers to enable for this server"""
