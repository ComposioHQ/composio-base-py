# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ManageUpdateParams"]


class ManageUpdateParams(TypedDict, total=False):
    status: Required[Literal["enable", "disable"]]
