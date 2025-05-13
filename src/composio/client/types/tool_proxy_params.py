# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolProxyParams", "Parameter"]


class ToolProxyParams(TypedDict, total=False):
    endpoint: Required[str]

    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH"]]

    body: object

    connected_account_id: str

    parameters: Iterable[Parameter]


class Parameter(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["header", "query"]]

    value: Required[str]
