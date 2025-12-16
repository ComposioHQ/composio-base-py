# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["TriggerInstanceListActiveParams"]


class TriggerInstanceListActiveParams(TypedDict, total=False):
    query_auth_config_ids_1: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="auth_config_ids")]
    """Array of auth config IDs to filter triggers by"""

    query_auth_config_ids_2: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="authConfigIds")]
    """DEPRECATED: This parameter will be removed in a future version.

    Please use auth_config_ids instead.
    """

    query_connected_account_ids_1: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="connected_account_ids")]
    """Array of connected account IDs to filter triggers by"""

    query_connected_account_ids_2: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="connectedAccountIds")]
    """DEPRECATED: This parameter will be removed in a future version.

    Please use connected_account_ids instead.
    """

    cursor: str
    """Cursor for pagination.

    The cursor is a base64 encoded string of the page and limit. The page is the
    page number and the limit is the number of items per page. The cursor is used to
    paginate through the items. The cursor is not required for the first page.
    """

    deprecated_auth_config_uuids: Annotated[
        Optional[SequenceNotStr[str]], PropertyInfo(alias="deprecatedAuthConfigUuids")
    ]
    """DEPRECATED: This parameter will be removed in a future version.

    Please use auth_config_ids instead.
    """

    deprecated_connected_account_uuids: Annotated[
        Optional[SequenceNotStr[str]], PropertyInfo(alias="deprecatedConnectedAccountUuids")
    ]
    """DEPRECATED: This parameter will be removed in a future version.

    Please use connected_account_ids instead.
    """

    limit: Optional[float]
    """Number of items per page, max allowed is 1000"""

    page: float
    """Page number for pagination. Starts from 1."""

    query_show_disabled_1: Annotated[Optional[bool], PropertyInfo(alias="show_disabled")]
    """When set to true, includes disabled triggers in the response."""

    query_show_disabled_2: Annotated[Optional[bool], PropertyInfo(alias="showDisabled")]
    """DEPRECATED: This parameter will be removed in a future version.

    Please use show_disabled instead.
    """

    query_trigger_ids_1: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="trigger_ids")]
    """Array of trigger IDs to filter triggers by"""

    query_trigger_names_1: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="trigger_names")]
    """Array of trigger names to filter triggers by"""

    query_trigger_ids_2: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="triggerIds")]
    """DEPRECATED: This parameter will be removed in a future version.

    Please use trigger_ids instead.
    """

    query_trigger_names_2: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="triggerNames")]
    """DEPRECATED: This parameter will be removed in a future version.

    Please use trigger_names instead.
    """
