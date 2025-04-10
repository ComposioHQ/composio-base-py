# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ConnectedAccountListParams"]


class ConnectedAccountListParams(TypedDict, total=False):
    auth_config_id: str
    """The auth config id of the connected account"""

    cursor: Optional[float]
    """The cursor to paginate through the connected accounts"""

    limit: Optional[float]
    """The limit of the connected accounts to return"""

    order_by: Literal["created_at", "updated_at"]
    """The order by of the connected accounts"""

    status: Literal["ACTIVE", "INACTIVE", "DELETED", "INITIATED", "EXPIRED", "FAILED"]
    """The status of the connected account"""

    toolkit_slug: str
    """The toolkit slug of the connected account"""

    user_id: str
    """The user id of the connected account"""
