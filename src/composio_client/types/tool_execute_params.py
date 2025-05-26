# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolExecuteParams", "CustomAuthParams", "CustomAuthParamsParameter"]


class ToolExecuteParams(TypedDict, total=False):
    allow_tracing: bool
    """Enable debug tracing for tool execution (useful for debugging)"""

    arguments: Dict[str, Optional[object]]
    """
    Key-value pairs of arguments required by the tool (mutually exclusive with text)
    """

    connected_account_id: str
    """Unique identifier for the connected account to use for authentication"""

    custom_auth_params: CustomAuthParams
    """
    Custom authentication parameters for tools that support parameterized
    authentication
    """

    entity_id: str
    """Entity identifier for multi-entity connected accounts (e.g.

    multiple repositories, organizations)
    """

    text: str
    """
    Natural language description of the task to perform (mutually exclusive with
    arguments)
    """

    version: str
    """Tool version to execute (defaults to "latest" if not specified)"""


_CustomAuthParamsParameterReservedKeywords = TypedDict(
    "_CustomAuthParamsParameterReservedKeywords",
    {
        "in": Literal["query", "header"],
    },
    total=False,
)


class CustomAuthParamsParameter(_CustomAuthParamsParameterReservedKeywords, total=False):
    name: Required[str]
    """The name of the parameter. For example, 'x-api-key', 'Content-Type', etc."""

    value: Required[Union[str, float]]
    """The value of the parameter. For example, '1234567890', 'application/json', etc."""


class CustomAuthParams(TypedDict, total=False):
    parameters: Required[Iterable[CustomAuthParamsParameter]]

    base_url: str
    """
    The base URL (root address) what you should use while making http requests to
    the connected account. For example, for gmail, it would be
    'https://gmail.googleapis.com'
    """

    body: Dict[str, Optional[object]]
    """The body to be sent to the endpoint for authentication.

    This is a JSON object. Note: This is very rarely needed and is only required by
    very few apps.
    """
