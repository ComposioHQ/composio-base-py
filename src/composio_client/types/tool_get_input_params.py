# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolGetInputParams"]


class ToolGetInputParams(TypedDict, total=False):
    text: Required[str]
    """Natural language description of what you want to accomplish with this tool"""

    custom_description: str
    """
    Custom description of the tool to help guide the LLM in generating more accurate
    inputs
    """

    system_prompt: str
    """
    System prompt to control and guide the behavior of the LLM when generating
    inputs
    """

    version: str
    """
    Tool version to use when generating inputs (defaults to "latest" if not
    specified)
    """
