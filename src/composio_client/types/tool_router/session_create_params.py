# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "SessionCreateParams",
    "Experimental",
    "ExperimentalAssistivePromptConfig",
    "ExperimentalCustomToolkit",
    "ExperimentalCustomToolkitTool",
    "ExperimentalCustomTool",
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

    experimental: Experimental
    """
    Experimental features - not stable, may be modified or removed in future
    versions.
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


class ExperimentalAssistivePromptConfig(TypedDict, total=False):
    """Customize assistive prompt generation (e.g., timezone)."""

    user_timezone: str
    """IANA timezone identifier (e.g., 'America/New_York', 'Europe/London').

    Used to customize the system prompt with timezone-aware instructions.
    """


class ExperimentalCustomToolkitTool(TypedDict, total=False):
    description: Required[str]
    """Used for BM25 search matching and shown to the LLM."""

    input_schema: Required[Dict[str, Optional[object]]]
    """Must have type: "object" and a properties field."""

    name: Required[str]
    """Human-readable display name"""

    slug: Required[str]
    """Tool slug.

    Combined with toolkit slug to form LOCAL*<TOOLKIT>*<TOOL> (max 60 chars total).
    """

    output_schema: Dict[str, Optional[object]]
    """Optional output schema for the tool response."""


class ExperimentalCustomToolkit(TypedDict, total=False):
    description: Required[str]
    """Used for BM25 search matching and shown in toolkit connection statuses."""

    name: Required[str]
    """Display name shown to the LLM and in search results."""

    slug: Required[str]
    """Unique slug for the toolkit.

    Must not conflict with existing Composio toolkit slugs. Alphanumeric,
    underscores, and hyphens only.
    """

    tools: Required[Iterable[ExperimentalCustomToolkitTool]]
    """Tools in this custom toolkit"""


class ExperimentalCustomTool(TypedDict, total=False):
    description: Required[str]
    """Used for BM25 search matching and shown to the LLM."""

    input_schema: Required[Dict[str, Optional[object]]]
    """Must have type: "object" and a properties field."""

    name: Required[str]
    """Human-readable display name"""

    slug: Required[str]
    """Tool slug.

    Forms LOCAL*<TOOL> (standalone) or LOCAL*<TOOLKIT>\\__<TOOL> (extending). Max 60
    chars total.
    """

    extends_toolkit: str
    """If set, must be a valid Composio toolkit slug.

    The tool inherits that toolkit's auth/connection status. If omitted, the tool is
    standalone (no-auth).
    """

    output_schema: Dict[str, Optional[object]]
    """JSON Schema describing tool output (optional)"""


class Experimental(TypedDict, total=False):
    """
    Experimental features - not stable, may be modified or removed in future versions.
    """

    assistive_prompt_config: ExperimentalAssistivePromptConfig
    """Customize assistive prompt generation (e.g., timezone)."""

    custom_toolkits: Iterable[ExperimentalCustomToolkit]
    """Custom toolkits with grouped tools.

    Toolkit slugs must not conflict with existing Composio toolkits. All tools are
    no-auth.
    """

    custom_tools: Iterable[ExperimentalCustomTool]
    """Custom tools to include in search.

    Standalone tools need no auth. Tools with extends_toolkit inherit the Composio
    toolkit's connection.
    """


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

    enable_connection_removal: Optional[bool]
    """
    Enable the "remove" action in COMPOSIO_MANAGE_CONNECTIONS to allow deleting
    connected accounts. Default true.
    """

    enable_wait_for_connections: Optional[bool]
    """
    When true, the COMPOSIO_WAIT_FOR_CONNECTIONS tool is available for agents to
    poll connection status after sharing auth URLs. Default is false (disabled). May
    not work reliably with GPT models.
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

    enable: bool
    """Set to false to disable the workbench entirely.

    When disabled, no code execution tools are available in the session.
    """

    enable_proxy_execution: bool
    """Whether proxy execution is enabled.

    When enabled, workbench can call URLs and APIs directly.
    """
