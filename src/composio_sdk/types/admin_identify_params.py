# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AdminIdentifyParams"]


class AdminIdentifyParams(TypedDict, total=False):
    hash: Required[str]

    admin_token: Annotated[str, PropertyInfo(alias="adminToken")]
