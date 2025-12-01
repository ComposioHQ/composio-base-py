# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.tool_router import (
    session_link_params,
    session_create_params,
    session_execute_params,
    session_toolkits_params,
)
from ...types.tool_router.session_link_response import SessionLinkResponse
from ...types.tool_router.session_create_response import SessionCreateResponse
from ...types.tool_router.session_execute_response import SessionExecuteResponse
from ...types.tool_router.session_retrieve_response import SessionRetrieveResponse
from ...types.tool_router.session_toolkits_response import SessionToolkitsResponse

__all__ = ["SessionResource", "AsyncSessionResource"]


class SessionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return SessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return SessionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        user_id: str,
        auth_configs: Dict[str, str] | Omit = omit,
        connected_accounts: Dict[str, str] | Omit = omit,
        connections: session_create_params.Connections | Omit = omit,
        execution: session_create_params.Execution | Omit = omit,
        toolkits: session_create_params.Toolkits | Omit = omit,
        tools: session_create_params.Tools | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionCreateResponse:
        """Creates a new session for the tool router feature.

        This endpoint initializes a
        new session with specified toolkits and their authentication configurations. The
        session provides an isolated environment for testing and managing tool routing
        logic with scoped MCP server access.

        Args:
          user_id: The identifier of the user who is initiating the session, ideally a unique
              identifier from your database like a user ID or email address

          auth_configs: The auth configs to use for the session. This will override the default behavior
              and use the given auth config when specific toolkits are being executed

          connected_accounts: The connected accounts to use for the session. This will override the default
              behaviour and use the given connected account when specific toolkits are being
              executed

          connections: Configuration for connection management settings

          execution: Configuration for workbench behavior including security restrictions and
              execution limits

          toolkits: Toolkit configuration - specify either enabled toolkits (allowlist) or disabled
              toolkits (denylist). Mutually exclusive.

          tools: Configuration for tool overrides and filtering

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/tool_router/session",
            body=maybe_transform(
                {
                    "user_id": user_id,
                    "auth_configs": auth_configs,
                    "connected_accounts": connected_accounts,
                    "connections": connections,
                    "execution": execution,
                    "toolkits": toolkits,
                    "tools": tools,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCreateResponse,
        )

    def retrieve(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveResponse:
        """Retrieves an existing tool router session by its ID.

        Returns the session
        configuration, MCP server URL, and available tools.

        Args:
          session_id: The session ID returned when creating the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/api/v3/tool_router/session/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRetrieveResponse,
        )

    def execute(
        self,
        session_id: str,
        *,
        tool_slug: str,
        arguments: Dict[str, Optional[object]] | Omit = omit,
        x_session_access_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExecuteResponse:
        """Executes a specific tool within a tool router session.

        The toolkit is
        automatically inferred from the tool slug. The tool must belong to an allowed
        toolkit and must not be disabled in the session configuration. This endpoint
        validates permissions, resolves connected accounts, and executes the tool with
        the session context.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          tool_slug: The unique slug identifier of the tool to execute

          arguments: The arguments required by the tool

          x_session_access_key: Session access key for sandbox/workbench authentication. Alternative to
              x-api-key for internal tool router endpoints.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {**strip_not_given({"x-session-access-key": x_session_access_key}), **(extra_headers or {})}
        return self._post(
            f"/api/v3/tool_router/session/{session_id}/execute",
            body=maybe_transform(
                {
                    "tool_slug": tool_slug,
                    "arguments": arguments,
                },
                session_execute_params.SessionExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionExecuteResponse,
        )

    def link(
        self,
        session_id: str,
        *,
        toolkit: str,
        callback_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionLinkResponse:
        """
        Initiates an authentication link session for a specific toolkit within a tool
        router session. Returns a link token and redirect URL that users can use to
        complete the OAuth flow.

        Args:
          session_id: The session ID returned when creating the session

          toolkit: The unique slug identifier of the toolkit to connect

          callback_url: URL where users will be redirected after completing auth

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/api/v3/tool_router/session/{session_id}/link",
            body=maybe_transform(
                {
                    "toolkit": toolkit,
                    "callback_url": callback_url,
                },
                session_link_params.SessionLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionLinkResponse,
        )

    def toolkits(
        self,
        session_id: str,
        *,
        cursor: str | Omit = omit,
        limit: Optional[float] | Omit = omit,
        toolkits: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionToolkitsResponse:
        """
        Retrieves a cursor-paginated list of toolkits available in the tool router
        session. Includes toolkit metadata, composio-managed auth schemes, and connected
        accounts if available. Optionally filter by specific toolkit slugs.

        Args:
          session_id: The session ID returned when creating the session

          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          limit: Number of items per page, max allowed is 1000

          toolkits: Optional comma-separated list of toolkit slugs to filter by. If provided, only
              these toolkits will be returned, overriding the session configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/api/v3/tool_router/session/{session_id}/toolkits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "toolkits": toolkits,
                    },
                    session_toolkits_params.SessionToolkitsParams,
                ),
            ),
            cast_to=SessionToolkitsResponse,
        )


class AsyncSessionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncSessionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        user_id: str,
        auth_configs: Dict[str, str] | Omit = omit,
        connected_accounts: Dict[str, str] | Omit = omit,
        connections: session_create_params.Connections | Omit = omit,
        execution: session_create_params.Execution | Omit = omit,
        toolkits: session_create_params.Toolkits | Omit = omit,
        tools: session_create_params.Tools | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionCreateResponse:
        """Creates a new session for the tool router feature.

        This endpoint initializes a
        new session with specified toolkits and their authentication configurations. The
        session provides an isolated environment for testing and managing tool routing
        logic with scoped MCP server access.

        Args:
          user_id: The identifier of the user who is initiating the session, ideally a unique
              identifier from your database like a user ID or email address

          auth_configs: The auth configs to use for the session. This will override the default behavior
              and use the given auth config when specific toolkits are being executed

          connected_accounts: The connected accounts to use for the session. This will override the default
              behaviour and use the given connected account when specific toolkits are being
              executed

          connections: Configuration for connection management settings

          execution: Configuration for workbench behavior including security restrictions and
              execution limits

          toolkits: Toolkit configuration - specify either enabled toolkits (allowlist) or disabled
              toolkits (denylist). Mutually exclusive.

          tools: Configuration for tool overrides and filtering

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/tool_router/session",
            body=await async_maybe_transform(
                {
                    "user_id": user_id,
                    "auth_configs": auth_configs,
                    "connected_accounts": connected_accounts,
                    "connections": connections,
                    "execution": execution,
                    "toolkits": toolkits,
                    "tools": tools,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCreateResponse,
        )

    async def retrieve(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveResponse:
        """Retrieves an existing tool router session by its ID.

        Returns the session
        configuration, MCP server URL, and available tools.

        Args:
          session_id: The session ID returned when creating the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/api/v3/tool_router/session/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRetrieveResponse,
        )

    async def execute(
        self,
        session_id: str,
        *,
        tool_slug: str,
        arguments: Dict[str, Optional[object]] | Omit = omit,
        x_session_access_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExecuteResponse:
        """Executes a specific tool within a tool router session.

        The toolkit is
        automatically inferred from the tool slug. The tool must belong to an allowed
        toolkit and must not be disabled in the session configuration. This endpoint
        validates permissions, resolves connected accounts, and executes the tool with
        the session context.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          tool_slug: The unique slug identifier of the tool to execute

          arguments: The arguments required by the tool

          x_session_access_key: Session access key for sandbox/workbench authentication. Alternative to
              x-api-key for internal tool router endpoints.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {**strip_not_given({"x-session-access-key": x_session_access_key}), **(extra_headers or {})}
        return await self._post(
            f"/api/v3/tool_router/session/{session_id}/execute",
            body=await async_maybe_transform(
                {
                    "tool_slug": tool_slug,
                    "arguments": arguments,
                },
                session_execute_params.SessionExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionExecuteResponse,
        )

    async def link(
        self,
        session_id: str,
        *,
        toolkit: str,
        callback_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionLinkResponse:
        """
        Initiates an authentication link session for a specific toolkit within a tool
        router session. Returns a link token and redirect URL that users can use to
        complete the OAuth flow.

        Args:
          session_id: The session ID returned when creating the session

          toolkit: The unique slug identifier of the toolkit to connect

          callback_url: URL where users will be redirected after completing auth

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/api/v3/tool_router/session/{session_id}/link",
            body=await async_maybe_transform(
                {
                    "toolkit": toolkit,
                    "callback_url": callback_url,
                },
                session_link_params.SessionLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionLinkResponse,
        )

    async def toolkits(
        self,
        session_id: str,
        *,
        cursor: str | Omit = omit,
        limit: Optional[float] | Omit = omit,
        toolkits: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionToolkitsResponse:
        """
        Retrieves a cursor-paginated list of toolkits available in the tool router
        session. Includes toolkit metadata, composio-managed auth schemes, and connected
        accounts if available. Optionally filter by specific toolkit slugs.

        Args:
          session_id: The session ID returned when creating the session

          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          limit: Number of items per page, max allowed is 1000

          toolkits: Optional comma-separated list of toolkit slugs to filter by. If provided, only
              these toolkits will be returned, overriding the session configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/api/v3/tool_router/session/{session_id}/toolkits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "toolkits": toolkits,
                    },
                    session_toolkits_params.SessionToolkitsParams,
                ),
            ),
            cast_to=SessionToolkitsResponse,
        )


class SessionResourceWithRawResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_raw_response_wrapper(
            session.create,
        )
        self.retrieve = to_raw_response_wrapper(
            session.retrieve,
        )
        self.execute = to_raw_response_wrapper(
            session.execute,
        )
        self.link = to_raw_response_wrapper(
            session.link,
        )
        self.toolkits = to_raw_response_wrapper(
            session.toolkits,
        )


class AsyncSessionResourceWithRawResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_raw_response_wrapper(
            session.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            session.retrieve,
        )
        self.execute = async_to_raw_response_wrapper(
            session.execute,
        )
        self.link = async_to_raw_response_wrapper(
            session.link,
        )
        self.toolkits = async_to_raw_response_wrapper(
            session.toolkits,
        )


class SessionResourceWithStreamingResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_streamed_response_wrapper(
            session.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            session.retrieve,
        )
        self.execute = to_streamed_response_wrapper(
            session.execute,
        )
        self.link = to_streamed_response_wrapper(
            session.link,
        )
        self.toolkits = to_streamed_response_wrapper(
            session.toolkits,
        )


class AsyncSessionResourceWithStreamingResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_streamed_response_wrapper(
            session.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            session.retrieve,
        )
        self.execute = async_to_streamed_response_wrapper(
            session.execute,
        )
        self.link = async_to_streamed_response_wrapper(
            session.link,
        )
        self.toolkits = async_to_streamed_response_wrapper(
            session.toolkits,
        )
