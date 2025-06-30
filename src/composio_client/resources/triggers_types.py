# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import triggers_type_list_params
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
from ..types.triggers_type_list_response import TriggersTypeListResponse
from ..types.triggers_type_retrieve_response import TriggersTypeRetrieveResponse

__all__ = ["TriggersTypesResource", "AsyncTriggersTypesResource"]


class TriggersTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TriggersTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return TriggersTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TriggersTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return TriggersTypesResourceWithStreamingResponse(self)

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
    ) -> TriggersTypeRetrieveResponse:
        """
        Retrieve detailed information about a specific trigger type using its slug
        identifier

        Args:
          slug: The unique slug identifier for the trigger type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            f"/api/v3/triggers_types/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggersTypeRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        toolkit_slugs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggersTypeListResponse:
        """
        Retrieve a list of available trigger types with optional filtering by toolkit.
        Results are paginated and can be filtered by toolkit.

        Args:
          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          limit: Number of items per page

          toolkit_slugs: Array of toolkit slugs to filter triggers by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/triggers_types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "toolkit_slugs": toolkit_slugs,
                    },
                    triggers_type_list_params.TriggersTypeListParams,
                ),
            ),
            cast_to=TriggersTypeListResponse,
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
        Retrieves a list of all available trigger type enum values that can be used
        across the API
        """
        return self._get(
            "/api/v3/triggers_types/list/enum",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncTriggersTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTriggersTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncTriggersTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTriggersTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncTriggersTypesResourceWithStreamingResponse(self)

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
    ) -> TriggersTypeRetrieveResponse:
        """
        Retrieve detailed information about a specific trigger type using its slug
        identifier

        Args:
          slug: The unique slug identifier for the trigger type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            f"/api/v3/triggers_types/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggersTypeRetrieveResponse,
        )

    async def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        toolkit_slugs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggersTypeListResponse:
        """
        Retrieve a list of available trigger types with optional filtering by toolkit.
        Results are paginated and can be filtered by toolkit.

        Args:
          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          limit: Number of items per page

          toolkit_slugs: Array of toolkit slugs to filter triggers by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/triggers_types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "toolkit_slugs": toolkit_slugs,
                    },
                    triggers_type_list_params.TriggersTypeListParams,
                ),
            ),
            cast_to=TriggersTypeListResponse,
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
        Retrieves a list of all available trigger type enum values that can be used
        across the API
        """
        return await self._get(
            "/api/v3/triggers_types/list/enum",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class TriggersTypesResourceWithRawResponse:
    def __init__(self, triggers_types: TriggersTypesResource) -> None:
        self._triggers_types = triggers_types

        self.retrieve = to_raw_response_wrapper(
            triggers_types.retrieve,
        )
        self.list = to_raw_response_wrapper(
            triggers_types.list,
        )
        self.retrieve_enum = to_raw_response_wrapper(
            triggers_types.retrieve_enum,
        )


class AsyncTriggersTypesResourceWithRawResponse:
    def __init__(self, triggers_types: AsyncTriggersTypesResource) -> None:
        self._triggers_types = triggers_types

        self.retrieve = async_to_raw_response_wrapper(
            triggers_types.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            triggers_types.list,
        )
        self.retrieve_enum = async_to_raw_response_wrapper(
            triggers_types.retrieve_enum,
        )


class TriggersTypesResourceWithStreamingResponse:
    def __init__(self, triggers_types: TriggersTypesResource) -> None:
        self._triggers_types = triggers_types

        self.retrieve = to_streamed_response_wrapper(
            triggers_types.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            triggers_types.list,
        )
        self.retrieve_enum = to_streamed_response_wrapper(
            triggers_types.retrieve_enum,
        )


class AsyncTriggersTypesResourceWithStreamingResponse:
    def __init__(self, triggers_types: AsyncTriggersTypesResource) -> None:
        self._triggers_types = triggers_types

        self.retrieve = async_to_streamed_response_wrapper(
            triggers_types.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            triggers_types.list,
        )
        self.retrieve_enum = async_to_streamed_response_wrapper(
            triggers_types.retrieve_enum,
        )
