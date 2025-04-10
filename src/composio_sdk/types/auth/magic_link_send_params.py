# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MagicLinkSendParams"]


class MagicLinkSendParams(TypedDict, total=False):
    email: Required[str]

    verify_host: Annotated[str, PropertyInfo(alias="verifyHost")]
