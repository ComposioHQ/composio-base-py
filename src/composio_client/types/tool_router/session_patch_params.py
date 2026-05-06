# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "SessionPatchParams",
    "Execute",
    "Experimental",
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


class SessionPatchParams(TypedDict, total=False):
    auth_configs: Dict[str, str]
    """The auth configs to use for the session.

    This will override the default behavior and use the given auth config when
    specific toolkits are being executed
    """

    connected_accounts: Optional[Dict[str, SequenceNotStr[str]]]
    """
    The connected accounts to use for the session, as an array of nano-IDs per
    toolkit. This overrides the default behaviour and pins specific connected
    accounts when toolkits are executed. Each account must exist (not deleted or
    disabled) and belong to the same `user_id` as the session. Multi-account
    sessions can pin multiple; non-multi-account sessions are capped at length 1.
    """

    execute: Execute

    experimental: Optional[Experimental]

    manage_connections: Optional[ManageConnections]

    multi_account: Optional[MultiAccount]

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

    workbench: Optional[Workbench]


class Execute(TypedDict, total=False):
    enable_multi_execute: bool


class ExperimentalPermissions(TypedDict, total=False):
    """Per-tool elicitation permission config.

    Replaces the stored block when provided.
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

    Replaces the stored block when provided.
    """


class ManageConnections(TypedDict, total=False):
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
    vCPU / 4 GB), xlarge (8 vCPU / 8 GB). Patching this value recreates the sandbox
    on next access — sandbox FS state is lost, but /mnt/files/ R2 mount persists.
    """
