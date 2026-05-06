# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "SessionRetrieveResponse",
    "Config",
    "ConfigExecute",
    "ConfigPreload",
    "ConfigSearch",
    "ConfigManageConnections",
    "ConfigMultiAccount",
    "ConfigTags",
    "ConfigToolkits",
    "ConfigToolkitsEnabled",
    "ConfigToolkitsDisabled",
    "ConfigTools",
    "ConfigToolsEnabled",
    "ConfigToolsDisabled",
    "ConfigToolsTags",
    "ConfigToolsTagsTags",
    "ConfigWorkbench",
    "Mcp",
    "Experimental",
    "ExperimentalCustomToolkit",
    "ExperimentalCustomToolkitTool",
    "ExperimentalCustomTool",
    "Warning",
]


class ConfigExecute(BaseModel):
    """Execute helper configuration"""

    enable_multi_execute: Optional[bool] = None


class ConfigPreload(BaseModel):
    """Preload configuration.

    Explicit slugs are returned as an array; dynamic preload is returned as "all".
    """

    tools: Union[List[str], Literal["all"]]
    """
    Explicit preloaded tool slugs, or "all" when the session dynamically exposes all
    app tools allowed by its filters.
    """


class ConfigSearch(BaseModel):
    """Search helper configuration"""

    enable: Optional[bool] = None


class ConfigManageConnections(BaseModel):
    """Manage connections configuration"""

    callback_url: Optional[str] = None
    """Custom callback URL for connected account auth flows"""

    enable_connection_removal: Optional[bool] = None
    """Enable the "remove" action in COMPOSIO_MANAGE_CONNECTIONS. Default true."""

    enable_wait_for_connections: Optional[bool] = None
    """Enable the COMPOSIO_WAIT_FOR_CONNECTIONS tool for polling connection status.

    Default false. May not work reliably with GPT models.
    """

    enabled: Optional[bool] = None
    """Whether to enable the connection manager for automatic connection handling"""


class ConfigMultiAccount(BaseModel):
    """Multi-account configuration for this session."""

    enable: Optional[bool] = None
    """When true, enables multi-account mode for this session.

    When not set, falls back to org/project-level configuration.
    """

    max_accounts_per_toolkit: Optional[int] = None
    """Maximum number of connected accounts allowed per toolkit.

    Defaults to 5 when multi-account is enabled.
    """

    require_explicit_selection: Optional[bool] = None
    """
    When true, require explicit account selection when multiple accounts are
    connected. When false (default), use the first/default account.
    """


class ConfigTags(BaseModel):
    """MCP tool annotation hints for filtering tools with enabled/disabled support.

    enabled: tags that the tool must have at least one of. disabled: tags that the tool must NOT have any of. Both conditions must be satisfied.
    """

    disabled: Optional[List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]] = None
    """Tags that the tool must NOT have any of"""

    enabled: Optional[List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]] = None
    """Tags that the tool must have at least one of"""


class ConfigToolkitsEnabled(BaseModel):
    enabled: List[str]


class ConfigToolkitsDisabled(BaseModel):
    disabled: List[str]


ConfigToolkits: TypeAlias = Union[ConfigToolkitsEnabled, ConfigToolkitsDisabled]


class ConfigToolsEnabled(BaseModel):
    enabled: List[str]


class ConfigToolsDisabled(BaseModel):
    disabled: List[str]


class ConfigToolsTagsTags(BaseModel):
    disabled: Optional[List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]] = None
    """Tags that the tool must NOT have any of"""

    enabled: Optional[List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]] = None
    """Tags that the tool must have at least one of"""


class ConfigToolsTags(BaseModel):
    tags: ConfigToolsTagsTags


ConfigTools: TypeAlias = Union[ConfigToolsEnabled, ConfigToolsDisabled, ConfigToolsTags]


class ConfigWorkbench(BaseModel):
    """Workbench configuration"""

    auto_offload_threshold: Optional[float] = None
    """
    Character threshold after which tool execution response are saved to a file in
    workbench. Default is 20k.
    """

    enable: Optional[bool] = None
    """Whether the workbench (code execution sandbox) is enabled.

    When false, COMPOSIO_REMOTE_WORKBENCH and COMPOSIO_REMOTE_BASH_TOOL are not
    exposed.
    """

    proxy_execution_enabled: Optional[bool] = None
    """Whether proxy execution is enabled in the workbench"""

    sandbox_size: Optional[Literal["standard", "medium", "large", "xlarge"]] = None
    """
    Sandbox compute tier: standard (1 vCPU / 1 GB), medium (2 vCPU / 2 GB), large (4
    vCPU / 4 GB), xlarge (8 vCPU / 8 GB). Defaults to standard.
    """


