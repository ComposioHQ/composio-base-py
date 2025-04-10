# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthOneTapParams", "Variant0", "Variant0Data", "Variant1", "Variant1Data"]


class Variant0(TypedDict, total=False):
    data: Required[Variant0Data]

    type: Required[Literal["jwt"]]


class Variant0Data(TypedDict, total=False):
    jwt: Required[str]


class Variant1(TypedDict, total=False):
    data: Required[Variant1Data]

    type: Required[Literal["auth-code"]]


class Variant1Data(TypedDict, total=False):
    auth_code: Required[Annotated[str, PropertyInfo(alias="authCode")]]


AuthOneTapParams: TypeAlias = Union[Variant0, Variant1]
