# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ToolkitListParams"]


class ToolkitListParams(TypedDict, total=False):
    category: str

    is_local: bool

    managed_by: Literal["all", "composio_managed", "project_managed"]

    sort_by: Literal["usage", "alphabetically"]
