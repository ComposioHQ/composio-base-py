# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConnectedAccountRefreshParams"]


class ConnectedAccountRefreshParams(TypedDict, total=False):
    query_redirect_url: Annotated[str, PropertyInfo(alias="redirect_url")]

    body_redirect_url: Annotated[str, PropertyInfo(alias="redirect_url")]
