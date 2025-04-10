# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MagicLinkVerifyResponse", "Data"]


class Data(BaseModel):
    email: str

    jwt_token: str = FieldInfo(alias="jwtToken")

    member_id: str = FieldInfo(alias="memberId")

    org_id: str = FieldInfo(alias="orgId")


class MagicLinkVerifyResponse(BaseModel):
    data: Data

    message: str
