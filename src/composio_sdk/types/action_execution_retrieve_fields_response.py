# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ActionExecutionRetrieveFieldsResponse", "Field"]


class Field(BaseModel):
    id: str
    """The id of the field"""

    display_name: str = FieldInfo(alias="displayName")
    """The display name of the field"""

    type: str
    """The type of the field"""

    regex: Optional[str] = None
    """The regex of the field"""


class ActionExecutionRetrieveFieldsResponse(BaseModel):
    fields: Dict[str, List[Field]]
