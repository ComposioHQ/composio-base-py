# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import tool_list_params
from .execute import (
    ExecuteResource,
    AsyncExecuteResource,
    ExecuteResourceWithRawResponse,
    AsyncExecuteResourceWithRawResponse,
    ExecuteResourceWithStreamingResponse,
    AsyncExecuteResourceWithStreamingResponse,
)
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
from ..._base_client import make_request_options
from ...types.tool_list_response import ToolListResponse
from ...types.tool_retrieve_response import ToolRetrieveResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def execute(self) -> ExecuteResource:
        return ExecuteResource(self._client)

    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/composiohq/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/composiohq/composio-base-py#with_streaming_response
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
                        "toolkit_slug": toolkit_slug,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
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
    def execute(self) -> AsyncExecuteResource:
        return AsyncExecuteResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/composiohq/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/composiohq/composio-base-py#with_streaming_response
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
                        "toolkit_slug": toolkit_slug,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
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
        self.retrieve_enum = to_raw_response_wrapper(
            tools.retrieve_enum,
        )

    @cached_property
    def execute(self) -> ExecuteResourceWithRawResponse:
        return ExecuteResourceWithRawResponse(self._tools.execute)


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.retrieve = async_to_raw_response_wrapper(
            tools.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tools.list,
        )
        self.retrieve_enum = async_to_raw_response_wrapper(
            tools.retrieve_enum,
        )

    @cached_property
    def execute(self) -> AsyncExecuteResourceWithRawResponse:
        return AsyncExecuteResourceWithRawResponse(self._tools.execute)


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.retrieve = to_streamed_response_wrapper(
            tools.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tools.list,
        )
        self.retrieve_enum = to_streamed_response_wrapper(
            tools.retrieve_enum,
        )

    @cached_property
    def execute(self) -> ExecuteResourceWithStreamingResponse:
        return ExecuteResourceWithStreamingResponse(self._tools.execute)


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.retrieve = async_to_streamed_response_wrapper(
            tools.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
        self.retrieve_enum = async_to_streamed_response_wrapper(
            tools.retrieve_enum,
        )

    @cached_property
    def execute(self) -> AsyncExecuteResourceWithStreamingResponse:
        return AsyncExecuteResourceWithStreamingResponse(self._tools.execute)
