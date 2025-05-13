# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TriggerInstanceListActiveParams"]


class TriggerInstanceListActiveParams(TypedDict, total=False):
    auth_config_ids: Annotated[Optional[List[str]], PropertyInfo(alias="authConfigIds")]
    """Array of auth config IDs to filter triggers by"""

    connected_account_ids: Annotated[Optional[List[str]], PropertyInfo(alias="connectedAccountIds")]
    """Array of connected account IDs to filter triggers by"""

    deprecated_auth_config_uuids: Annotated[Optional[List[str]], PropertyInfo(alias="deprecatedAuthConfigUuids")]
    """Array of auth config UUIDs to filter triggers by"""

    deprecated_connected_account_uuids: Annotated[
        Optional[List[str]], PropertyInfo(alias="deprecatedConnectedAccountUuids")
    ]
    """Array of connected account UUIDs to filter triggers by"""

    limit: float
    """Number of items to return per page."""

    page: float
    """Page number for pagination. Starts from 1."""

    show_disabled: Annotated[Optional[str], PropertyInfo(alias="showDisabled")]
    """When set to true, includes disabled triggers in the response."""

    trigger_ids: Annotated[Optional[List[str]], PropertyInfo(alias="triggerIds")]
    """Array of trigger IDs to filter triggers by"""

    trigger_names: Annotated[Optional[List[str]], PropertyInfo(alias="triggerNames")]
    """Array of trigger names to filter triggers by"""
