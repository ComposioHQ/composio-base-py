# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CliRetrieveSessionResponse", "Account"]


class Account(BaseModel):
    id: str
    """ID of the linked account"""

    email: str
    """Email of the linked account"""

    name: str
    """Name of the linked account"""


class CliRetrieveSessionResponse(BaseModel):
    id: str
    """Unique identifier for the CLI session"""

    account: Optional[Account] = None
    """Information about the linked account, if any"""

    code: str
    """Temporary code used for CLI login"""

    expires_at: str = FieldInfo(alias="expiresAt")
    """Expiration time of the session"""

    status: Literal["pending", "linked"]
    """Current status of the session"""
