# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MigrationRetrieveNanoidResponse"]


class MigrationRetrieveNanoidResponse(BaseModel):
    nanoid: str
    """The NanoId corresponding to the provided UUID."""
