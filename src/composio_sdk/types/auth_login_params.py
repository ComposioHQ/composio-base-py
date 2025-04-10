# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthLoginParams"]


class AuthLoginParams(TypedDict, total=False):
    redirect_uri: Annotated[str, PropertyInfo(alias="redirectUri")]
