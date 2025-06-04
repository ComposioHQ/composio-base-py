# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["AdminListConnectionsResponse", "Item"]


class Item(BaseModel):
    id: str
    """
    Identifier that can be used with other API endpoints that operate on connections
    """


class AdminListConnectionsResponse(BaseModel):
    items: List[Item]
    """Collection of account connection objects, may be empty if no connections exist"""
