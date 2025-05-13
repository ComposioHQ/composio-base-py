# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["HandleResource", "AsyncHandleResource"]


class HandleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HandleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return HandleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HandleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return HandleResourceWithStreamingResponse(self)

    def retrieve(
        self,
        project_id: Union[str, Literal["default"]],
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Args:
          slug: The slug of the trigger instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            f"/api/v3/trigger_instances/{slug}/{project_id}/handle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def execute(
        self,
        project_id: Union[str, Literal["default"]],
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Args:
          slug: The slug of the trigger instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            f"/api/v3/trigger_instances/{slug}/{project_id}/handle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncHandleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHandleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncHandleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHandleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncHandleResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        project_id: Union[str, Literal["default"]],
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Args:
          slug: The slug of the trigger instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            f"/api/v3/trigger_instances/{slug}/{project_id}/handle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def execute(
        self,
        project_id: Union[str, Literal["default"]],
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Args:
          slug: The slug of the trigger instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            f"/api/v3/trigger_instances/{slug}/{project_id}/handle",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class HandleResourceWithRawResponse:
    def __init__(self, handle: HandleResource) -> None:
        self._handle = handle

        self.retrieve = to_raw_response_wrapper(
            handle.retrieve,
        )
        self.execute = to_raw_response_wrapper(
            handle.execute,
        )


class AsyncHandleResourceWithRawResponse:
    def __init__(self, handle: AsyncHandleResource) -> None:
        self._handle = handle

        self.retrieve = async_to_raw_response_wrapper(
            handle.retrieve,
        )
        self.execute = async_to_raw_response_wrapper(
            handle.execute,
        )


class HandleResourceWithStreamingResponse:
    def __init__(self, handle: HandleResource) -> None:
        self._handle = handle

        self.retrieve = to_streamed_response_wrapper(
            handle.retrieve,
        )
        self.execute = to_streamed_response_wrapper(
            handle.execute,
        )


class AsyncHandleResourceWithStreamingResponse:
    def __init__(self, handle: AsyncHandleResource) -> None:
        self._handle = handle

        self.retrieve = async_to_streamed_response_wrapper(
            handle.retrieve,
        )
        self.execute = async_to_streamed_response_wrapper(
            handle.execute,
        )
