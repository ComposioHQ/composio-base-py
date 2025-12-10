# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TriggerInstanceUpsertParams"]


class TriggerInstanceUpsertParams(TypedDict, total=False):
    connected_account_id: str
    """Connected account nanoid"""

    connected_auth_id: Annotated[str, PropertyInfo(alias="connectedAuthId")]
    """DEPRECATED: This parameter will be removed in a future version.

    Please use connected_account_id instead.
    """

    toolkit_versions: Union[str, Dict[str, str], None]
    """Toolkit version specification.

    Supports "latest" string or a record mapping toolkit slugs to specific versions.
    """

    body_trigger_config_1: Annotated[Dict[str, Optional[object]], PropertyInfo(alias="trigger_config")]
    """Trigger configuration"""

    body_trigger_config_2: Annotated[Dict[str, Optional[object]], PropertyInfo(alias="triggerConfig")]
    """DEPRECATED: This parameter will be removed in a future version.

    Please use trigger_config instead.
    """

    version: str
    """DEPRECATED: This parameter will be removed in a future version.

    Please use toolkit_versions instead.
    """
