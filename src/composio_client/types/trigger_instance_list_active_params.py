# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TriggerInstanceListActiveParams"]


class TriggerInstanceListActiveParams(TypedDict, total=False):
    query_auth_config_ids_1: Annotated[Optional[List[str]], PropertyInfo(alias="auth_config_ids")]
    """Array of auth config IDs to filter triggers by"""

    query_auth_config_ids_2: Annotated[str, PropertyInfo(alias="authConfigIds")]

    query_connected_account_ids_1: Annotated[Optional[List[str]], PropertyInfo(alias="connected_account_ids")]
    """Array of connected account IDs to filter triggers by"""

    query_connected_account_ids_2: Annotated[str, PropertyInfo(alias="connectedAccountIds")]

    cursor: str
    """Cursor for pagination.

    The cursor is a base64 encoded string of the page and limit. The page is the
    page number and the limit is the number of items per page. The cursor is used to
    paginate through the items. The cursor is not required for the first page.
    """

    deprecated_auth_config_uuids: Annotated[Optional[List[str]], PropertyInfo(alias="deprecatedAuthConfigUuids")]
    """Array of auth config UUIDs to filter triggers by"""

    deprecated_connected_account_uuids: Annotated[
        Optional[List[str]], PropertyInfo(alias="deprecatedConnectedAccountUuids")
    ]
    """Array of connected account UUIDs to filter triggers by"""

    limit: Optional[float]
    """Number of items per page"""

    page: float
    """Page number for pagination. Starts from 1."""

    query_show_disabled_1: Annotated[Optional[bool], PropertyInfo(alias="show_disabled")]
    """When set to true, includes disabled triggers in the response."""

    query_show_disabled_2: Annotated[str, PropertyInfo(alias="showDisabled")]

    query_trigger_ids_1: Annotated[Optional[List[str]], PropertyInfo(alias="trigger_ids")]
    """Array of trigger IDs to filter triggers by"""

    query_trigger_names_1: Annotated[Optional[List[str]], PropertyInfo(alias="trigger_names")]
    """Array of trigger names to filter triggers by"""

    query_trigger_ids_2: Annotated[str, PropertyInfo(alias="triggerIds")]

    query_trigger_names_2: Annotated[str, PropertyInfo(alias="triggerNames")]
