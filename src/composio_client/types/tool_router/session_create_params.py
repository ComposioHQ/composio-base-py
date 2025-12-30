# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "SessionCreateParams",
    "ManageConnections",
    "Tags",
    "TagsUnionMember1",
    "Toolkits",
    "ToolkitsEnable",
    "ToolkitsDisable",
    "Tools",
    "ToolsEnable",
    "ToolsDisable",
    "ToolsTags",
    "ToolsTagsTags",
    "ToolsTagsTagsUnionMember1",
    "Workbench",
]


class SessionCreateParams(TypedDict, total=False):
    user_id: Required[str]
    """
    The identifier of the user who is initiating the session, ideally a unique
    identifier from your database like a user ID or email address
    """

    auth_configs: Dict[str, str]
    """The auth configs to use for the session.

    This will override the default behavior and use the given auth config when
    specific toolkits are being executed
    """

    connected_accounts: Dict[str, str]
    """The connected accounts to use for the session.

    This will override the default behaviour and use the given connected account
    when specific toolkits are being executed
    """

    manage_connections: ManageConnections
    """Configuration for connection management settings"""

    tags: Tags
    """Global MCP tool annotation hints for filtering.

    Array format is treated as enabled list. Object format supports both enabled
    (tool must have at least one) and disabled (tool must NOT have any) lists.
    Toolkit-level tags override this. Toolkit enabled/disabled lists take precedence
    over tag filtering.
    """

    toolkits: Toolkits
    """
    Toolkit configuration - specify either enable toolkits (allowlist) or disable
    toolkits (denylist). Mutually exclusive.
    """

    tools: Dict[str, Tools]
    """
    Tool-level configuration per toolkit - either specify enable tools (whitelist),
    disable tools (blacklist), or filter by MCP tags for each toolkit
    """

    workbench: Workbench
    """Configuration for workbench behavior"""


class ManageConnections(TypedDict, total=False):
    """Configuration for connection management settings"""

    callback_url: str
    """
    The URL to redirect to after a user completes authentication for a connected
    account. This allows you to handle the auth callback in your own application.
    """

    enable: Optional[bool]
    """Whether to enable the connection manager for automatic connection handling.

    If true, we will provide a tool your agent can use to initiate connections to
    toolkits if it doesnt exist. If set to false, then you have to manage
    connections manually.
    """


class TagsUnionMember1(TypedDict, total=False):
    disable: List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]
    """Tags that the tool must NOT have any of"""

    enable: List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]
    """Tags that the tool must have at least one of"""


Tags: TypeAlias = Union[
    List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]], TagsUnionMember1
]


class ToolkitsEnable(TypedDict, total=False):
    """Enable only specific toolkits (allowlist)"""

    enable: Required[SequenceNotStr[str]]
    """Only these specific toolkits will be enabled"""


class ToolkitsDisable(TypedDict, total=False):
    """Disable specific toolkits (denylist)"""

    disable: Required[SequenceNotStr[str]]
    """These specific toolkits will be disabled"""


Toolkits: TypeAlias = Union[ToolkitsEnable, ToolkitsDisable]


class ToolsEnable(TypedDict, total=False):
    enable: Required[SequenceNotStr[str]]
    """Only these specific tools will be available for this toolkit"""


class ToolsDisable(TypedDict, total=False):
    disable: Required[SequenceNotStr[str]]
    """These specific tools will be disabled for this toolkit"""


class ToolsTagsTagsUnionMember1(TypedDict, total=False):
    disable: List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]
    """Tags that the tool must NOT have any of"""

    enable: List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]
    """Tags that the tool must have at least one of"""


ToolsTagsTags: TypeAlias = Union[
    List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]], ToolsTagsTagsUnionMember1
]


class ToolsTags(TypedDict, total=False):
    tags: Required[ToolsTagsTags]
    """MCP tags to filter tools.

    Array format is treated as enabled list. Object format supports both enabled and
    disabled lists.
    """


Tools: TypeAlias = Union[ToolsEnable, ToolsDisable, ToolsTags]


class Workbench(TypedDict, total=False):
    """Configuration for workbench behavior"""

    auto_offload_threshold: float
    """Character threshold for automatic offloading.

    When workbench response exceeds this threshold, it will be automatically
    offloaded. Default is picked automatically based on the response size.
    """

    enable_proxy_execution: bool
    """Whether proxy execution is enabled.

    When enabled, workbench can call URLs and APIs directly.
    """
