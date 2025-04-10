# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ActionExecutionLogParams", "SearchParam"]


class ActionExecutionLogParams(TypedDict, total=False):
    cursor: Required[Optional[float]]
    """cursor_that_can_be_used_to_paginate_through_the_logs"""

    case_sensitive: bool
    """whether_the_search_is_case_sensitive_or_not"""

    from_: Annotated[float, PropertyInfo(alias="from")]
    """start_time_of_the_logs_in_epoch_time"""

    limit: float
    """number_of_logs_to_return"""

    search_params: Iterable[SearchParam]

    to: float
    """end_time_of_the_logs_in_epoch_time"""


class SearchParam(TypedDict, total=False):
    field: str

    operation: str

    value: str
