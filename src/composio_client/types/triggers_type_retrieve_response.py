# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["TriggersTypeRetrieveResponse", "Toolkit"]


class Toolkit(BaseModel):
    logo: str
    """URL to the toolkit logo image"""

    name: str
    """Name of the toolkit that contains this trigger"""

    uuid: str
    """Unique identifier for the associated toolkit"""


class TriggersTypeRetrieveResponse(BaseModel):
    config: Dict[str, Optional[object]]
    """Configuration parameters required for the trigger"""

    description: str
    """Detailed description of what the trigger does and when it fires"""

    instructions: str
    """Step-by-step instructions on how to set up and use this trigger"""

    name: str
    """Display name of the trigger type"""

    payload: Dict[str, Optional[object]]
    """Structure of the event payload that will be delivered by this trigger"""

    slug: str
    """Unique identifier for the trigger type"""

    toolkit: Toolkit
    """Information about the toolkit that contains this trigger"""
