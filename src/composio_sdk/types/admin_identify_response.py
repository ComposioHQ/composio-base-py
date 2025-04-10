# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AdminIdentifyResponse"]


class AdminIdentifyResponse(BaseModel):
    api_key: str = FieldInfo(alias="apiKey")

    client_id: str = FieldInfo(alias="clientId")

    email: str

    org_id: str = FieldInfo(alias="orgId")
