# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "SessionCreateParams",
    "Connections",
    "Execution",
    "Toolkits",
    "ToolkitsEnabled",
    "ToolkitsDisabled",
    "Tools",
    "ToolsFilters",
    "ToolsFiltersTags",
    "ToolsOverrides",
    "ToolsOverridesEnabled",
    "ToolsOverridesDisabled",
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

    connections: Connections
    """Configuration for connection management settings"""

    execution: Execution
    """
    Configuration for workbench behavior including security restrictions and
    execution limits
    """

    toolkits: Toolkits
    """
    Toolkit configuration - specify either enabled toolkits (allowlist) or disabled
    toolkits (denylist). Mutually exclusive.
    """

    tools: Tools
    """Configuration for tool overrides and filtering"""


class Connections(TypedDict, total=False):
    """Configuration for connection management settings"""

    auto_manage_connections: Optional[bool]
    """Whether to enable the connection manager for automatic connection handling.

    If true, we will provide a tool your agent can use to initiate connections to
    toolkits if it doesnt exist. If set to false, then you have to manage
    connections manually.
    """

    callback_url: str
    """
    The URL to redirect to after a user completes authentication for a connected
    account. This allows you to handle the auth callback in your own application.
    """

    infer_scopes_from_tools: Optional[bool]
    """
    If enabled, authentication scopes will be automatically inferred from the
    specific tools being used in the session. This ensures minimal permissions are
    requested.
    """


class Execution(TypedDict, total=False):
    """
    Configuration for workbench behavior including security restrictions and execution limits
    """

    proxy_execution_enabled: Optional[bool]
    """Whether to allow proxy execute calls in the workbench.

    If false, prevents arbitrary HTTP requests and destructive actions.
    """

    timeout_seconds: float
    """Maximum allowed execution time for workbench operations in seconds.

    If not specified, uses the default timeout.
    """


class ToolkitsEnabled(TypedDict, total=False):
    """Enable only specific toolkits (allowlist)"""

    enabled: Required[SequenceNotStr[str]]
    """Only these specific toolkits will be enabled"""


class ToolkitsDisabled(TypedDict, total=False):
    """Disable specific toolkits (denylist)"""

    disabled: Required[SequenceNotStr[str]]
    """These specific toolkits will be disabled"""


Toolkits: TypeAlias = Union[ToolkitsEnabled, ToolkitsDisabled]


class ToolsFiltersTags(TypedDict, total=False):
    """
    Filter tools by tags such as read_only_hint, non_destructive_hint, open_world_hint, idempotent_hint. Use include to only show tools with specific tags, or exclude to hide tools with specific tags.
    """

    exclude: SequenceNotStr[str]
    """Exclude tools that have any of these tags.

    Tools with any of these tags will be filtered out.
    """

    include: SequenceNotStr[str]
    """Only include tools that have these tags.

    Tools must have at least one of these tags to be included.
    """


class ToolsFilters(TypedDict, total=False):
    """Configuration for filtering available tools based on tags and characteristics"""

    tags: ToolsFiltersTags
    """
    Filter tools by tags such as read_only_hint, non_destructive_hint,
    open_world_hint, idempotent_hint. Use include to only show tools with specific
    tags, or exclude to hide tools with specific tags.
    """


class ToolsOverridesEnabled(TypedDict, total=False):
    enabled: Required[SequenceNotStr[str]]
    """Only these specific tools will be available for this toolkit"""


class ToolsOverridesDisabled(TypedDict, total=False):
    disabled: Required[SequenceNotStr[str]]
    """These specific tools will be disabled for this toolkit"""


ToolsOverrides: TypeAlias = Union[ToolsOverridesEnabled, ToolsOverridesDisabled]


class Tools(TypedDict, total=False):
    """Configuration for tool overrides and filtering"""

    filters: ToolsFilters
    """Configuration for filtering available tools based on tags and characteristics"""

    overrides: Dict[str, ToolsOverrides]
    """
    Tool-level overrides per toolkit - either specify enabled tools (whitelist) or
    disabled tools (blacklist) for each toolkit
    """
