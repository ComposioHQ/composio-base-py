# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "SessionCreateParams",
    "Execute",
    "Experimental",
    "ExperimentalAssistivePromptConfig",
    "ExperimentalCustomToolkit",
    "ExperimentalCustomToolkitTool",
    "ExperimentalCustomTool",
    "ExperimentalPermissions",
    "ManageConnections",
    "MultiAccount",
    "Preload",
    "Search",
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

    connected_accounts: Dict[str, SequenceNotStr[str]]
    """
    The connected accounts to use for the session, as an array of nano-IDs per
    toolkit. This overrides the default behaviour and pins specific connected
    accounts when toolkits are executed. Each account must exist (not deleted or
    disabled) and belong to the same `user_id` as the session. Multi-account
    sessions can pin multiple; non-multi-account sessions are capped at length 1.
    """

    execute: Execute

    experimental: Experimental
    """
    Experimental features - not stable, may be modified or removed in future
    versions.
    """

    manage_connections: ManageConnections
    """Configuration for connection management settings"""

    multi_account: MultiAccount
    """Configure multi-account behavior.

    When enabled, users can connect multiple accounts per toolkit.
    """

    preload: Preload
    """Preload configuration.

    Use an explicit list for frequently used tool slugs, or "all" to dynamically
    expose every app tool allowed by positive toolkits/tools/tags filters.
    """

    search: Search

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
    """Tool-level configuration per toolkit.

    Allows you to enable, disable, or filter by tags for specific tools within each
    toolkit. Every slug passed in `enable` / `disable` must be a valid Composio tool
    slug for that toolkit — invalid or typo'd slugs fail session creation with a
    clear error listing which ones didn't match.
    """

    workbench: Workbench
    """Configuration for workbench behavior"""


class Execute(TypedDict, total=False):
    enable_multi_execute: bool


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

    preload: bool
    """SDK hint for direct custom-tool exposure.

    Not stored in session config; echoed in create/attach responses for inline
    custom definitions.
    """


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

    preload: bool
    """SDK hint for direct custom-tool exposure.

    Not stored in session config; echoed in create/attach responses for inline
    custom definitions.
    """


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

    preload: bool
    """SDK hint for direct custom-tool exposure.

    Not stored in session config; echoed in create/attach responses for inline
    custom definitions.
    """


class ExperimentalPermissions(TypedDict, total=False):
    """Per-tool elicitation permission config.

    Default behavior + per-tool always_allow/always_deny overrides. Mutation via PATCH.
    """

    default: Required[Literal["allow_all", "ask_every_call", "ask_once_per_session"]]
    """Default elicitation behavior when no override matches.

    `allow_all` runs every tool without prompting; `ask_every_call` prompts on each
    invocation; `ask_once_per_session` prompts once and remembers the answer for the
    rest of the session.
    """

    overrides: Dict[str, Literal["always_allow", "always_deny", "ask_once", "ask_always"]]
    """
    Per-tool overrides keyed by `${toolSlug}:${connectedAccountId ?? "__none__"}`,
    plus account-wide overrides keyed by `*:${connectedAccountId ?? "__none__"}`.
    Exact tool overrides take precedence over account-wide overrides. `always_allow`
    skips the prompt and runs the tool; `always_deny` blocks the tool; `ask_once`
    prompts once per session (allow/deny) and remembers; `ask_always` prompts on
    every call with allow-once/allow-session/deny, ignoring any cached session
    allow. Overrides take precedence over `default`.
    """


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

    link_url_overwrite: str
    """
    Experimental base URL override for connection link redirects created from this
    tool-router session. When set, link creation returns
    `${link_url_overwrite}/link/{link_token}` instead of the default Composio
    Connect base URL. Use only when your integration needs links to open through a
    custom Connect host.
    """

    permissions: ExperimentalPermissions
    """Per-tool elicitation permission config.

    Default behavior + per-tool always_allow/always_deny overrides. Mutation via
    PATCH.
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


class MultiAccount(TypedDict, total=False):
    """Configure multi-account behavior.

    When enabled, users can connect multiple accounts per toolkit.
    """

    enable: bool
    """When true, enables multi-account mode for this session.

    When not set, falls back to org/project-level configuration.
    """

    max_accounts_per_toolkit: int
    """Maximum number of connected accounts allowed per toolkit.

    Must be between 2 and 10.
    """

    require_explicit_selection: bool
    """When true, the agent must explicitly select which account to use.

    When false (default), the first/default account is used automatically.
    """


class Preload(TypedDict, total=False):
    """Preload configuration.

    Use an explicit list for frequently used tool slugs, or "all" to dynamically expose every app tool allowed by positive toolkits/tools/tags filters.
    """

    tools: Union[SequenceNotStr[str], str]
    """
    Explicit tool slugs to preload, or "all" to dynamically expose all current and
    future app tools allowed by the positive session filters. "all" is capped at
    1000 tools and is not supported without a positive allowlist.
    """


class Search(TypedDict, total=False):
    enable: bool


class TagsUnionMember1(TypedDict, total=False):
    disable: List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]

    enable: List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]


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

    enable: List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]


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

    sandbox_size: Literal["standard", "medium", "large", "xlarge"]
    """
    Sandbox compute tier: standard (1 vCPU / 1 GB), medium (2 vCPU / 2 GB), large (4
    vCPU / 4 GB), xlarge (8 vCPU / 8 GB). Defaults to standard.
    """
