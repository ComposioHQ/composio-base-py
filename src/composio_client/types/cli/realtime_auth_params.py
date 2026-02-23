# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RealtimeAuthParams"]


class RealtimeAuthParams(TypedDict, total=False):
    channel_name: Required[str]
    """The channel name to authenticate for"""

    socket_id: Required[str]
    """The socket ID for Pusher authentication"""
