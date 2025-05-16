# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["TriggersTypeListParams"]


class TriggersTypeListParams(TypedDict, total=False):
    cursor: str

    limit: Optional[float]

    toolkit_slugs: Optional[List[str]]
    """Array of toolkit slugs"""
