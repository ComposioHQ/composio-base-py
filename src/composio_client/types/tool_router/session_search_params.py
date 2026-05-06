# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = [
    "SessionSearchParams",
    "Query",
    "Experimental",
    "ExperimentalCustomToolkit",
    "ExperimentalCustomToolkitTool",
    "ExperimentalCustomTool",
]


class SessionSearchParams(TypedDict, total=False):
    queries: Required[Iterable[Query]]
    """List of search queries to execute in parallel."""

    experimental: Experimental
    """Inline custom tools and toolkits for this request.

    v3.1 sessions do not persist customs — pass them on every request that needs
    them.
    """

    model: str
    """Optional model hint for search/planning behavior (e.g., "gpt-4o")."""


class Query(TypedDict, total=False):
    use_case: Required[str]
    """The task or use case to search tools for.

    Provide a detailed description to get the best results. Max 1024 characters.
    """

    known_fields: str
    """
    Known field hints as key:value pairs (e.g., "channel_name:general,
    user_email:john@example.com"). Max 500 characters.
    """


class ExperimentalCustomToolkitTool(TypedDict, total=False):
    description: Required[str]
    """Used for BM25 search matching and shown to the LLM."""

    input_schema: Required[Dict[str, Optional[object]]]
    """Must have type: "object" and a properties field."""

    name: Required[str]
    """Human-readable display name"""

    slug: Required[str]
    """Tool slug.

    Combined with toolkit slug to form LOCAL*<TOOLKIT>*<TOOL> (max 60 chars total).
    """

    output_schema: Dict[str, Optional[object]]
    """Optional output schema for the tool response."""

    preload: bool
    """SDK hint for direct custom-tool exposure.

    Not stored in session config; echoed in create/attach responses for inline
    custom definitions.
    """


class ExperimentalCustomToolkit(TypedDict, total=False):
    description: Required[str]
    """Used for BM25 search matching and shown in toolkit connection statuses."""

    name: Required[str]
    """Display name shown to the LLM and in search results."""

    slug: Required[str]
    """Unique slug for the toolkit.

    Must not conflict with existing Composio toolkit slugs. Alphanumeric,
    underscores, and hyphens only.
    """

    tools: Required[Iterable[ExperimentalCustomToolkitTool]]
    """Tools in this custom toolkit"""

    preload: bool
    """SDK hint for direct custom-tool exposure.

    Not stored in session config; echoed in create/attach responses for inline
    custom definitions.
    """


class ExperimentalCustomTool(TypedDict, total=False):
    description: Required[str]
    """Used for BM25 search matching and shown to the LLM."""

    input_schema: Required[Dict[str, Optional[object]]]
    """Must have type: "object" and a properties field."""

    name: Required[str]
    """Human-readable display name"""

    slug: Required[str]
    """Tool slug.

    Forms LOCAL*<TOOL> (standalone) or LOCAL*<TOOLKIT>\\__<TOOL> (extending). Max 60
    chars total.
    """

    extends_toolkit: str
    """If set, must be a valid Composio toolkit slug.

    The tool inherits that toolkit's auth/connection status. If omitted, the tool is
    standalone (no-auth).
    """

    output_schema: Dict[str, Optional[object]]
    """JSON Schema describing tool output (optional)"""

    preload: bool
    """SDK hint for direct custom-tool exposure.

    Not stored in session config; echoed in create/attach responses for inline
    custom definitions.
    """


class Experimental(TypedDict, total=False):
    """Inline custom tools and toolkits for this request.

    v3.1 sessions do not persist customs — pass them on every request that needs them.
    """

    custom_toolkits: Iterable[ExperimentalCustomToolkit]
    """Custom toolkits with grouped tools.

    Toolkit slugs must not conflict with existing Composio toolkits. All tools are
    no-auth.
    """

    custom_tools: Iterable[ExperimentalCustomTool]
    """Custom tools to include in search.

    Standalone tools need no auth. Tools with extends_toolkit inherit the Composio
    toolkit's connection.
    """
