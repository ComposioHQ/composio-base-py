# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionExecuteParams"]


class SessionExecuteParams(TypedDict, total=False):
    tool_slug: Required[str]
    """The unique slug identifier of the tool to execute"""

    arguments: Dict[str, Optional[object]]
    """The arguments required by the tool"""
