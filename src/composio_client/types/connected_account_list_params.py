# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["ConnectedAccountListParams"]


class ConnectedAccountListParams(TypedDict, total=False):
    auth_config_ids: Optional[SequenceNotStr[str]]
    """The auth config ids of the connected accounts"""

    connected_account_ids: Optional[SequenceNotStr[str]]
    """The connected account ids to filter by"""

    cursor: Optional[str]
    """The cursor to paginate through the connected accounts"""

    limit: Optional[float]
    """The limit of the connected accounts to return"""

    order_by: Literal["created_at", "updated_at"]
    """The order by of the connected accounts"""

    order_direction: Literal["asc", "desc"]
    """The order direction of the connected accounts"""

    statuses: Optional[List[Literal["INITIALIZING", "INITIATED", "ACTIVE", "FAILED", "EXPIRED", "INACTIVE"]]]
    """The status of the connected account"""

    toolkit_slugs: Optional[SequenceNotStr[str]]
    """The toolkit slugs of the connected accounts"""

    user_ids: Optional[SequenceNotStr[str]]
    """The user ids of the connected accounts"""
