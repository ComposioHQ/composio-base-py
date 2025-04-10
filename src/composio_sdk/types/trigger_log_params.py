# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TriggerLogParams"]


class TriggerLogParams(TypedDict, total=False):
    cursor: Required[Optional[str]]
    """cursor that can be used to paginate through the logs"""

    entity_id: Annotated[str, PropertyInfo(alias="entityId")]

    integration_id: Annotated[str, PropertyInfo(alias="integrationId")]

    limit: float
    """number of logs to return"""

    search: str
    """Search term to filter logs"""

    status: Literal["all", "success", "error"]
    """Filter logs by their status level"""

    time: Literal["5m", "30m", "6h", "1d", "1w", "1month", "1y"]
    """Return logs from the last N time units"""
