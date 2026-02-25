# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TriggerListParams", "SearchParam"]


class TriggerListParams(TypedDict, total=False):
    cursor: Optional[str]

    entity_id: Annotated[str, PropertyInfo(alias="entityId")]

    from_: Annotated[Optional[float], PropertyInfo(alias="from")]
    """Start time for logs (epoch timestamp in milliseconds)"""

    include_payload: bool
    """Whether to include payload fields in the response.

    Set to false for faster list views.
    """

    integration_id: Annotated[str, PropertyInfo(alias="integrationId")]

    limit: Optional[float]
    """The limit of trigger logs to return"""

    search: str
    """Search term to filter logs"""

    search_params: Iterable[SearchParam]
    """Advanced search parameters for filtering logs"""

    status: Literal["all", "success", "error"]
    """Filter logs by their status level"""

    time: Literal["5m", "30m", "6h", "1d", "1w", "1month", "1y"]
    """Return logs from the last N time units"""

    to: Optional[float]
    """End time for logs (epoch timestamp in milliseconds)"""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """Filter logs by user ID"""


class SearchParam(TypedDict, total=False):
    field: str

    operation: str

    value: str
