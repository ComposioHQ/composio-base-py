# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TeamMemberUpdateResponse"]


class TeamMemberUpdateResponse(BaseModel):
    id: str

    created_at: str

    email: str

    name: str

    role: str

    updated_at: str
