# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import link_submit_input_params
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
from ..types.link_retrieve_response import LinkRetrieveResponse
from ..types.link_submit_input_response import LinkSubmitInputResponse

__all__ = ["LinkResource", "AsyncLinkResource"]


class LinkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return LinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return LinkResourceWithStreamingResponse(self)

    def retrieve(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkRetrieveResponse:
        """
        Retrieves information about an authentication session using the link token

        Args:
          token: The link token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return self._get(
            f"/api/v3/internal/connected_accounts/link/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkRetrieveResponse,
        )

    def submit_input(
        self,
        token: str,
        *,
        input: Dict[str, Optional[object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkSubmitInputResponse:
        """
        Submits authentication input for a link session

        Args:
          token: The link token

          input: The input fields for authentication

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return self._post(
            f"/api/v3/internal/connected_accounts/link/{token}",
            body=maybe_transform({"input": input}, link_submit_input_params.LinkSubmitInputParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkSubmitInputResponse,
        )


class AsyncLinkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncLinkResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkRetrieveResponse:
        """
        Retrieves information about an authentication session using the link token

        Args:
          token: The link token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return await self._get(
            f"/api/v3/internal/connected_accounts/link/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkRetrieveResponse,
        )

    async def submit_input(
        self,
        token: str,
        *,
        input: Dict[str, Optional[object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkSubmitInputResponse:
        """
        Submits authentication input for a link session

        Args:
          token: The link token

          input: The input fields for authentication

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return await self._post(
            f"/api/v3/internal/connected_accounts/link/{token}",
            body=await async_maybe_transform({"input": input}, link_submit_input_params.LinkSubmitInputParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkSubmitInputResponse,
        )


class LinkResourceWithRawResponse:
    def __init__(self, link: LinkResource) -> None:
        self._link = link

        self.retrieve = to_raw_response_wrapper(
            link.retrieve,
        )
        self.submit_input = to_raw_response_wrapper(
            link.submit_input,
        )


class AsyncLinkResourceWithRawResponse:
    def __init__(self, link: AsyncLinkResource) -> None:
        self._link = link

        self.retrieve = async_to_raw_response_wrapper(
            link.retrieve,
        )
        self.submit_input = async_to_raw_response_wrapper(
            link.submit_input,
        )


class LinkResourceWithStreamingResponse:
    def __init__(self, link: LinkResource) -> None:
        self._link = link

        self.retrieve = to_streamed_response_wrapper(
            link.retrieve,
        )
        self.submit_input = to_streamed_response_wrapper(
            link.submit_input,
        )


class AsyncLinkResourceWithStreamingResponse:
    def __init__(self, link: AsyncLinkResource) -> None:
        self._link = link

        self.retrieve = async_to_streamed_response_wrapper(
            link.retrieve,
        )
        self.submit_input = async_to_streamed_response_wrapper(
            link.submit_input,
        )
