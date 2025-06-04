# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AdminRefreshAuthTokensParams"]


class AdminRefreshAuthTokensParams(TypedDict, total=False):
    connection_ids: Required[Annotated[List[str], PropertyInfo(alias="connectionIds")]]
    """List of connection identifiers that need token refresh"""

    x_composio_admin_token: Required[Annotated[str, PropertyInfo(alias="x-composio-admin-token")]]
    """Admin authentication token required for administrative operations"""

    parallelism: int
    """Controls processing speed and system load.

    Higher values process faster but increase load.
    """
