# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import tool_router_create_session_params
from .session import (
    SessionResource,
    AsyncSessionResource,
    SessionResourceWithRawResponse,
    AsyncSessionResourceWithRawResponse,
    SessionResourceWithStreamingResponse,
    AsyncSessionResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.tool_router_create_session_response import ToolRouterCreateSessionResponse

__all__ = ["ToolRouterResource", "AsyncToolRouterResource"]


class ToolRouterResource(SyncAPIResource):
    @cached_property
    def session(self) -> SessionResource:
        return SessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> ToolRouterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return ToolRouterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolRouterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return ToolRouterResourceWithStreamingResponse(self)

    def create_session(
        self,
        *,
        user_id: str,
        config: tool_router_create_session_params.Config | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRouterCreateSessionResponse:
        """Creates a new session for the tool router lab feature (Legacy).

        This endpoint
        initializes a new session with specified toolkits and their authentication
        configurations. The session provides an isolated environment for testing and
        managing tool routing logic with scoped MCP server access.

        Args:
          user_id: Unique user identifier for the session owner

          config: Session configuration including enabled toolkits and their auth configs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/labs/tool_router/session",
            body=maybe_transform(
                {
                    "user_id": user_id,
                    "config": config,
                },
                tool_router_create_session_params.ToolRouterCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRouterCreateSessionResponse,
        )


class AsyncToolRouterResource(AsyncAPIResource):
    @cached_property
    def session(self) -> AsyncSessionResource:
        return AsyncSessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncToolRouterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncToolRouterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolRouterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncToolRouterResourceWithStreamingResponse(self)

    async def create_session(
        self,
        *,
        user_id: str,
        config: tool_router_create_session_params.Config | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRouterCreateSessionResponse:
        """Creates a new session for the tool router lab feature (Legacy).

        This endpoint
        initializes a new session with specified toolkits and their authentication
        configurations. The session provides an isolated environment for testing and
        managing tool routing logic with scoped MCP server access.

        Args:
          user_id: Unique user identifier for the session owner

          config: Session configuration including enabled toolkits and their auth configs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/labs/tool_router/session",
            body=await async_maybe_transform(
                {
                    "user_id": user_id,
                    "config": config,
                },
                tool_router_create_session_params.ToolRouterCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRouterCreateSessionResponse,
        )


class ToolRouterResourceWithRawResponse:
    def __init__(self, tool_router: ToolRouterResource) -> None:
        self._tool_router = tool_router

        self.create_session = to_raw_response_wrapper(
            tool_router.create_session,
        )

    @cached_property
    def session(self) -> SessionResourceWithRawResponse:
        return SessionResourceWithRawResponse(self._tool_router.session)


class AsyncToolRouterResourceWithRawResponse:
    def __init__(self, tool_router: AsyncToolRouterResource) -> None:
        self._tool_router = tool_router

        self.create_session = async_to_raw_response_wrapper(
            tool_router.create_session,
        )

    @cached_property
    def session(self) -> AsyncSessionResourceWithRawResponse:
        return AsyncSessionResourceWithRawResponse(self._tool_router.session)


class ToolRouterResourceWithStreamingResponse:
    def __init__(self, tool_router: ToolRouterResource) -> None:
        self._tool_router = tool_router

        self.create_session = to_streamed_response_wrapper(
            tool_router.create_session,
        )

    @cached_property
    def session(self) -> SessionResourceWithStreamingResponse:
        return SessionResourceWithStreamingResponse(self._tool_router.session)


class AsyncToolRouterResourceWithStreamingResponse:
    def __init__(self, tool_router: AsyncToolRouterResource) -> None:
        self._tool_router = tool_router

        self.create_session = async_to_streamed_response_wrapper(
            tool_router.create_session,
        )

    @cached_property
    def session(self) -> AsyncSessionResourceWithStreamingResponse:
        return AsyncSessionResourceWithStreamingResponse(self._tool_router.session)
