# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import tool_list_params, tool_proxy_params
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
from ..types.tool_retrieve_response import ToolRetrieveResponse

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
        Retrieve detailed information about a specific tool using its slug identifier.
        This endpoint returns full metadata about a tool including input/output
        parameters, versions, and toolkit information.

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
        important: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
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
        Retrieve a paginated list of available tools with comprehensive filtering,
        sorting and search capabilities. Use query parameters to narrow down results by
        toolkit, tags, or search terms.

        Args:
          cursor: Pagination cursor for fetching next page of results (base64 encoded)

          important: Filter to only show important/featured tools (set to "true" to enable)

          limit: Maximum number of tools to return per page (defaults to 20, max 100)

          search: Free-text search query to find tools by name, description, or functionality

          tags: Filter tools by one or more tags (can be specified multiple times)

          tool_slugs: Comma-separated list of specific tool slugs to retrieve (overrides other
              filters)

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
        Proxy an HTTP request to a third-party API using connected account credentials.
        This endpoint allows making authenticated API calls to external services while
        abstracting away authentication details.

        Args:
          endpoint: The API endpoint to call (absolute URL or path relative to base URL of the
              connected account)

          method: The HTTP method to use for the request

          body: The request body (for POST, PUT, and PATCH requests)

          connected_account_id: The ID of the connected account to use for authentication (if not provided, will
              use the default account for the project)

          parameters: Additional HTTP headers or query parameters to include in the request

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
        """
        Retrieve a list of all available tool enumeration values (tool slugs) for the
        project. This endpoint returns a comma-separated string of tool slugs that can
        be used in other API calls.
        """
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
        Retrieve detailed information about a specific tool using its slug identifier.
        This endpoint returns full metadata about a tool including input/output
        parameters, versions, and toolkit information.

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
        important: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
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
        Retrieve a paginated list of available tools with comprehensive filtering,
        sorting and search capabilities. Use query parameters to narrow down results by
        toolkit, tags, or search terms.

        Args:
          cursor: Pagination cursor for fetching next page of results (base64 encoded)

          important: Filter to only show important/featured tools (set to "true" to enable)

          limit: Maximum number of tools to return per page (defaults to 20, max 100)

          search: Free-text search query to find tools by name, description, or functionality

          tags: Filter tools by one or more tags (can be specified multiple times)

          tool_slugs: Comma-separated list of specific tool slugs to retrieve (overrides other
              filters)

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
        Proxy an HTTP request to a third-party API using connected account credentials.
        This endpoint allows making authenticated API calls to external services while
        abstracting away authentication details.

        Args:
          endpoint: The API endpoint to call (absolute URL or path relative to base URL of the
              connected account)

          method: The HTTP method to use for the request

          body: The request body (for POST, PUT, and PATCH requests)

          connected_account_id: The ID of the connected account to use for authentication (if not provided, will
              use the default account for the project)

          parameters: Additional HTTP headers or query parameters to include in the request

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
        """
        Retrieve a list of all available tool enumeration values (tool slugs) for the
        project. This endpoint returns a comma-separated string of tool slugs that can
        be used in other API calls.
        """
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
        self.proxy = async_to_streamed_response_wrapper(
            tools.proxy,
        )
        self.retrieve_enum = async_to_streamed_response_wrapper(
            tools.retrieve_enum,
        )
