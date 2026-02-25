# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.logs import tool_list_params, tool_retrieve_params
from ..._base_client import make_request_options
from ...types.logs.tool_list_response import ToolListResponse
from ...types.logs.tool_retrieve_response import ToolRetrieveResponse

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
        *,
        cursor: Optional[float],
        case_sensitive: Optional[bool] | Omit = omit,
        from_: float | Omit = omit,
        limit: float | Omit = omit,
        search_params: Iterable[tool_retrieve_params.SearchParam] | Omit = omit,
        to: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRetrieveResponse:
        """
        Search and retrieve action execution logs

        Args:
          cursor: cursor_that_can_be_used_to_paginate_through_the_logs

          case_sensitive: whether_the_search_is_case_sensitive_or_not

          from_: start_time_of_the_logs_in_epoch_time

          limit: number_of_logs_to_return

          to: end_time_of_the_logs_in_epoch_time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/internal/action_execution/logs",
            body=maybe_transform(
                {
                    "cursor": cursor,
                    "case_sensitive": case_sensitive,
                    "from_": from_,
                    "limit": limit,
                    "search_params": search_params,
                    "to": to,
                },
                tool_retrieve_params.ToolRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: Optional[float],
        case_sensitive: Optional[bool] | Omit = omit,
        from_: float | Omit = omit,
        limit: float | Omit = omit,
        search_params: Iterable[tool_list_params.SearchParam] | Omit = omit,
        to: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListResponse:
        """
        Search and retrieve action execution logs

        Args:
          cursor: cursor_that_can_be_used_to_paginate_through_the_logs

          case_sensitive: whether_the_search_is_case_sensitive_or_not

          from_: start_time_of_the_logs_in_epoch_time

          limit: number_of_logs_to_return

          to: end_time_of_the_logs_in_epoch_time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/internal/action_execution/logs",
            body=maybe_transform(
                {
                    "cursor": cursor,
                    "case_sensitive": case_sensitive,
                    "from_": from_,
                    "limit": limit,
                    "search_params": search_params,
                    "to": to,
                },
                tool_list_params.ToolListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolListResponse,
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
        *,
        cursor: Optional[float],
        case_sensitive: Optional[bool] | Omit = omit,
        from_: float | Omit = omit,
        limit: float | Omit = omit,
        search_params: Iterable[tool_retrieve_params.SearchParam] | Omit = omit,
        to: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRetrieveResponse:
        """
        Search and retrieve action execution logs

        Args:
          cursor: cursor_that_can_be_used_to_paginate_through_the_logs

          case_sensitive: whether_the_search_is_case_sensitive_or_not

          from_: start_time_of_the_logs_in_epoch_time

          limit: number_of_logs_to_return

          to: end_time_of_the_logs_in_epoch_time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/internal/action_execution/logs",
            body=await async_maybe_transform(
                {
                    "cursor": cursor,
                    "case_sensitive": case_sensitive,
                    "from_": from_,
                    "limit": limit,
                    "search_params": search_params,
                    "to": to,
                },
                tool_retrieve_params.ToolRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRetrieveResponse,
        )

    async def list(
        self,
        *,
        cursor: Optional[float],
        case_sensitive: Optional[bool] | Omit = omit,
        from_: float | Omit = omit,
        limit: float | Omit = omit,
        search_params: Iterable[tool_list_params.SearchParam] | Omit = omit,
        to: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListResponse:
        """
        Search and retrieve action execution logs

        Args:
          cursor: cursor_that_can_be_used_to_paginate_through_the_logs

          case_sensitive: whether_the_search_is_case_sensitive_or_not

          from_: start_time_of_the_logs_in_epoch_time

          limit: number_of_logs_to_return

          to: end_time_of_the_logs_in_epoch_time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/internal/action_execution/logs",
            body=await async_maybe_transform(
                {
                    "cursor": cursor,
                    "case_sensitive": case_sensitive,
                    "from_": from_,
                    "limit": limit,
                    "search_params": search_params,
                    "to": to,
                },
                tool_list_params.ToolListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolListResponse,
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


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.retrieve = async_to_raw_response_wrapper(
            tools.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tools.list,
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


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.retrieve = async_to_streamed_response_wrapper(
            tools.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
