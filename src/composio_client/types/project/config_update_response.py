# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConfigUpdateResponse"]


class ConfigUpdateResponse(BaseModel):
    is_2_fa_enabled: bool = FieldInfo(alias="is_2FA_enabled")

    log_visibility_setting: Literal["show_all", "dont_store_data"]

    mask_secret_keys_in_connected_account: bool

    display_name: Optional[str] = None

    logo_url: Optional[str] = None

    require_mcp_api_key: Optional[bool] = None