class Config(BaseModel):
    """The configuration used to create this session"""

    execute: ConfigExecute
    """Execute helper configuration"""

    preload: ConfigPreload
    """Preload configuration.

    Explicit slugs are returned as an array; dynamic preload is returned as "all".
    """

    search: ConfigSearch
    """Search helper configuration"""

    user_id: str
    """User identifier for this session"""

    auth_configs: Optional[Dict[str, str]] = None
    """Auth config overrides per toolkit"""

    connected_accounts: Optional[Dict[str, List[str]]] = None
    """Per-toolkit connected account overrides (array of nano-IDs).

    Multi-account sessions can pin more than one account per toolkit; otherwise
    length is 1.
    """

    manage_connections: Optional[ConfigManageConnections] = None
    """Manage connections configuration"""

    multi_account: Optional[ConfigMultiAccount] = None
    """Multi-account configuration for this session."""

    tags: Optional[ConfigTags] = None
    """MCP tool annotation hints for filtering tools with enabled/disabled support.

    enabled: tags that the tool must have at least one of. disabled: tags that the
    tool must NOT have any of. Both conditions must be satisfied.
    """

    toolkits: Optional[ConfigToolkits] = None
    """Toolkit configuration - either enabled list or disabled list"""

    tools: Optional[Dict[str, ConfigTools]] = None
    """Tool-level configuration per toolkit"""

    workbench: Optional[ConfigWorkbench] = None
    """Workbench configuration"""


class Mcp(BaseModel):
    type: Literal["http"]
    """The type of the MCP server. Can be http"""

    url: str
    """The URL of the MCP server"""


class ExperimentalCustomToolkitTool(BaseModel):
    description: str

    input_schema: Dict[str, Optional[object]]

    name: str

    original_slug: str
    """Original tool slug as provided by the user"""

    slug: str
    """Prefixed tool slug (e.g. LOCAL_CRM_FIND_CUSTOMER)"""

    output_schema: Optional[Dict[str, Optional[object]]] = None


class ExperimentalCustomToolkit(BaseModel):
    description: str

    name: str

    slug: str

    tools: List[ExperimentalCustomToolkitTool]


class ExperimentalCustomTool(BaseModel):
    description: str

    input_schema: Dict[str, Optional[object]]

    name: str

    original_slug: str
    """Original tool slug as provided by the user"""

    slug: str
    """Prefixed tool slug (e.g. LOCAL_GMAIL_GET_IMPORTANT_EMAILS)"""

    extends_toolkit: Optional[str] = None

    output_schema: Optional[Dict[str, Optional[object]]] = None


class Experimental(BaseModel):
    """Experimental features"""

    assistive_prompt: Optional[str] = None
    """The assistive system prompt for the tool router session"""

    custom_toolkits: Optional[List[ExperimentalCustomToolkit]] = None
    """User-defined custom toolkits with grouped tools (no-auth)"""

    custom_tools: Optional[List[ExperimentalCustomTool]] = None
    """Custom tools — standalone or extending Composio toolkits"""


class Warning(BaseModel):
    code: Literal["PRELOAD_TOOLS_HIGH_CONTEXT_USAGE"]
    """Stable machine code identifying the advisory. Safe to switch on in client code."""

    message: str
    """Human-readable description of the advisory.

    Suitable for logging or surfacing to end users.
    """


class SessionRetrieveResponse(BaseModel):
    config: Config
    """The configuration used to create this session"""

    config_version: int
    """Monotonic version of the config.

    Incremented on each PATCH. Use for optimistic concurrency control.
    """

    mcp: Mcp

    session_id: str
    """The identifier of the session"""

    tool_router_tools: List[str]
    """List of available tools in this session"""

    experimental: Optional[Experimental] = None
    """Experimental features"""

    warnings: Optional[List[Warning]] = None
    """
    Advisory list — the session exists and is usable, but the listed issues may
    warrant attention.
    """
