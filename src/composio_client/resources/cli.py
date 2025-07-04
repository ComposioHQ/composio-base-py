# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import cli_get_session_params, cli_link_session_params
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
from ..types.cli_get_session_response import CliGetSessionResponse
from ..types.cli_link_session_response import CliLinkSessionResponse
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def get_session(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CliGetSessionResponse:
        """
        Retrieves the current state of a CLI session using either the session ID (UUID)
        or the 6-character code. This endpoint is used by both the CLI client to check
        if the session has been linked, and by the web interface to display session
        details before linking.

        Args:
          id: CLI session ID (UUID format) or 6-character code to check. Both formats are
              supported for flexibility in client implementations.

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
                query=maybe_transform({"id": id}, cli_get_session_params.CliGetSessionParams),
            ),
            cast_to=CliGetSessionResponse,
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
        """Links a pending CLI session to the currently authenticated user.

        This is the
        final step in the CLI authentication flow, where the user enters the code in the
        web interface and their account is associated with the CLI session, allowing the
        CLI to act on their behalf.

        Args:
          id: The CLI session ID or code to link to the current user

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

    async def get_session(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CliGetSessionResponse:
        """
        Retrieves the current state of a CLI session using either the session ID (UUID)
        or the 6-character code. This endpoint is used by both the CLI client to check
        if the session has been linked, and by the web interface to display session
        details before linking.

        Args:
          id: CLI session ID (UUID format) or 6-character code to check. Both formats are
              supported for flexibility in client implementations.

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
                query=await async_maybe_transform({"id": id}, cli_get_session_params.CliGetSessionParams),
            ),
            cast_to=CliGetSessionResponse,
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
        """Links a pending CLI session to the currently authenticated user.

        This is the
        final step in the CLI authentication flow, where the user enters the code in the
        web interface and their account is associated with the CLI session, allowing the
        CLI to act on their behalf.

        Args:
          id: The CLI session ID or code to link to the current user

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


class CliResourceWithRawResponse:
    def __init__(self, cli: CliResource) -> None:
        self._cli = cli

        self.create_session = to_raw_response_wrapper(
            cli.create_session,
        )
        self.get_session = to_raw_response_wrapper(
            cli.get_session,
        )
        self.link_session = to_raw_response_wrapper(
            cli.link_session,
        )


class AsyncCliResourceWithRawResponse:
    def __init__(self, cli: AsyncCliResource) -> None:
        self._cli = cli

        self.create_session = async_to_raw_response_wrapper(
            cli.create_session,
        )
        self.get_session = async_to_raw_response_wrapper(
            cli.get_session,
        )
        self.link_session = async_to_raw_response_wrapper(
            cli.link_session,
        )


class CliResourceWithStreamingResponse:
    def __init__(self, cli: CliResource) -> None:
        self._cli = cli

        self.create_session = to_streamed_response_wrapper(
            cli.create_session,
        )
        self.get_session = to_streamed_response_wrapper(
            cli.get_session,
        )
        self.link_session = to_streamed_response_wrapper(
            cli.link_session,
        )


class AsyncCliResourceWithStreamingResponse:
    def __init__(self, cli: AsyncCliResource) -> None:
        self._cli = cli

        self.create_session = async_to_streamed_response_wrapper(
            cli.create_session,
        )
        self.get_session = async_to_streamed_response_wrapper(
            cli.get_session,
        )
        self.link_session = async_to_streamed_response_wrapper(
            cli.link_session,
        )
