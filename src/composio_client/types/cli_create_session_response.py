# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CliCreateSessionResponse"]


class CliCreateSessionResponse(BaseModel):
    id: str
    """Unique identifier for the CLI session.

    UUID v4 format used for tracking and retrieval.
    """

    code: str
    """The 6-character hexadecimal code used for CLI login"""

    expires_at: str = FieldInfo(alias="expiresAt")
    """The ISO timestamp when the session expires"""

    status: Literal["pending", "linked"]
    """The current status of the session"""
