# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ToolProxyResponse"]


class ToolProxyResponse(BaseModel):
    status: float

    data: Optional[object] = None

    headers: Optional[Dict[str, str]] = None
