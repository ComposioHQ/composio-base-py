# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["ExecuteInputResponse"]


class ExecuteInputResponse(BaseModel):
    arguments: Optional[Dict[str, Optional[object]]] = None
    """The arguments for the action needed to execute the given task."""

    error: Optional[str] = None
    """The error message if the arguments were not generated successfully."""
