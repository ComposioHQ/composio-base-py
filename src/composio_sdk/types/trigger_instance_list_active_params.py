# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TriggerInstanceListActiveParams"]


class TriggerInstanceListActiveParams(TypedDict, total=False):
    auth_config_ids: Annotated[str, PropertyInfo(alias="authConfigIds")]
    """Comma-separated list of auth config IDs to filter triggers by"""

    connected_account_ids: Annotated[str, PropertyInfo(alias="connectedAccountIds")]
    """Comma-separated list of connected account IDs to filter triggers by"""

    limit: float
    """Number of items to return per page."""

    page: float
    """Page number for pagination. Starts from 1."""

    show_disabled: Annotated[Optional[bool], PropertyInfo(alias="showDisabled")]
    """When set to true, includes disabled triggers in the response."""

    trigger_ids: Annotated[str, PropertyInfo(alias="triggerIds")]
    """Comma-separated list of trigger IDs to filter triggers by"""

    trigger_names: Annotated[str, PropertyInfo(alias="triggerNames")]
    """Comma-separated list of trigger names to filter triggers by"""
