# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SessionSearchResponse",
    "Result",
    "ResultReferenceWorkbenchSnippet",
    "Session",
    "TimeInfo",
    "ToolSchemas",
    "ToolSchemasSchemaRef",
    "ToolSchemasSchemaRefArgs",
    "ToolkitConnectionStatus",
]


class ResultReferenceWorkbenchSnippet(BaseModel):
    code: str
    """Python code snippet for the workbench"""

    description: str
    """Description of what the code snippet does"""


class Result(BaseModel):
    index: float
    """1-based index of the query in the request"""

    primary_tool_slugs: List[str]
    """List of main tool slugs matching the search criteria"""

    related_tool_slugs: List[str]
    """List of related tool slugs that might be useful"""

    toolkits: List[str]
    """List of unique toolkit slugs used by tools in this query"""

    use_case: str
    """The use case that was searched"""

    difficulty: Optional[str] = None
    """
    Task difficulty assessment (e.g., "easy - Simple single-tool operation with
    known parameters")
    """

    error: Optional[str] = None
    """Error message if the search for this query failed, null otherwise.

    Always present for failed queries.
    """

    execution_guidance: Optional[str] = None
    """
    Guidance message about the search results, particularly when a cached plan is
    available
    """

    known_pitfalls: Optional[List[str]] = None
    """Common pitfalls and considerations (only present when cached plan is available)"""

    memory: Optional[Dict[str, List[str]]] = None
    """Memory data relevant to this query, grouped by app.

    Only present for non-cached search results.
    """

    plan_id: Optional[str] = None
    """ID of cached plan if available"""

    recommended_plan_steps: Optional[List[str]] = None
    """Workflow steps from cached plan (only present when cached plan is available)"""

    reference_workbench_snippets: Optional[List[ResultReferenceWorkbenchSnippet]] = None
    """
    Reference Python code snippets for processing tool responses in the workbench
    (only present when cached plan is available)
    """


class Session(BaseModel):
    """Session info for correlating meta tool calls"""

    id: str
    """Session identifier to be passed to subsequent meta tool calls as session_id."""

    generate_id: bool
    """Whether a fresh session id was generated in this call."""

    instructions: str
    """LLM-facing guidance on how to reuse this session id"""


class TimeInfo(BaseModel):
    """Time information for the query"""

    current_time_utc: str
    """Current time in ISO format (UTC)"""

    current_time_utc_epoch_seconds: float
    """Current time as Unix epoch timestamp in seconds"""

    message: str
    """Important message about time handling and timezone considerations"""


class ToolSchemasSchemaRefArgs(BaseModel):
    """Arguments to pass to the tool"""

    tool_slugs: List[str]
    """Tool slugs to fetch schemas for"""


class ToolSchemasSchemaRef(BaseModel):
    """Reference to fetch full schema when hasFullSchema is false"""

    args: ToolSchemasSchemaRefArgs
    """Arguments to pass to the tool"""

    message: str
    """Instruction message for the LLM"""

    tool: Literal["COMPOSIO_GET_TOOL_SCHEMAS"]
    """Tool to call"""


class ToolSchemas(BaseModel):
    tool_slug: str
    """The slug of the tool"""

    toolkit: str
    """The slug of the toolkit that provides this tool"""

    description: Optional[str] = None
    """Description of the tool"""

    has_full_schema: Optional[bool] = FieldInfo(alias="hasFullSchema", default=None)
    """Whether the full input_schema is included in this response"""

    input_schema: Optional[Dict[str, Optional[object]]] = None
    """Input schema for the tool (only present when hasFullSchema is true)"""

    output_schema: Optional[Dict[str, Optional[object]]] = None
    """Output/response schema for the tool"""

    schema_ref: Optional[ToolSchemasSchemaRef] = FieldInfo(alias="schemaRef", default=None)
    """Reference to fetch full schema when hasFullSchema is false"""


class ToolkitConnectionStatus(BaseModel):
    description: str
    """Description of what the toolkit does and its capabilities"""

    has_active_connection: bool
    """Whether an active connection exists for this toolkit"""

    status_message: str
    """Human-readable message about the connection status and next steps"""

    toolkit: str
    """The toolkit slug identifier (e.g., "gmail", "slack")"""

    connection_details: Optional[Dict[str, Optional[object]]] = None
    """Connection details including auth config and connected account IDs.

    Only present when has_active_connection is true.
    """

    current_user_info: Optional[Dict[str, Optional[object]]] = None
    """Information about the currently connected user (email, name, etc.)"""


class SessionSearchResponse(BaseModel):
    error: Optional[str] = None
    """Error message if any searches failed, null if all succeeded.

    Format: "X out of Y searches failed, reasons: <details>"
    """

    next_steps_guidance: List[str]
    """Combined workflow guidance covering connections, planner, and memory usage.

    Each element is a step instruction.
    """

    results: List[Result]
    """Per-query search results with tools, reasoning, and memory.

    One entry per query in request order.
    """

    session: Session
    """Session info for correlating meta tool calls"""

    success: bool
    """Whether all searches completed successfully. False if any query failed."""

    time_info: TimeInfo
    """Time information for the query"""

    tool_schemas: Dict[str, ToolSchemas]
    """Deduplicated tool definitions keyed by tool_slug for O(1) lookup.

    Each tool appears once even if used in multiple queries.
    """

    toolkit_connection_statuses: List[ToolkitConnectionStatus]
    """
    Connection status for all toolkits mentioned across all queries, with
    descriptions merged in.
    """
