# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AuthConfigCreateResponse", "AuthConfig", "Toolkit"]


class AuthConfig(BaseModel):
    id: str
    """The auth config id of the toolkit (must be a valid auth config id)"""

    auth_scheme: str
    """The authentication mode of the toolkit"""

    is_composio_managed: bool
    """Whether the auth config is managed by Composio"""

    restrict_to_following_tools: Optional[List[str]] = None
    """The tools that the user can use with the auth config"""


class Toolkit(BaseModel):
    slug: str
    """The unique key of the toolkit"""


class AuthConfigCreateResponse(BaseModel):
    auth_config: AuthConfig

    toolkit: Toolkit
