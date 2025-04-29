# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import tool_list_params, tool_proxy_params, tool_execute_params, tool_get_input_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.tool_list_response import ToolListResponse
from ..types.tool_proxy_response import ToolProxyResponse
from ..types.tool_execute_response import ToolExecuteResponse
from ..types.tool_retrieve_response import ToolRetrieveResponse
from ..types.tool_get_input_response import ToolGetInputResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        tool_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_slug:
            raise ValueError(f"Expected a non-empty value for `tool_slug` but received {tool_slug!r}")
        return self._get(
            f"/api/v3/tools/{tool_slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        important: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tool_slugs: str | NotGiven = NOT_GIVEN,
        toolkit_slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolListResponse:
        """
        Args:
          cursor: The cursor to paginate through the results

          important: Whether to filter by important tools

          limit: The number of results to return

          search: The search query to filter by

          tags: The tags to filter the tools by

          tool_slugs: The slugs of the tools to filter by

          toolkit_slug: The slug of the toolkit to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/tools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "important": important,
                        "limit": limit,
                        "search": search,
                        "tags": tags,
                        "tool_slugs": tool_slugs,
                        "toolkit_slug": toolkit_slug,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    def execute(
        self,
        action: str,
        *,
        allow_tracing: bool | NotGiven = NOT_GIVEN,
        arguments: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        custom_auth_params: tool_execute_params.CustomAuthParams | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolExecuteResponse:
        """
        Args:
          action: The name of the action

          custom_auth_params: An optional field for people who want to use their own auth to execute the
              action.

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
                    "custom_auth_params": custom_auth_params,
                    "entity_id": entity_id,
                    "text": text,
                    "version": version,
                },
                tool_execute_params.ToolExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolExecuteResponse,
        )

    def get_input(
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
    ) -> ToolGetInputResponse:
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
                tool_get_input_params.ToolGetInputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGetInputResponse,
        )

    def proxy(
        self,
        *,
        endpoint: str,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"],
        body: object | NotGiven = NOT_GIVEN,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        parameters: Iterable[tool_proxy_params.Parameter] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolProxyResponse:
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
                tool_proxy_params.ToolProxyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolProxyResponse,
        )

    def retrieve_enum(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        return self._get(
            "/api/v3/tools/enum",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        tool_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_slug:
            raise ValueError(f"Expected a non-empty value for `tool_slug` but received {tool_slug!r}")
        return await self._get(
            f"/api/v3/tools/{tool_slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRetrieveResponse,
        )

    async def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        important: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tool_slugs: str | NotGiven = NOT_GIVEN,
        toolkit_slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolListResponse:
        """
        Args:
          cursor: The cursor to paginate through the results

          important: Whether to filter by important tools

          limit: The number of results to return

          search: The search query to filter by

          tags: The tags to filter the tools by

          tool_slugs: The slugs of the tools to filter by

          toolkit_slug: The slug of the toolkit to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/tools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "important": important,
                        "limit": limit,
                        "search": search,
                        "tags": tags,
                        "tool_slugs": tool_slugs,
                        "toolkit_slug": toolkit_slug,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    async def execute(
        self,
        action: str,
        *,
        allow_tracing: bool | NotGiven = NOT_GIVEN,
        arguments: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        custom_auth_params: tool_execute_params.CustomAuthParams | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolExecuteResponse:
        """
        Args:
          action: The name of the action

          custom_auth_params: An optional field for people who want to use their own auth to execute the
              action.

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
                    "custom_auth_params": custom_auth_params,
                    "entity_id": entity_id,
                    "text": text,
                    "version": version,
                },
                tool_execute_params.ToolExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolExecuteResponse,
        )

    async def get_input(
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
    ) -> ToolGetInputResponse:
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
                tool_get_input_params.ToolGetInputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGetInputResponse,
        )

    async def proxy(
        self,
        *,
        endpoint: str,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"],
        body: object | NotGiven = NOT_GIVEN,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        parameters: Iterable[tool_proxy_params.Parameter] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolProxyResponse:
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
                tool_proxy_params.ToolProxyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolProxyResponse,
        )

    async def retrieve_enum(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        return await self._get(
            "/api/v3/tools/enum",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.retrieve = to_raw_response_wrapper(
            tools.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tools.list,
        )
        self.execute = to_raw_response_wrapper(
            tools.execute,
        )
        self.get_input = to_raw_response_wrapper(
            tools.get_input,
        )
        self.proxy = to_raw_response_wrapper(
            tools.proxy,
        )
        self.retrieve_enum = to_raw_response_wrapper(
            tools.retrieve_enum,
        )


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.retrieve = async_to_raw_response_wrapper(
            tools.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tools.list,
        )
        self.execute = async_to_raw_response_wrapper(
            tools.execute,
        )
        self.get_input = async_to_raw_response_wrapper(
            tools.get_input,
        )
        self.proxy = async_to_raw_response_wrapper(
            tools.proxy,
        )
        self.retrieve_enum = async_to_raw_response_wrapper(
            tools.retrieve_enum,
        )


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.retrieve = to_streamed_response_wrapper(
            tools.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tools.list,
        )
        self.execute = to_streamed_response_wrapper(
            tools.execute,
        )
        self.get_input = to_streamed_response_wrapper(
            tools.get_input,
        )
        self.proxy = to_streamed_response_wrapper(
            tools.proxy,
        )
        self.retrieve_enum = to_streamed_response_wrapper(
            tools.retrieve_enum,
        )


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.retrieve = async_to_streamed_response_wrapper(
            tools.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
        self.execute = async_to_streamed_response_wrapper(
            tools.execute,
        )
        self.get_input = async_to_streamed_response_wrapper(
            tools.get_input,
        )
        self.proxy = async_to_streamed_response_wrapper(
            tools.proxy,
        )
        self.retrieve_enum = async_to_streamed_response_wrapper(
            tools.retrieve_enum,
        )
