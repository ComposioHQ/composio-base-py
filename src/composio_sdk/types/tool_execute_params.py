# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["ToolExecuteParams"]


class ToolExecuteParams(TypedDict, total=False):
    allow_tracing: bool

    arguments: Dict[str, Optional[object]]

    connected_account_id: str

    entity_id: str

    text: str

    version: str
