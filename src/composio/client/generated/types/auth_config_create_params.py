# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthConfigCreateParams", "Toolkit", "AuthConfig", "AuthConfigUnionMember0", "AuthConfigUnionMember1"]


class AuthConfigCreateParams(TypedDict, total=False):
    toolkit: Required[Toolkit]

    auth_config: AuthConfig


class Toolkit(TypedDict, total=False):
    slug: Required[str]
    """List of app unique keys to filter by"""


class AuthConfigUnionMember0(TypedDict, total=False):
    type: Required[Literal["use_composio_managed_auth"]]

    credentials: Dict[str, Union[str, bool, float]]

    name: str
    """The name of the integration"""

    restrict_to_following_tools: List[str]
    """The actions that the user can perform on the auth config"""


class AuthConfigUnionMember1(TypedDict, total=False):
    auth_scheme: Required[
        Annotated[
            Literal[
                "OAUTH2",
                "OAUTH1",
                "OAUTH1A",
                "API_KEY",
                "BASIC",
                "BILLCOM_AUTH",
                "BEARER_TOKEN",
                "GOOGLE_SERVICE_ACCOUNT",
                "NO_AUTH",
                "BASIC_WITH_JWT",
                "COMPOSIO_LINK",
                "CALCOM_AUTH",
                "SNOWFLAKE",
            ],
            PropertyInfo(alias="authScheme"),
        ]
    ]

    credentials: Required[Dict[str, Union[str, bool, float]]]

    type: Required[Literal["use_custom_auth"]]

    name: str
    """The name of the integration"""

    restrict_to_following_tools: List[str]
    """The actions that the user can perform on the auth config"""


AuthConfig: TypeAlias = Union[AuthConfigUnionMember0, AuthConfigUnionMember1]
