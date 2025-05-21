# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolProxyParams", "Parameter"]


class ToolProxyParams(TypedDict, total=False):
    endpoint: Required[str]
    """
    The API endpoint to call (absolute URL or path relative to base URL of the
    connected account)
    """

    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH"]]
    """The HTTP method to use for the request"""

    body: object
    """The request body (for POST, PUT, and PATCH requests)"""

    connected_account_id: str
    """
    The ID of the connected account to use for authentication (if not provided, will
    use the default account for the project)
    """

    parameters: Iterable[Parameter]
    """Additional HTTP headers or query parameters to include in the request"""


class Parameter(TypedDict, total=False):
    name: Required[str]
    """Parameter name"""

    type: Required[Literal["header", "query"]]
    """Parameter type (header or query)"""

    value: Required[str]
    """Parameter value"""
