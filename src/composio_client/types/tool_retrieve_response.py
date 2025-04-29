# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolRetrieveResponse", "Deprecated", "Toolkit"]


class Deprecated(BaseModel):
    display_name: str = FieldInfo(alias="displayName")
    """The display name of the tool"""

    is_action_deprecated: bool = FieldInfo(alias="isActionDeprecated")
    """Whether the action is deprecated"""


class Toolkit(BaseModel):
    logo: str

    name: str

    slug: str


class ToolRetrieveResponse(BaseModel):
    available_versions: List[str]

    deprecated: Deprecated

    description: str

    input_parameters: Dict[str, Optional[object]]

    name: str

    no_auth: bool

    output_parameters: Dict[str, Optional[object]]

    slug: str

    tags: List[str]

    toolkit: Toolkit

    version: str
