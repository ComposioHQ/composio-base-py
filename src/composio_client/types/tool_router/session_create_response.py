# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "SessionCreateResponse",
    "Config",
    "ConfigConnections",
    "ConfigExecution",
    "ConfigToolkits",
    "ConfigToolkitsEnabled",
    "ConfigToolkitsDisabled",
    "ConfigTools",
    "ConfigToolsFilters",
    "ConfigToolsFiltersTags",
    "ConfigToolsOverrides",
    "ConfigToolsOverridesEnabled",
    "ConfigToolsOverridesDisabled",
    "Mcp",
]


class ConfigConnections(BaseModel):
    auto_manage_connections: Optional[bool] = None
    """Whether to enable the connection manager for automatic connection handling"""

    callback_url: Optional[str] = None
    """Custom callback URL for connected account auth flows"""

    infer_scopes_from_tools: Optional[bool] = None
    """Whether to auto-infer auth scopes from tools"""


class ConfigExecution(BaseModel):
    proxy_execution_enabled: Optional[bool] = None
    """Whether to allow proxy execute calls in the workbench"""

    timeout_seconds: Optional[float] = None
    """Maximum execution time for workbench operations in seconds"""


class ConfigToolkitsEnabled(BaseModel):
    enabled: List[str]


class ConfigToolkitsDisabled(BaseModel):
    disabled: List[str]


ConfigToolkits: TypeAlias = Union[ConfigToolkitsEnabled, ConfigToolkitsDisabled]


class ConfigToolsFiltersTags(BaseModel):
    exclude: Optional[List[str]] = None
    """Exclude tools that have these tags"""

    include: Optional[List[str]] = None
    """Only include tools that have these tags"""


class ConfigToolsFilters(BaseModel):
    tags: Optional[ConfigToolsFiltersTags] = None
    """Filter tools by specific tags"""


class ConfigToolsOverridesEnabled(BaseModel):
    enabled: List[str]


class ConfigToolsOverridesDisabled(BaseModel):
    disabled: List[str]


ConfigToolsOverrides: TypeAlias = Union[ConfigToolsOverridesEnabled, ConfigToolsOverridesDisabled]


class ConfigTools(BaseModel):
    filters: Optional[ConfigToolsFilters] = None
    """Tool filtering configuration"""

    overrides: Optional[Dict[str, ConfigToolsOverrides]] = None
    """Tool-level overrides per toolkit"""


class Config(BaseModel):
    user_id: str
    """User identifier for this session"""

    auth_configs: Optional[Dict[str, str]] = None
    """Auth config overrides per toolkit"""

    connected_accounts: Optional[Dict[str, str]] = None
    """Connected account overrides per toolkit"""

    connections: Optional[ConfigConnections] = None
    """Connections configuration"""

    execution: Optional[ConfigExecution] = None
    """Execution configuration"""

    toolkits: Optional[ConfigToolkits] = None
    """Toolkit configuration - either enabled list or disabled list"""

    tools: Optional[ConfigTools] = None
    """Tools configuration"""


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
