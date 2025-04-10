# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PaymentCreateSessionResponse"]


class PaymentCreateSessionResponse(BaseModel):
    session_id: str = FieldInfo(alias="sessionId")
    """ID of the created payment session"""

    url: str
    """URL to the payment page"""
