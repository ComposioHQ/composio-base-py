# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthRetrieveCallbackParams"]


class AuthRetrieveCallbackParams(TypedDict, total=False):
    auth_code: Annotated[str, PropertyInfo(alias="authCode")]

    code: str

    error: str

    error_description: str

    state: str
