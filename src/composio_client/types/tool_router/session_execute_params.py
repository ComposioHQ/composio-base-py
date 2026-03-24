# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionExecuteParams"]


class SessionExecuteParams(TypedDict, total=False):
    tool_slug: Required[str]
    """The unique slug identifier of the tool to execute"""

    account: str
    """Account identifier to specify which connected account to use.

    Use the account ID (e.g. "coup_hurricane_dal_analytical") or an alias. When
    omitted with a single account, the default is used. When omitted with multiple
    accounts, an error lists available accounts.
    """

    arguments: Dict[str, Optional[object]]
    """The arguments required by the tool"""
