# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentCreateSessionParams"]


class PaymentCreateSessionParams(TypedDict, total=False):
    apply_discount: Required[Annotated[bool, PropertyInfo(alias="applyDiscount")]]
    """Whether to apply discount coupon"""

    plan: Required[Literal["HOBBY", "STARTER", "GROWTH"]]
    """Subscription plan to purchase"""
