# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CliCreateSessionResponse"]


class CliCreateSessionResponse(BaseModel):
    id: str
    """Unique identifier for the CLI session"""

    code: str
    """Temporary code to use for CLI login"""

    expires_at: str = FieldInfo(alias="expiresAt")
    """Expiration time of the session"""

    status: Literal["pending", "linked"]
    """Current status of the session"""
