# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TriggerInstanceUpsertParams"]


class TriggerInstanceUpsertParams(TypedDict, total=False):
    connected_auth_id: Required[Annotated[str, PropertyInfo(alias="connectedAuthId")]]
    """Connection ID"""

    trigger_config: Required[Annotated[Dict[str, Optional[object]], PropertyInfo(alias="triggerConfig")]]
    """Trigger configuration"""
