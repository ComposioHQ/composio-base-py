# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.cli_create_session_response import CliCreateSessionResponse

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CliCreateSessionResponse:
        """Generates a new CLI session with a random 6-character code.

        This endpoint is the
        first step in the CLI authentication flow, creating a session that can later be
        linked to a user account. The generated code is displayed to the user in the CLI
        and should be entered in the web interface to complete authentication.
        """
        return self._post(
            "/api/v3/cli/create-session",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CliCreateSessionResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CliCreateSessionResponse:
        """Generates a new CLI session with a random 6-character code.

        This endpoint is the
        first step in the CLI authentication flow, creating a session that can later be
        linked to a user account. The generated code is displayed to the user in the CLI
        and should be entered in the web interface to complete authentication.
        """
        return await self._post(
            "/api/v3/cli/create-session",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CliCreateSessionResponse,
        )


class CliResourceWithRawResponse:
    def __init__(self, cli: CliResource) -> None:
        self._cli = cli

        self.create_session = to_raw_response_wrapper(
            cli.create_session,
        )


class AsyncCliResourceWithRawResponse:
    def __init__(self, cli: AsyncCliResource) -> None:
        self._cli = cli

        self.create_session = async_to_raw_response_wrapper(
            cli.create_session,
        )


class CliResourceWithStreamingResponse:
    def __init__(self, cli: CliResource) -> None:
        self._cli = cli

        self.create_session = to_streamed_response_wrapper(
            cli.create_session,
        )


class AsyncCliResourceWithStreamingResponse:
    def __init__(self, cli: AsyncCliResource) -> None:
        self._cli = cli

        self.create_session = async_to_streamed_response_wrapper(
            cli.create_session,
        )
