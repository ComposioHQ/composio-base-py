# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["APIKeyRetrieveResponse"]


class APIKeyRetrieveResponse(BaseModel):
    org_api_key: str
    """The API key for the organization that can be used for authentication.

    Format: org_xxx
    """
