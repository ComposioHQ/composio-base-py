# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import TypedDict

__all__ = ["ToolRetrieveParams"]


class ToolRetrieveParams(TypedDict, total=False):
    toolkit_versions: Union[str, Dict[str, str]]
    """Can be omitted, null, a string, or an object mapping toolkit names to versions"""

    version: str
    """Optional version of the tool to retrieve"""
