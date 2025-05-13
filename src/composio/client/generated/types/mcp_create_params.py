# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["McpCreateParams"]


class McpCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the MCP server"""

    actions: List[str]
    """Actions available for the server"""

    apps: List[str]
    """App IDs associated with the server"""

    auth_configs: Dict[str, Optional[object]]
    """Auth configurations"""

    connected_account_ids: List[str]
    """Connected account IDs"""

    custom_auth_headers: bool
    """Whether to use custom auth headers"""

    entity_ids: List[str]
    """Entity IDs"""

    ttl: Literal["1d", "3d", "1 month", "no expiration"]
    """Time to live for the server"""
