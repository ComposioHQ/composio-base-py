# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ConnectedAccountDeleteParams"]


class ConnectedAccountDeleteParams(TypedDict, total=False):
    revoke_on_delete: Optional[bool]
    """
    When `true`, the delete also starts a background job that revokes the upstream
    credentials of every connected account in scope, and the response carries a
    `revoke_job_id`. Defaults to `false`. Revocation is irreversible — recovering a
    deleted entity does not restore working credentials.
    """
