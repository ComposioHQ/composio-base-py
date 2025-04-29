# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolExecuteParams", "CustomAuthParams", "CustomAuthParamsParameter"]


class ToolExecuteParams(TypedDict, total=False):
    allow_tracing: bool

    arguments: Dict[str, Optional[object]]

    connected_account_id: str

    custom_auth_params: CustomAuthParams
    """
    An optional field for people who want to use their own auth to execute the
    action.
    """

    entity_id: str

    text: str

    version: str


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

    This is a JSON object. Note: This is very rarely neeed and is only required by
    very few apps.
    """
