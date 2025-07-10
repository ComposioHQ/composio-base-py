# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["AuthConfigUpdateParams", "Variant0", "Variant0ToolAccessConfig", "Variant1", "Variant1ToolAccessConfig"]


class Variant0(TypedDict, total=False):
    credentials: Required[Dict[str, Optional[object]]]

    type: Required[Literal["custom"]]

    tool_access_config: Variant0ToolAccessConfig


class Variant0ToolAccessConfig(TypedDict, total=False):
    tools_available_for_execution: List[str]
    """The actions that the user can perform on the auth config.

    If passed, this will update the actions that the user can perform on the auth
    config.
    """

    tools_for_connected_account_creation: List[str]
    """
    Tools used to generate the minimum required scopes for the auth config (only
    valid for OAuth). If passed, this will update the scopes.
    """


class Variant1(TypedDict, total=False):
    type: Required[Literal["default"]]

    scopes: str

    tool_access_config: Variant1ToolAccessConfig


class Variant1ToolAccessConfig(TypedDict, total=False):
    tools_available_for_execution: List[str]
    """The actions that the user can perform on the auth config.

    If passed, this will update the actions that the user can perform on the auth
    config.
    """

    tools_for_connected_account_creation: List[str]
    """
    Tools used to generate the minimum required scopes for the auth config (only
    valid for OAuth). If passed, this will update the scopes.
    """


AuthConfigUpdateParams: TypeAlias = Union[Variant0, Variant1]
