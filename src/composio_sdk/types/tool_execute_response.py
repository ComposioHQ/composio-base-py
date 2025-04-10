# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ToolExecuteResponse"]


class ToolExecuteResponse(BaseModel):
    data: Dict[str, Optional[object]]

    error: Optional[str] = None

    successful: bool

    log_id: Optional[str] = None

    session_info: Optional[object] = None
