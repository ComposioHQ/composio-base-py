# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ActionExecutionLogResponse", "Data", "DataApp"]


class DataApp(BaseModel):
    icon: str

    name: str


class Data(BaseModel):
    id: str

    action_key: str = FieldInfo(alias="actionKey")

    app: DataApp

    app_key: str = FieldInfo(alias="appKey")

    connected_account_id: str = FieldInfo(alias="connectedAccountId")

    created_at: float = FieldInfo(alias="createdAt")

    entity_id: str = FieldInfo(alias="entityId")

    execution_time: float = FieldInfo(alias="executionTime")

    minimal_response: str = FieldInfo(alias="minimalResponse")

    status: Literal["success", "failed"]


class ActionExecutionLogResponse(BaseModel):
    data: List[Data]

    next_cursor: Optional[float] = FieldInfo(alias="nextCursor", default=None)
