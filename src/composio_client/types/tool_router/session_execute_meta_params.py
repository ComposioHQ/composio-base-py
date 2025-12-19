# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionExecuteMetaParams"]


class SessionExecuteMetaParams(TypedDict, total=False):
    slug: Required[
        Literal[
            "COMPOSIO_SEARCH_TOOLS",
            "COMPOSIO_MULTI_EXECUTE_TOOL",
            "COMPOSIO_MANAGE_CONNECTIONS",
            "COMPOSIO_REMOTE_WORKBENCH",
            "COMPOSIO_REMOTE_BASH_TOOL",
            "COMPOSIO_GET_TOOL_SCHEMAS",
        ]
    ]
    """The unique slug identifier of the meta tool to execute"""

    arguments: Dict[str, Optional[object]]
    """The arguments required by the meta tool"""
