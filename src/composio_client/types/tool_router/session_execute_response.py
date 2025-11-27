# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["SessionExecuteResponse"]


class SessionExecuteResponse(BaseModel):
    data: Dict[str, Optional[object]]
    """The data returned by the tool execution"""

    error: Optional[str] = None
    """Error message if the execution failed, null otherwise"""

    log_id: str
    """Unique identifier for the execution log"""
