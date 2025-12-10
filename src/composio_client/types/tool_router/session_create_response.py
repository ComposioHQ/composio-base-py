# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "SessionCreateResponse",
    "Config",
    "ConfigManageConnections",
    "ConfigToolkits",
    "ConfigToolkitsEnabled",
    "ConfigToolkitsDisabled",
    "ConfigTools",
    "ConfigToolsEnabled",
    "ConfigToolsDisabled",
    "ConfigToolsTags",
    "ConfigWorkbench",
    "Mcp",
]


class ConfigManageConnections(BaseModel):
    """Manage connections configuration"""

    callback_url: Optional[str] = None
    """Custom callback URL for connected account auth flows"""

    enabled: Optional[bool] = None
    """Whether to enable the connection manager for automatic connection handling"""


class ConfigToolkitsEnabled(BaseModel):
    enabled: List[str]


class ConfigToolkitsDisabled(BaseModel):
    disabled: List[str]


ConfigToolkits: TypeAlias = Union[ConfigToolkitsEnabled, ConfigToolkitsDisabled]


class ConfigToolsEnabled(BaseModel):
    enabled: List[str]


class ConfigToolsDisabled(BaseModel):
    disabled: List[str]


class ConfigToolsTags(BaseModel):
    tags: List[str]


ConfigTools: TypeAlias = Union[ConfigToolsEnabled, ConfigToolsDisabled, ConfigToolsTags]


class ConfigWorkbench(BaseModel):
    """Workbench configuration"""

    auto_offload_threshold: Optional[float] = None
    """
    Character threshold after which tool execution response are saved to a file in
    workbench. Default is 20k.
    """

    proxy_execution_enabled: Optional[bool] = None
    """Whether proxy execution is enabled in the workbench"""


class Config(BaseModel):
    """The session configuration including user, toolkits, and overrides"""

    user_id: str
    """User identifier for this session"""

    auth_configs: Optional[Dict[str, str]] = None
    """Auth config overrides per toolkit"""

    connected_accounts: Optional[Dict[str, str]] = None
    """Connected account overrides per toolkit"""

    manage_connections: Optional[ConfigManageConnections] = None
    """Manage connections configuration"""

    tags: Optional[List[Literal["readOnlyHint", "destructiveHint", "idempotentHint"]]] = None
    """MCP tool annotation hints for filtering tools.

    readOnlyHint: tool does not modify environment. destructiveHint: tool may
    perform destructive updates. idempotentHint: tool may interact with external
    entities.
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


class SessionCreateResponse(BaseModel):
    config: Config
    """The session configuration including user, toolkits, and overrides"""

    mcp: Mcp

    session_id: str
    """The identifier of the session"""

    tool_router_tools: List[
        Literal[
            "COMPOSIO_SEARCH_TOOLS",
            "COMPOSIO_MULTI_EXECUTE_TOOL",
            "COMPOSIO_MANAGE_CONNECTIONS",
            "COMPOSIO_REMOTE_WORKBENCH",
            "COMPOSIO_REMOTE_BASH_TOOL",
            "COMPOSIO_GET_TOOL_SCHEMAS",
        ]
    ]
    """List of available tools in this session"""
