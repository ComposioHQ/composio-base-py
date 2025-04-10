# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthRetrieveCallbackResponse", "Data", "DataUserData"]


class DataUserData(BaseModel):
    email: str


class Data(BaseModel):
    jwt_token: str = FieldInfo(alias="jwtToken")

    user_data: DataUserData = FieldInfo(alias="userData")


class AuthRetrieveCallbackResponse(BaseModel):
    data: Data

    message: str
