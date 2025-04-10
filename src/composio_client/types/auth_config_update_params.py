# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AuthConfigUpdateParams", "AuthConfig"]


class AuthConfigUpdateParams(TypedDict, total=False):
    auth_config: Required[AuthConfig]


class AuthConfig(TypedDict, total=False):
    credentials: Dict[str, Optional[object]]
    """Authentication configuration"""
