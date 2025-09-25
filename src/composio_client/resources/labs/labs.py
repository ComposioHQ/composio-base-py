# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .tool_router import (
    ToolRouterResource,
    AsyncToolRouterResource,
    ToolRouterResourceWithRawResponse,
    AsyncToolRouterResourceWithRawResponse,
    ToolRouterResourceWithStreamingResponse,
    AsyncToolRouterResourceWithStreamingResponse,
)

__all__ = ["LabsResource", "AsyncLabsResource"]


class LabsResource(SyncAPIResource):
    @cached_property
    def tool_router(self) -> ToolRouterResource:
        return ToolRouterResource(self._client)

    @cached_property
    def with_raw_response(self) -> LabsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return LabsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return LabsResourceWithStreamingResponse(self)


class AsyncLabsResource(AsyncAPIResource):
    @cached_property
    def tool_router(self) -> AsyncToolRouterResource:
        return AsyncToolRouterResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLabsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncLabsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncLabsResourceWithStreamingResponse(self)


class LabsResourceWithRawResponse:
    def __init__(self, labs: LabsResource) -> None:
        self._labs = labs

    @cached_property
    def tool_router(self) -> ToolRouterResourceWithRawResponse:
        return ToolRouterResourceWithRawResponse(self._labs.tool_router)


class AsyncLabsResourceWithRawResponse:
    def __init__(self, labs: AsyncLabsResource) -> None:
        self._labs = labs

    @cached_property
    def tool_router(self) -> AsyncToolRouterResourceWithRawResponse:
        return AsyncToolRouterResourceWithRawResponse(self._labs.tool_router)


class LabsResourceWithStreamingResponse:
    def __init__(self, labs: LabsResource) -> None:
        self._labs = labs

    @cached_property
    def tool_router(self) -> ToolRouterResourceWithStreamingResponse:
        return ToolRouterResourceWithStreamingResponse(self._labs.tool_router)


class AsyncLabsResourceWithStreamingResponse:
    def __init__(self, labs: AsyncLabsResource) -> None:
        self._labs = labs

    @cached_property
    def tool_router(self) -> AsyncToolRouterResourceWithStreamingResponse:
        return AsyncToolRouterResourceWithStreamingResponse(self._labs.tool_router)
