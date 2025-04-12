# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ActionExecutionRetrieveLogResponse",
    "App",
    "Connection",
    "Step",
    "StepLog",
    "StepLogRequest",
    "StepLogResponse",
    "StepMetadata",
]


class App(BaseModel):
    icon: str

    name: str

    unique_id: str = FieldInfo(alias="uniqueId")


class Connection(BaseModel):
    entity: str

    id: Optional[str] = None


class StepLogRequest(BaseModel):
    method: str

    url: str

    headers: Optional[Dict[str, str]] = None

    json_: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="json", default=None)

    params: Optional[Dict[str, Optional[object]]] = None

    timeout: Optional[float] = None


class StepLogResponse(BaseModel):
    status: float

    time: str


class StepLog(BaseModel):
    level: str

    message: str

    request: StepLogRequest

    request_id: str = FieldInfo(alias="requestId")

    response: StepLogResponse

    time: float

    type: Literal["network", "system"]


class StepMetadata(BaseModel):
    encryption: Optional[str] = None


class Step(BaseModel):
    end_time: float = FieldInfo(alias="endTime")

    message: str

    start_time: float = FieldInfo(alias="startTime")

    status: Literal["success", "failure", "error"]

    total_duration: float = FieldInfo(alias="totalDuration")

    type: Literal["tool_execution", "fetch_connection_details"]

    logs: Optional[List[StepLog]] = None

    metadata: Optional[StepMetadata] = None


class ActionExecutionRetrieveLogResponse(BaseModel):
    action_id: str = FieldInfo(alias="actionId")

    action_log_id: str = FieldInfo(alias="actionLogId")

    app: App

    connection: Connection

    end_time: float = FieldInfo(alias="endTime")

    error: Dict[str, Optional[object]]

    execution_metadata: Dict[str, Optional[object]] = FieldInfo(alias="executionMetadata")

    payload_received: Dict[str, Optional[object]] = FieldInfo(alias="payloadReceived")

    response: Dict[str, Optional[object]]

    session: Dict[str, Optional[object]]

    start_time: float = FieldInfo(alias="startTime")

    status: Literal["success", "error", "warning", "info"]

    steps: List[Step]

    total_duration: str = FieldInfo(alias="totalDuration")

    version: str
