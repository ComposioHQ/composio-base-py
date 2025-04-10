# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.tools import execute_input_params, execute_proxy_params, execute_execute_params
from ..._base_client import make_request_options
from ...types.tools.execute_input_response import ExecuteInputResponse
from ...types.tools.execute_proxy_response import ExecuteProxyResponse
from ...types.tools.execute_execute_response import ExecuteExecuteResponse

__all__ = ["ExecuteResource", "AsyncExecuteResource"]


class ExecuteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExecuteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/composiohq/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return ExecuteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecuteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/composiohq/composio-base-py#with_streaming_response
        """
        return ExecuteResourceWithStreamingResponse(self)

    def execute(
        self,
        action: str,
        *,
        allow_tracing: bool | NotGiven = NOT_GIVEN,
        arguments: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecuteExecuteResponse:
        """
        Args:
          action: The name of the action

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return self._post(
            f"/api/v3/tools/execute/{action}",
            body=maybe_transform(
                {
                    "allow_tracing": allow_tracing,
                    "arguments": arguments,
                    "connected_account_id": connected_account_id,
                    "entity_id": entity_id,
                    "text": text,
                    "version": version,
                },
                execute_execute_params.ExecuteExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecuteExecuteResponse,
        )

    def input(
        self,
        action_name: str,
        *,
        text: str,
        custom_description: str | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecuteInputResponse:
        """
        Args:
          text: The use-case description for the action, this will give context to LLM to
              generate the correct inputs for the action.

          custom_description: The custom description for the action, use this to provide customised context
              about the action to the LLM to suit your use-case.

          system_prompt: The system prompt to be used by LLM, use this to control and guide the behaviour
              of the LLM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_name:
            raise ValueError(f"Expected a non-empty value for `action_name` but received {action_name!r}")
        return self._post(
            f"/api/v3/tools/execute/{action_name}/input",
            body=maybe_transform(
                {
                    "text": text,
                    "custom_description": custom_description,
                    "system_prompt": system_prompt,
                    "version": version,
                },
                execute_input_params.ExecuteInputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecuteInputResponse,
        )

    def proxy(
        self,
        *,
        endpoint: str,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"],
        body: object | NotGiven = NOT_GIVEN,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        parameters: Iterable[execute_proxy_params.Parameter] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecuteProxyResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/tools/execute/proxy",
            body=maybe_transform(
                {
                    "endpoint": endpoint,
                    "method": method,
                    "body": body,
                    "connected_account_id": connected_account_id,
                    "parameters": parameters,
                },
                execute_proxy_params.ExecuteProxyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecuteProxyResponse,
        )


class AsyncExecuteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExecuteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/composiohq/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncExecuteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecuteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/composiohq/composio-base-py#with_streaming_response
        """
        return AsyncExecuteResourceWithStreamingResponse(self)

    async def execute(
        self,
        action: str,
        *,
        allow_tracing: bool | NotGiven = NOT_GIVEN,
        arguments: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecuteExecuteResponse:
        """
        Args:
          action: The name of the action

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return await self._post(
            f"/api/v3/tools/execute/{action}",
            body=await async_maybe_transform(
                {
                    "allow_tracing": allow_tracing,
                    "arguments": arguments,
                    "connected_account_id": connected_account_id,
                    "entity_id": entity_id,
                    "text": text,
                    "version": version,
                },
                execute_execute_params.ExecuteExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecuteExecuteResponse,
        )

    async def input(
        self,
        action_name: str,
        *,
        text: str,
        custom_description: str | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecuteInputResponse:
        """
        Args:
          text: The use-case description for the action, this will give context to LLM to
              generate the correct inputs for the action.

          custom_description: The custom description for the action, use this to provide customised context
              about the action to the LLM to suit your use-case.

          system_prompt: The system prompt to be used by LLM, use this to control and guide the behaviour
              of the LLM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_name:
            raise ValueError(f"Expected a non-empty value for `action_name` but received {action_name!r}")
        return await self._post(
            f"/api/v3/tools/execute/{action_name}/input",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "custom_description": custom_description,
                    "system_prompt": system_prompt,
                    "version": version,
                },
                execute_input_params.ExecuteInputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecuteInputResponse,
        )

    async def proxy(
        self,
        *,
        endpoint: str,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"],
        body: object | NotGiven = NOT_GIVEN,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        parameters: Iterable[execute_proxy_params.Parameter] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecuteProxyResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/tools/execute/proxy",
            body=await async_maybe_transform(
                {
                    "endpoint": endpoint,
                    "method": method,
                    "body": body,
                    "connected_account_id": connected_account_id,
                    "parameters": parameters,
                },
                execute_proxy_params.ExecuteProxyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecuteProxyResponse,
        )


class ExecuteResourceWithRawResponse:
    def __init__(self, execute: ExecuteResource) -> None:
        self._execute = execute

        self.execute = to_raw_response_wrapper(
            execute.execute,
        )
        self.input = to_raw_response_wrapper(
            execute.input,
        )
        self.proxy = to_raw_response_wrapper(
            execute.proxy,
        )


class AsyncExecuteResourceWithRawResponse:
    def __init__(self, execute: AsyncExecuteResource) -> None:
        self._execute = execute

        self.execute = async_to_raw_response_wrapper(
            execute.execute,
        )
        self.input = async_to_raw_response_wrapper(
            execute.input,
        )
        self.proxy = async_to_raw_response_wrapper(
            execute.proxy,
        )


class ExecuteResourceWithStreamingResponse:
    def __init__(self, execute: ExecuteResource) -> None:
        self._execute = execute

        self.execute = to_streamed_response_wrapper(
            execute.execute,
        )
        self.input = to_streamed_response_wrapper(
            execute.input,
        )
        self.proxy = to_streamed_response_wrapper(
            execute.proxy,
        )


class AsyncExecuteResourceWithStreamingResponse:
    def __init__(self, execute: AsyncExecuteResource) -> None:
        self._execute = execute

        self.execute = async_to_streamed_response_wrapper(
            execute.execute,
        )
        self.input = async_to_streamed_response_wrapper(
            execute.input,
        )
        self.proxy = async_to_streamed_response_wrapper(
            execute.proxy,
        )
