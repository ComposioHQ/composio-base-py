# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TeamMemberUpdateParams"]


class TeamMemberUpdateParams(TypedDict, total=False):
    email: str

    name: str

    role: Literal["ADMIN", "DEVELOPER"]
