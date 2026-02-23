# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CliCreateSessionParams"]


class CliCreateSessionParams(TypedDict, total=False):
    scope: Literal["project", "user"]
    """Key scope.

    'project' (default) returns a project-level API key; 'user' returns a user-level
    API key valid across projects.
    """

    source: str
    """Free-form string describing the source, e.g. 'Johns MacBook (darwin, v1.2.3)'"""
