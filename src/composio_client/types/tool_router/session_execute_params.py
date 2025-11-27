# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SessionExecuteParams"]


class SessionExecuteParams(TypedDict, total=False):
    tool_slug: Required[str]
    """The unique slug identifier of the tool to execute"""

    arguments: Dict[str, Optional[object]]
    """The arguments required by the tool"""

    x_session_access_key: Annotated[str, PropertyInfo(alias="x-session-access-key")]
    """Session access key for sandbox/workbench authentication.

    Alternative to x-api-key for internal tool router endpoints.
    """
