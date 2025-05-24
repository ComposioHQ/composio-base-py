# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ToolGetInputResponse"]


class ToolGetInputResponse(BaseModel):
    arguments: Optional[Dict[str, Optional[object]]] = None
    """
    Key-value pairs of arguments required by the tool to accomplish the described
    task
    """

    error: Optional[str] = None
    """Error message if the arguments could not be generated (null if successful)"""
