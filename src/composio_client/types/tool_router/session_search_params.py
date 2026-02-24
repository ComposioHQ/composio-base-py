# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SessionSearchParams", "Query"]


class SessionSearchParams(TypedDict, total=False):
    queries: Required[Iterable[Query]]
    """List of search queries to execute in parallel. Up to 7 queries supported."""

    model: str
    """Optional model hint for search/planning behavior (e.g., "gpt-4o").

    Ignored if invalid.
    """


class Query(TypedDict, total=False):
    use_case: Required[str]
    """The task or use case to search tools for.

    Provide a detailed description to get the best results.
    """

    known_fields: str
    """
    Known field hints as key:value pairs (e.g., "channel_name:general,
    user_email:john@example.com")
    """
