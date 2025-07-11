# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import toolkit_list_params, toolkit_retrieve_categories_params
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
from ..types.toolkit_list_response import ToolkitListResponse
from ..types.toolkit_retrieve_response import ToolkitRetrieveResponse
from ..types.toolkit_retrieve_categories_response import ToolkitRetrieveCategoriesResponse

__all__ = ["ToolkitsResource", "AsyncToolkitsResource"]


class ToolkitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolkitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return ToolkitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolkitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return ToolkitsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolkitRetrieveResponse:
        """
        Retrieves comprehensive information about a specific toolkit using its unique
        slug identifier. This endpoint provides detailed metadata, authentication
        configuration options, and feature counts for the requested toolkit.

        Args:
          slug: The unique slug identifier of the toolkit to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            f"/api/v3/toolkits/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolkitRetrieveResponse,
        )

    def list(
        self,
        *,
        category: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        is_local: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        managed_by: Literal["composio", "all", "project"] | NotGiven = NOT_GIVEN,
        sort_by: Literal["usage", "alphabetically"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolkitListResponse:
        """
        Retrieves a comprehensive list of toolkits that are available to the
        authenticated project. Toolkits represent integration points with external
        services and applications, each containing a collection of tools and triggers.
        This endpoint supports filtering by category, management type, and local
        availability, as well as different sorting options.

        Args:
          category: Filter toolkits by category

          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          is_local: Whether to include local toolkits in the results

          limit: Number of items per page

          managed_by: Filter toolkits by who manages them

          sort_by: Sort order for returned toolkits

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/toolkits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "cursor": cursor,
                        "is_local": is_local,
                        "limit": limit,
                        "managed_by": managed_by,
                        "sort_by": sort_by,
                    },
                    toolkit_list_params.ToolkitListParams,
                ),
            ),
            cast_to=ToolkitListResponse,
        )

    def retrieve_categories(
        self,
        *,
        cache: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolkitRetrieveCategoriesResponse:
        """Retrieves a comprehensive list of all available toolkit categories.

        These
        categories can be used to filter toolkits by type or purpose when using the
        toolkit listing endpoint. Categories help organize toolkits into logical groups
        based on their functionality or industry focus.

        Args:
          cache: Cache control parameter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/toolkits/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cache": cache}, toolkit_retrieve_categories_params.ToolkitRetrieveCategoriesParams
                ),
            ),
            cast_to=ToolkitRetrieveCategoriesResponse,
        )


class AsyncToolkitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolkitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncToolkitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolkitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncToolkitsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolkitRetrieveResponse:
        """
        Retrieves comprehensive information about a specific toolkit using its unique
        slug identifier. This endpoint provides detailed metadata, authentication
        configuration options, and feature counts for the requested toolkit.

        Args:
          slug: The unique slug identifier of the toolkit to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            f"/api/v3/toolkits/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolkitRetrieveResponse,
        )

    async def list(
        self,
        *,
        category: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        is_local: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        managed_by: Literal["composio", "all", "project"] | NotGiven = NOT_GIVEN,
        sort_by: Literal["usage", "alphabetically"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolkitListResponse:
        """
        Retrieves a comprehensive list of toolkits that are available to the
        authenticated project. Toolkits represent integration points with external
        services and applications, each containing a collection of tools and triggers.
        This endpoint supports filtering by category, management type, and local
        availability, as well as different sorting options.

        Args:
          category: Filter toolkits by category

          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          is_local: Whether to include local toolkits in the results

          limit: Number of items per page

          managed_by: Filter toolkits by who manages them

          sort_by: Sort order for returned toolkits

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/toolkits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "cursor": cursor,
                        "is_local": is_local,
                        "limit": limit,
                        "managed_by": managed_by,
                        "sort_by": sort_by,
                    },
                    toolkit_list_params.ToolkitListParams,
                ),
            ),
            cast_to=ToolkitListResponse,
        )

    async def retrieve_categories(
        self,
        *,
        cache: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolkitRetrieveCategoriesResponse:
        """Retrieves a comprehensive list of all available toolkit categories.

        These
        categories can be used to filter toolkits by type or purpose when using the
        toolkit listing endpoint. Categories help organize toolkits into logical groups
        based on their functionality or industry focus.

        Args:
          cache: Cache control parameter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/toolkits/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cache": cache}, toolkit_retrieve_categories_params.ToolkitRetrieveCategoriesParams
                ),
            ),
            cast_to=ToolkitRetrieveCategoriesResponse,
        )


class ToolkitsResourceWithRawResponse:
    def __init__(self, toolkits: ToolkitsResource) -> None:
        self._toolkits = toolkits

        self.retrieve = to_raw_response_wrapper(
            toolkits.retrieve,
        )
        self.list = to_raw_response_wrapper(
            toolkits.list,
        )
        self.retrieve_categories = to_raw_response_wrapper(
            toolkits.retrieve_categories,
        )


class AsyncToolkitsResourceWithRawResponse:
    def __init__(self, toolkits: AsyncToolkitsResource) -> None:
        self._toolkits = toolkits

        self.retrieve = async_to_raw_response_wrapper(
            toolkits.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            toolkits.list,
        )
        self.retrieve_categories = async_to_raw_response_wrapper(
            toolkits.retrieve_categories,
        )


class ToolkitsResourceWithStreamingResponse:
    def __init__(self, toolkits: ToolkitsResource) -> None:
        self._toolkits = toolkits

        self.retrieve = to_streamed_response_wrapper(
            toolkits.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            toolkits.list,
        )
        self.retrieve_categories = to_streamed_response_wrapper(
            toolkits.retrieve_categories,
        )


class AsyncToolkitsResourceWithStreamingResponse:
    def __init__(self, toolkits: AsyncToolkitsResource) -> None:
        self._toolkits = toolkits

        self.retrieve = async_to_streamed_response_wrapper(
            toolkits.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            toolkits.list,
        )
        self.retrieve_categories = async_to_streamed_response_wrapper(
            toolkits.retrieve_categories,
        )
