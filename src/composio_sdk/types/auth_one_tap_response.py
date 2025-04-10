# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthOneTapResponse"]


class AuthOneTapResponse(BaseModel):
    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)

    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)

    email: Optional[str] = None

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)
