# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "SessionConfigHistoryResponse",
    "Item",
    "ItemConfig",
    "ItemConfigExecute",
    "ItemConfigPreload",
    "ItemConfigSearch",
    "ItemConfigManageConnections",
    "ItemConfigMultiAccount",
    "ItemConfigTags",
    "ItemConfigToolkits",
    "ItemConfigToolkitsEnabled",
    "ItemConfigToolkitsDisabled",
    "ItemConfigTools",
    "ItemConfigToolsEnabled",
    "ItemConfigToolsDisabled",
    "ItemConfigToolsTags",
    "ItemConfigToolsTagsTags",
    "ItemConfigWorkbench",
]


class ItemConfigExecute(BaseModel):
    """Execute helper configuration"""

    enable_multi_execute: Optional[bool] = None


class ItemConfigPreload(BaseModel):
    """Preload configuration.

    Explicit slugs are returned as an array; dynamic preload is returned as "all".
    """

    tools: Union[List[str], Literal["all"]]
    """
    Explicit preloaded tool slugs, or "all" when the session dynamically exposes all
    app tools allowed by its filters.
    """


class ItemConfigSearch(BaseModel):
    """Search helper configuration"""

    enable: Optional[bool] = None


class ItemConfigManageConnections(BaseModel):
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


class ItemConfigMultiAccount(BaseModel):
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


class ItemConfigTags(BaseModel):
    """MCP tool annotation hints for filtering tools with enabled/disabled support.

    enabled: tags that the tool must have at least one of. disabled: tags that the tool must NOT have any of. Both conditions must be satisfied.
    """

    disabled: Optional[List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]] = None
    """Tags that the tool must NOT have any of"""

    enabled: Optional[List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]] = None
    """Tags that the tool must have at least one of"""


class ItemConfigToolkitsEnabled(BaseModel):
    enabled: List[str]


class ItemConfigToolkitsDisabled(BaseModel):
    disabled: List[str]


ItemConfigToolkits: TypeAlias = Union[ItemConfigToolkitsEnabled, ItemConfigToolkitsDisabled]


class ItemConfigToolsEnabled(BaseModel):
    enabled: List[str]


class ItemConfigToolsDisabled(BaseModel):
    disabled: List[str]


class ItemConfigToolsTagsTags(BaseModel):
    disabled: Optional[List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]] = None
    """Tags that the tool must NOT have any of"""

    enabled: Optional[List[Literal["readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"]]] = None
    """Tags that the tool must have at least one of"""


class ItemConfigToolsTags(BaseModel):
    tags: ItemConfigToolsTagsTags


ItemConfigTools: TypeAlias = Union[ItemConfigToolsEnabled, ItemConfigToolsDisabled, ItemConfigToolsTags]


class ItemConfigWorkbench(BaseModel):
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


class ItemConfig(BaseModel):
    """The session configuration at this version"""

    execute: ItemConfigExecute
    """Execute helper configuration"""

    preload: ItemConfigPreload
    """Preload configuration.

    Explicit slugs are returned as an array; dynamic preload is returned as "all".
    """

    search: ItemConfigSearch
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

    manage_connections: Optional[ItemConfigManageConnections] = None
    """Manage connections configuration"""

    multi_account: Optional[ItemConfigMultiAccount] = None
    """Multi-account configuration for this session."""

    tags: Optional[ItemConfigTags] = None
    """MCP tool annotation hints for filtering tools with enabled/disabled support.

    enabled: tags that the tool must have at least one of. disabled: tags that the
    tool must NOT have any of. Both conditions must be satisfied.
    """

    toolkits: Optional[ItemConfigToolkits] = None
    """Toolkit configuration - either enabled list or disabled list"""

    tools: Optional[Dict[str, ItemConfigTools]] = None
    """Tool-level configuration per toolkit"""

    workbench: Optional[ItemConfigWorkbench] = None
    """Workbench configuration"""


class Item(BaseModel):
    config: ItemConfig
    """The session configuration at this version"""

    created_at: datetime
    """ISO timestamp.

    For history rows, when the entry was archived (i.e. the moment the version was
    superseded by a PATCH).
    """

    is_current: bool
    """True only for the live (current) session config, present on the first page.

    False for archived history rows.
    """

    version: int
    """The config version this entry represents"""


class SessionConfigHistoryResponse(BaseModel):
    current_page: float

    items: List[Item]

    total_items: float

    total_pages: float

    next_cursor: Optional[str] = None
