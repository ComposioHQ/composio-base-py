# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TriggerInstanceUpsertParams"]


class TriggerInstanceUpsertParams(TypedDict, total=False):
    connected_account_id: str
    """Connected account nanoid"""

    body_trigger_config_1: Annotated[Dict[str, Optional[object]], PropertyInfo(alias="trigger_config")]
    """Trigger configuration"""

    body_trigger_config_2: Annotated[Dict[str, Optional[object]], PropertyInfo(alias="triggerConfig")]
    """Trigger configuration (deprecated)"""
