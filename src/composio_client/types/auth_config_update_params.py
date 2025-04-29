# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["AuthConfigUpdateParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    credentials: Required[Dict[str, Optional[object]]]

    type: Required[Literal["custom"]]

    restrict_to_following_tools: List[str]


class Variant1(TypedDict, total=False):
    scopes: Required[List[str]]

    type: Required[Literal["default"]]

    restrict_to_following_tools: List[str]


AuthConfigUpdateParams: TypeAlias = Union[Variant0, Variant1]
