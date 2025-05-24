# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    type: Required[Literal["trigger", "event"]]
    """Specifies which webhook type to update (trigger or event)"""

    webhook_url: Required[str]
    """Valid URL that will receive webhook payloads. Must include https:// protocol."""
