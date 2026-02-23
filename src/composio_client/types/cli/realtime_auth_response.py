# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RealtimeAuthResponse"]


class RealtimeAuthResponse(BaseModel):
    auth: str
    """The authentication string for Pusher"""

    channel_data: Optional[str] = None
    """Channel data for presence channels"""
