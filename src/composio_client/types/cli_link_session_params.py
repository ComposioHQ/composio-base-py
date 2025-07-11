# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CliLinkSessionParams"]


class CliLinkSessionParams(TypedDict, total=False):
    id: Required[str]
    """The CLI session ID or code to link to the current user"""
