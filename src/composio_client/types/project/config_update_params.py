# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConfigUpdateParams"]


class ConfigUpdateParams(TypedDict, total=False):
    display_name: str

    is_2_fa_enabled: Annotated[bool, PropertyInfo(alias="is_2FA_enabled")]

    is_composio_link_enabled_for_managed_auth: bool
    """Whether to enable composio link for managed authentication.

    This key will be deprecated in the future. Please don't use this key.
    """

    log_visibility_setting: Literal["show_all", "dont_store_data"]

    logo_url: str

    mask_secret_keys_in_connected_account: bool

    require_mcp_api_key: bool

    signed_url_file_expiry_in_seconds: float
