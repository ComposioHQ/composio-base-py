# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PaymentManageSubscriptionResponse"]


class PaymentManageSubscriptionResponse(BaseModel):
    session_id: str = FieldInfo(alias="sessionId")
    """ID of the created billing portal session"""

    url: str
    """URL to the Stripe billing portal"""
