# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["TriggersTypeRetrieveResponse", "Toolkit"]


class Toolkit(BaseModel):
    logo: str

    name: str

    uuid: str


class TriggersTypeRetrieveResponse(BaseModel):
    config: Dict[str, Optional[object]]

    description: str

    instructions: str

    name: str

    payload: Dict[str, Optional[object]]

    slug: str

    toolkit: Toolkit
