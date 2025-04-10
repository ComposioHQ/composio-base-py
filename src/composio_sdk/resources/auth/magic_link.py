# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.auth import magic_link_send_params, magic_link_verify_params
from ..._base_client import make_request_options
from ...types.auth.magic_link_send_response import MagicLinkSendResponse
from ...types.auth.magic_link_verify_response import MagicLinkVerifyResponse

__all__ = ["MagicLinkResource", "AsyncMagicLinkResource"]


class MagicLinkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MagicLinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/composiohq/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return MagicLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MagicLinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/composiohq/composio-base-py#with_streaming_response
        """
        return MagicLinkResourceWithStreamingResponse(self)

    def send(
        self,
        *,
        email: str,
        verify_host: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MagicLinkSendResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/auth/magic_link/send",
            body=maybe_transform(
                {
                    "email": email,
                    "verify_host": verify_host,
                },
                magic_link_send_params.MagicLinkSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MagicLinkSendResponse,
        )

    def verify(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MagicLinkVerifyResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/auth/magic_link/verify",
            body=maybe_transform({"token": token}, magic_link_verify_params.MagicLinkVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MagicLinkVerifyResponse,
        )


class AsyncMagicLinkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMagicLinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/composiohq/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncMagicLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMagicLinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/composiohq/composio-base-py#with_streaming_response
        """
        return AsyncMagicLinkResourceWithStreamingResponse(self)

    async def send(
        self,
        *,
        email: str,
        verify_host: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MagicLinkSendResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/auth/magic_link/send",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "verify_host": verify_host,
                },
                magic_link_send_params.MagicLinkSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MagicLinkSendResponse,
        )

    async def verify(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MagicLinkVerifyResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/auth/magic_link/verify",
            body=await async_maybe_transform({"token": token}, magic_link_verify_params.MagicLinkVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MagicLinkVerifyResponse,
        )


class MagicLinkResourceWithRawResponse:
    def __init__(self, magic_link: MagicLinkResource) -> None:
        self._magic_link = magic_link

        self.send = to_raw_response_wrapper(
            magic_link.send,
        )
        self.verify = to_raw_response_wrapper(
            magic_link.verify,
        )


class AsyncMagicLinkResourceWithRawResponse:
    def __init__(self, magic_link: AsyncMagicLinkResource) -> None:
        self._magic_link = magic_link

        self.send = async_to_raw_response_wrapper(
            magic_link.send,
        )
        self.verify = async_to_raw_response_wrapper(
            magic_link.verify,
        )


class MagicLinkResourceWithStreamingResponse:
    def __init__(self, magic_link: MagicLinkResource) -> None:
        self._magic_link = magic_link

        self.send = to_streamed_response_wrapper(
            magic_link.send,
        )
        self.verify = to_streamed_response_wrapper(
            magic_link.verify,
        )


class AsyncMagicLinkResourceWithStreamingResponse:
    def __init__(self, magic_link: AsyncMagicLinkResource) -> None:
        self._magic_link = magic_link

        self.send = async_to_streamed_response_wrapper(
            magic_link.send,
        )
        self.verify = async_to_streamed_response_wrapper(
            magic_link.verify,
        )
