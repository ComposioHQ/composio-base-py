# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from .triggers import (
    TriggersResource,
    AsyncTriggersResource,
    TriggersResourceWithRawResponse,
    AsyncTriggersResourceWithRawResponse,
    TriggersResourceWithStreamingResponse,
    AsyncTriggersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def triggers(self) -> TriggersResource:
        """Logging and monitoring"""
        return TriggersResource(self._client)

    @cached_property
    def tools(self) -> ToolsResource:
        """Logging and monitoring"""
        return ToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def triggers(self) -> AsyncTriggersResource:
        """Logging and monitoring"""
        return AsyncTriggersResource(self._client)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        """Logging and monitoring"""
        return AsyncToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

    @cached_property
    def triggers(self) -> TriggersResourceWithRawResponse:
        """Logging and monitoring"""
        return TriggersResourceWithRawResponse(self._logs.triggers)

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        """Logging and monitoring"""
        return ToolsResourceWithRawResponse(self._logs.tools)


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

    @cached_property
    def triggers(self) -> AsyncTriggersResourceWithRawResponse:
        """Logging and monitoring"""
        return AsyncTriggersResourceWithRawResponse(self._logs.triggers)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        """Logging and monitoring"""
        return AsyncToolsResourceWithRawResponse(self._logs.tools)


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

    @cached_property
    def triggers(self) -> TriggersResourceWithStreamingResponse:
        """Logging and monitoring"""
        return TriggersResourceWithStreamingResponse(self._logs.triggers)

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        """Logging and monitoring"""
        return ToolsResourceWithStreamingResponse(self._logs.tools)


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

    @cached_property
    def triggers(self) -> AsyncTriggersResourceWithStreamingResponse:
        """Logging and monitoring"""
        return AsyncTriggersResourceWithStreamingResponse(self._logs.triggers)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        """Logging and monitoring"""
        return AsyncToolsResourceWithStreamingResponse(self._logs.tools)
