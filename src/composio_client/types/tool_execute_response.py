# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ToolExecuteResponse"]


class ToolExecuteResponse(BaseModel):
    data: Dict[str, Optional[object]]
    """Tool execution output data that varies based on the specific tool"""

    error: Optional[str] = None
    """Error message if the tool execution was not successful (null if successful)"""

    successful: bool
    """Indicates if the tool execution was successful"""

    log_id: Optional[str] = None
    """Unique identifier for the execution log (useful for debugging and support)"""

    session_info: Optional[object] = None
    """Optional session information for tools that return session context"""
