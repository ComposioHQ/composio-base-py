# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .session import (
    SessionResource,
    AsyncSessionResource,
    SessionResourceWithRawResponse,
    AsyncSessionResourceWithRawResponse,
    SessionResourceWithStreamingResponse,
    AsyncSessionResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

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


class ToolRouterResourceWithRawResponse:
    def __init__(self, tool_router: ToolRouterResource) -> None:
        self._tool_router = tool_router

    @cached_property
    def session(self) -> SessionResourceWithRawResponse:
        return SessionResourceWithRawResponse(self._tool_router.session)


class AsyncToolRouterResourceWithRawResponse:
    def __init__(self, tool_router: AsyncToolRouterResource) -> None:
        self._tool_router = tool_router

    @cached_property
    def session(self) -> AsyncSessionResourceWithRawResponse:
        return AsyncSessionResourceWithRawResponse(self._tool_router.session)


class ToolRouterResourceWithStreamingResponse:
    def __init__(self, tool_router: ToolRouterResource) -> None:
        self._tool_router = tool_router

    @cached_property
    def session(self) -> SessionResourceWithStreamingResponse:
        return SessionResourceWithStreamingResponse(self._tool_router.session)


class AsyncToolRouterResourceWithStreamingResponse:
    def __init__(self, tool_router: AsyncToolRouterResource) -> None:
        self._tool_router = tool_router

    @cached_property
    def session(self) -> AsyncSessionResourceWithStreamingResponse:
        return AsyncSessionResourceWithStreamingResponse(self._tool_router.session)
