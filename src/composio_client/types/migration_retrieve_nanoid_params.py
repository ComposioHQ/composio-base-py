# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MigrationRetrieveNanoidParams"]


class MigrationRetrieveNanoidParams(TypedDict, total=False):
    type: Required[Literal["CONNECTED_ACCOUNT", "AUTH_CONFIG", "TRIGGER_INSTANCE"]]
    """The type of resource that the UUID belongs to"""

    uuid: Required[str]
    """The legacy UUID that needs to be converted to a NanoId"""
