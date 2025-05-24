# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolGetInputParams"]


class ToolGetInputParams(TypedDict, total=False):
    text: Required[str]
    """Natural language description of what you want to accomplish with this tool"""

    custom_description: Annotated[str, PropertyInfo(alias="customDescription")]
    """
    Custom description of the tool to help guide the LLM in generating more accurate
    inputs
    """

    system_prompt: Annotated[str, PropertyInfo(alias="systemPrompt")]
    """
    System prompt to control and guide the behavior of the LLM when generating
    inputs
    """

    version: str
    """
    Tool version to use when generating inputs (defaults to "latest" if not
    specified)
    """
