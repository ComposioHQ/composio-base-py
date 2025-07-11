# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CliGetSessionResponse", "Account"]


class Account(BaseModel):
    id: str
    """The ID of the linked account"""

    email: str
    """The email address of the linked account"""

    name: str
    """The display name of the linked account"""


class CliGetSessionResponse(BaseModel):
    id: str
    """The unique identifier for the CLI session"""

    account: Optional[Account] = None
    """Information about the linked account, if any.

    Null if the session status is "pending".
    """

    code: str
    """The 6-character hexadecimal code used for CLI login"""

    expires_at: str = FieldInfo(alias="expiresAt")
    """The ISO timestamp when the session expires"""

    status: Literal["pending", "linked"]
    """The current status of the session"""
