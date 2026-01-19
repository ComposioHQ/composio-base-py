# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "SessionCreateResponse",
    "Config",
    "ConfigManageConnections",
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
]


class ConfigManageConnections(BaseModel):
    """Manage connections configuration"""

    callback_url: Optional[str] = None
    """Custom callback URL for connected account auth flows"""

    enable_wait_for_connections: Optional[bool] = None
    """Enable the COMPOSIO_WAIT_FOR_CONNECTIONS tool for polling connection status.

    Default false. May not work reliably with GPT models.
    """

    enabled: Optional[bool] = None
    """Whether to enable the connection manager for automatic connection handling"""


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


class Experimental(BaseModel):
    """Experimental features including the generated system prompt.

    Only returned on session creation, not on GET.
    """

    assistive_prompt: str
    """
    The assistive system prompt to inject into your agent for optimal tool router
    usage
    """


class SessionCreateResponse(BaseModel):
    config: Config
    """The session configuration including user, toolkits, and overrides"""

    mcp: Mcp

    session_id: str
    """The identifier of the session"""

    tool_router_tools: List[str]
    """List of available tools in this session"""

    experimental: Optional[Experimental] = None
    """Experimental features including the generated system prompt.

    Only returned on session creation, not on GET.
    """
