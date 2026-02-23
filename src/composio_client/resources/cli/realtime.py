# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cli import realtime_auth_params
from ..._base_client import make_request_options
from ...types.cli.realtime_auth_response import RealtimeAuthResponse
from ...types.cli.realtime_credentials_response import RealtimeCredentialsResponse

__all__ = ["RealtimeResource", "AsyncRealtimeResource"]


class RealtimeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RealtimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return RealtimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealtimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return RealtimeResourceWithStreamingResponse(self)

    def auth(
        self,
        *,
        channel_name: str,
        socket_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealtimeAuthResponse:
        """
        Authenticate CLI client access to a private-cli-{nanoId} Pusher channel

        Args:
          channel_name: The channel name to authenticate for

          socket_id: The socket ID for Pusher authentication

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/cli/realtime/auth",
            body=maybe_transform(
                {
                    "channel_name": channel_name,
                    "socket_id": socket_id,
                },
                realtime_auth_params.RealtimeAuthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeAuthResponse,
        )

    def credentials(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealtimeCredentialsResponse:
        """Get the Pusher key and project nanoId for the CLI realtime trigger channel.

        The
        CLI subscribes to private-cli-{project_id}.
        """
        return self._get(
            "/api/v3/cli/realtime/credentials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeCredentialsResponse,
        )


class AsyncRealtimeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRealtimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncRealtimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealtimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncRealtimeResourceWithStreamingResponse(self)

    async def auth(
        self,
        *,
        channel_name: str,
        socket_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealtimeAuthResponse:
        """
        Authenticate CLI client access to a private-cli-{nanoId} Pusher channel

        Args:
          channel_name: The channel name to authenticate for

          socket_id: The socket ID for Pusher authentication

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/cli/realtime/auth",
            body=await async_maybe_transform(
                {
                    "channel_name": channel_name,
                    "socket_id": socket_id,
                },
                realtime_auth_params.RealtimeAuthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeAuthResponse,
        )

    async def credentials(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealtimeCredentialsResponse:
        """Get the Pusher key and project nanoId for the CLI realtime trigger channel.

        The
        CLI subscribes to private-cli-{project_id}.
        """
        return await self._get(
            "/api/v3/cli/realtime/credentials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeCredentialsResponse,
        )


class RealtimeResourceWithRawResponse:
    def __init__(self, realtime: RealtimeResource) -> None:
        self._realtime = realtime

        self.auth = to_raw_response_wrapper(
            realtime.auth,
        )
        self.credentials = to_raw_response_wrapper(
            realtime.credentials,
        )


class AsyncRealtimeResourceWithRawResponse:
    def __init__(self, realtime: AsyncRealtimeResource) -> None:
        self._realtime = realtime

        self.auth = async_to_raw_response_wrapper(
            realtime.auth,
        )
        self.credentials = async_to_raw_response_wrapper(
            realtime.credentials,
        )


class RealtimeResourceWithStreamingResponse:
    def __init__(self, realtime: RealtimeResource) -> None:
        self._realtime = realtime

        self.auth = to_streamed_response_wrapper(
            realtime.auth,
        )
        self.credentials = to_streamed_response_wrapper(
            realtime.credentials,
        )


class AsyncRealtimeResourceWithStreamingResponse:
    def __init__(self, realtime: AsyncRealtimeResource) -> None:
        self._realtime = realtime

        self.auth = async_to_streamed_response_wrapper(
            realtime.auth,
        )
        self.credentials = async_to_streamed_response_wrapper(
            realtime.credentials,
        )
