# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AdminListConnectionsParams"]


class AdminListConnectionsParams(TypedDict, total=False):
    x_composio_admin_token: Required[Annotated[str, PropertyInfo(alias="x-composio-admin-token")]]
    """Admin authentication token required for administrative operations"""

    toolkit_slug: str
    """The unique identifier slug of the toolkit to filter connections by"""

    x_client_auto_id: Annotated[str, PropertyInfo(alias="x-client-auto-id")]
    """
    When provided, filters connections to only include those for custom apps
    associated with the specified project auto ID
    """
