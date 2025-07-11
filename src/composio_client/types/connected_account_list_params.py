# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ConnectedAccountListParams"]


class ConnectedAccountListParams(TypedDict, total=False):
    auth_config_ids: Optional[List[str]]
    """The auth config ids of the connected accounts"""

    cursor: Optional[str]
    """The cursor to paginate through the connected accounts"""

    labels: Optional[List[str]]
    """The labels of the connected accounts"""

    limit: Optional[float]
    """The limit of the connected accounts to return"""

    order_by: Literal["created_at", "updated_at"]
    """The order by of the connected accounts"""

    statuses: Optional[List[Literal["INITIALIZING", "INITIATED", "ACTIVE", "FAILED", "EXPIRED", "INACTIVE"]]]
    """The status of the connected account"""

    toolkit_slugs: Optional[List[str]]
    """The toolkit slugs of the connected accounts"""

    user_ids: Optional[List[str]]
    """The user ids of the connected accounts"""
