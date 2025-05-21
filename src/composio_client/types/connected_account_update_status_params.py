# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectedAccountUpdateStatusParams"]


class ConnectedAccountUpdateStatusParams(TypedDict, total=False):
    enabled: Required[bool]
    """Set to true to enable the account or false to disable it"""
