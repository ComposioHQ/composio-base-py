# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CliGetSessionParams"]


class CliGetSessionParams(TypedDict, total=False):
    id: Required[str]
    """CLI session ID (UUID format) or 6-character code to check.

    Both formats are supported for flexibility in client implementations.
    """
