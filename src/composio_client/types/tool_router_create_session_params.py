# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ToolRouterCreateSessionParams", "Config", "ConfigToolkit"]


class ToolRouterCreateSessionParams(TypedDict, total=False):
    user_id: Required[str]
    """Unique user identifier for the session owner"""

    config: Config
    """Session configuration including enabled toolkits and their auth configs"""


class ConfigToolkit(TypedDict, total=False):
    toolkit: Required[str]
    """Toolkit identifier (e.g., gmail, slack, github)"""

    auth_config_id: str
    """Specific auth configuration ID for this toolkit"""


class Config(TypedDict, total=False):
    """Session configuration including enabled toolkits and their auth configs"""

    manually_manage_connections: Optional[bool]
    """Whether to manually manage connections"""

    toolkits: Iterable[ConfigToolkit]
    """Array of toolkit configurations with optional auth configs"""
