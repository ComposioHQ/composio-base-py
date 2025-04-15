# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import cli_link_session_params, cli_retrieve_session_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.cli_link_session_response import CliLinkSessionResponse
from ..types.cli_create_session_response import CliCreateSessionResponse
from ..types.cli_retrieve_session_response import CliRetrieveSessionResponse

__all__ = ["CliResource", "AsyncCliResource"]


class CliResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CliResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return CliResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CliResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return CliResourceWithStreamingResponse(self)

    def create_session(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CliCreateSessionResponse:
        return self._post(
            "/api/v3/cli/create-session",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CliCreateSessionResponse,
        )

    def link_session(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CliLinkSessionResponse:
        """
        Args:
          id: CLI session ID or code to link

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/v3/cli/link-session",
            body=maybe_transform({"id": id}, cli_link_session_params.CliLinkSessionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CliLinkSessionResponse,
        )

    def retrieve_session(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CliRetrieveSessionResponse:
        """
        Args:
          id: CLI session ID or code to check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/cli/get-session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, cli_retrieve_session_params.CliRetrieveSessionParams),
            ),
            cast_to=CliRetrieveSessionResponse,
        )


class AsyncCliResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCliResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncCliResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCliResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncCliResourceWithStreamingResponse(self)

    async def create_session(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CliCreateSessionResponse:
        return await self._post(
            "/api/v3/cli/create-session",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CliCreateSessionResponse,
        )

    async def link_session(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CliLinkSessionResponse:
        """
        Args:
          id: CLI session ID or code to link

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/v3/cli/link-session",
            body=await async_maybe_transform({"id": id}, cli_link_session_params.CliLinkSessionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CliLinkSessionResponse,
        )

    async def retrieve_session(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CliRetrieveSessionResponse:
        """
        Args:
          id: CLI session ID or code to check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/cli/get-session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, cli_retrieve_session_params.CliRetrieveSessionParams),
            ),
            cast_to=CliRetrieveSessionResponse,
        )


class CliResourceWithRawResponse:
    def __init__(self, cli: CliResource) -> None:
        self._cli = cli

        self.create_session = to_raw_response_wrapper(
            cli.create_session,
        )
        self.link_session = to_raw_response_wrapper(
            cli.link_session,
        )
        self.retrieve_session = to_raw_response_wrapper(
            cli.retrieve_session,
        )


class AsyncCliResourceWithRawResponse:
    def __init__(self, cli: AsyncCliResource) -> None:
        self._cli = cli

        self.create_session = async_to_raw_response_wrapper(
            cli.create_session,
        )
        self.link_session = async_to_raw_response_wrapper(
            cli.link_session,
        )
        self.retrieve_session = async_to_raw_response_wrapper(
            cli.retrieve_session,
        )


class CliResourceWithStreamingResponse:
    def __init__(self, cli: CliResource) -> None:
        self._cli = cli

        self.create_session = to_streamed_response_wrapper(
            cli.create_session,
        )
        self.link_session = to_streamed_response_wrapper(
            cli.link_session,
        )
        self.retrieve_session = to_streamed_response_wrapper(
            cli.retrieve_session,
        )


class AsyncCliResourceWithStreamingResponse:
    def __init__(self, cli: AsyncCliResource) -> None:
        self._cli = cli

        self.create_session = async_to_streamed_response_wrapper(
            cli.create_session,
        )
        self.link_session = async_to_streamed_response_wrapper(
            cli.link_session,
        )
        self.retrieve_session = async_to_streamed_response_wrapper(
            cli.retrieve_session,
        )
