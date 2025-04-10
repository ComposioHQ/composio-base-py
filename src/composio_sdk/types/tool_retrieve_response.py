# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ToolRetrieveResponse", "Toolkit"]


class Toolkit(BaseModel):
    logo: str

    name: str

    slug: str


class ToolRetrieveResponse(BaseModel):
    available_versions: List[str]

    description: str

    input_parameters: Dict[str, Optional[object]]

    name: str

    output_parameters: Dict[str, Optional[object]]

    slug: str

    tags: List[str]

    toolkit: Toolkit

    version: str
