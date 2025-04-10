# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TriggerLogResponse", "Data", "DataMeta"]


class DataMeta(BaseModel):
    id: str

    client_id: str = FieldInfo(alias="clientId")

    connection_id: str = FieldInfo(alias="connectionId")

    created_at: str = FieldInfo(alias="createdAt")

    provider: str

    type: Literal["trigger", "action"]
    """Log entity type (trigger or action)"""

    updated_at: str = FieldInfo(alias="updatedAt")

    trigger_client_error: Optional[str] = FieldInfo(alias="triggerClientError", default=None)

    trigger_client_payload: Optional[str] = FieldInfo(alias="triggerClientPayload", default=None)

    trigger_client_response: Optional[str] = FieldInfo(alias="triggerClientResponse", default=None)

    trigger_name: Optional[str] = FieldInfo(alias="triggerName", default=None)

    trigger_provider_payload: Optional[str] = FieldInfo(alias="triggerProviderPayload", default=None)


class Data(BaseModel):
    id: str

    app_name: str = FieldInfo(alias="appName")

    client_id: str = FieldInfo(alias="clientId")

    connection_id: str = FieldInfo(alias="connectionId")

    created_at: str = FieldInfo(alias="createdAt")

    entity_id: str = FieldInfo(alias="entityId")

    meta: DataMeta

    status: str

    type: Literal["trigger", "action"]
    """Log entity type (trigger or action)"""


class TriggerLogResponse(BaseModel):
    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    data: Optional[List[Data]] = None
