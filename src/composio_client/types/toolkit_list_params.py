# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ToolkitListParams"]


class ToolkitListParams(TypedDict, total=False):
    category: str

    is_local: Optional[bool]
    """Whether to include local toolkits"""

    managed_by: Literal["composio", "all", "project"]

    sort_by: Literal["usage", "alphabetically"]
