# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolGetInputParams"]


class ToolGetInputParams(TypedDict, total=False):
    text: Required[str]
    """
    The use-case description for the action, this will give context to LLM to
    generate the correct inputs for the action.
    """

    custom_description: Annotated[str, PropertyInfo(alias="customDescription")]
    """
    The custom description for the action, use this to provide customised context
    about the action to the LLM to suit your use-case.
    """

    system_prompt: Annotated[str, PropertyInfo(alias="systemPrompt")]
    """
    The system prompt to be used by LLM, use this to control and guide the behaviour
    of the LLM.
    """

    version: str
