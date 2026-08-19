# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import TypedDict

__all__ = ["ToolRetrieveParams"]


class ToolRetrieveParams(TypedDict, total=False):
    toolkit_versions: Union[str, Dict[str, str]]
    """Toolkit version specification.

    Use "latest" for latest versions or bracket notation for specific versions per
    toolkit. Read only when version is omitted; when neither is supplied the tool
    resolves to the latest published version ("latest").
    """

    version: str
    """Optional version of the tool to retrieve.

    Takes precedence over toolkit_versions; when both are omitted the tool resolves
    to the latest published version ("latest").
    """
