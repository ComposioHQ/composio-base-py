# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ProjectDeleteResponse"]


class ProjectDeleteResponse(BaseModel):
    status: str
    """Status of the delete operation"""
