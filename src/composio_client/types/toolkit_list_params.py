# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ToolkitListParams"]


class ToolkitListParams(TypedDict, total=False):
    category: str
    """Filter toolkits by category"""

    is_local: Optional[bool]
    """Whether to include local toolkits in the results"""

    managed_by: Literal["composio", "all", "project"]
    """Filter toolkits by who manages them"""

    sort_by: Literal["usage", "alphabetically"]
    """Sort order for returned toolkits"""
