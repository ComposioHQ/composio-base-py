# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolRetrieveResponse", "Deprecated", "Toolkit"]


class Deprecated(BaseModel):
    display_name: str = FieldInfo(alias="displayName")
    """The display name of the tool"""

    is_deprecated: bool
    """Whether the action is deprecated"""


class Toolkit(BaseModel):
    logo: str
    """URL to the toolkit logo image"""

    name: str
    """Human-readable name of the parent toolkit"""

    slug: str
    """Unique identifier of the parent toolkit"""


class ToolRetrieveResponse(BaseModel):
    available_versions: List[str]
    """List of all available versions for this tool"""

    deprecated: Deprecated

    description: str
    """Detailed description of what the tool does"""

    input_parameters: Dict[str, Optional[object]]
    """Schema definition of required input parameters for the tool"""

    name: str
    """Human-readable name of the tool"""

    no_auth: bool
    """Indicates if the tool can be used without authentication"""

    output_parameters: Dict[str, Optional[object]]
    """Schema definition of return values from the tool"""

    slug: str
    """Unique identifier for the tool"""

    tags: List[str]
    """List of tags associated with the tool for categorization"""

    toolkit: Toolkit

    version: str
    """Current version of the tool"""
