# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .trigger import (
    TriggerResource,
    AsyncTriggerResource,
    TriggerResourceWithRawResponse,
    AsyncTriggerResourceWithRawResponse,
    TriggerResourceWithStreamingResponse,
    AsyncTriggerResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .action_execution import (
    ActionExecutionResource,
    AsyncActionExecutionResource,
    ActionExecutionResourceWithRawResponse,
    AsyncActionExecutionResourceWithRawResponse,
    ActionExecutionResourceWithStreamingResponse,
    AsyncActionExecutionResourceWithStreamingResponse,
)

__all__ = ["InternalResource", "AsyncInternalResource"]


class InternalResource(SyncAPIResource):
    @cached_property
    def trigger(self) -> TriggerResource:
        return TriggerResource(self._client)

    @cached_property
    def action_execution(self) -> ActionExecutionResource:
        return ActionExecutionResource(self._client)

    @cached_property
    def with_raw_response(self) -> InternalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return InternalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InternalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return InternalResourceWithStreamingResponse(self)


class AsyncInternalResource(AsyncAPIResource):
    @cached_property
    def trigger(self) -> AsyncTriggerResource:
        return AsyncTriggerResource(self._client)

    @cached_property
    def action_execution(self) -> AsyncActionExecutionResource:
        return AsyncActionExecutionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInternalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncInternalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInternalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncInternalResourceWithStreamingResponse(self)


class InternalResourceWithRawResponse:
    def __init__(self, internal: InternalResource) -> None:
        self._internal = internal

    @cached_property
    def trigger(self) -> TriggerResourceWithRawResponse:
        return TriggerResourceWithRawResponse(self._internal.trigger)

    @cached_property
    def action_execution(self) -> ActionExecutionResourceWithRawResponse:
        return ActionExecutionResourceWithRawResponse(self._internal.action_execution)


class AsyncInternalResourceWithRawResponse:
    def __init__(self, internal: AsyncInternalResource) -> None:
        self._internal = internal

    @cached_property
    def trigger(self) -> AsyncTriggerResourceWithRawResponse:
        return AsyncTriggerResourceWithRawResponse(self._internal.trigger)

    @cached_property
    def action_execution(self) -> AsyncActionExecutionResourceWithRawResponse:
        return AsyncActionExecutionResourceWithRawResponse(self._internal.action_execution)


class InternalResourceWithStreamingResponse:
    def __init__(self, internal: InternalResource) -> None:
        self._internal = internal

    @cached_property
    def trigger(self) -> TriggerResourceWithStreamingResponse:
        return TriggerResourceWithStreamingResponse(self._internal.trigger)

    @cached_property
    def action_execution(self) -> ActionExecutionResourceWithStreamingResponse:
        return ActionExecutionResourceWithStreamingResponse(self._internal.action_execution)


class AsyncInternalResourceWithStreamingResponse:
    def __init__(self, internal: AsyncInternalResource) -> None:
        self._internal = internal

    @cached_property
    def trigger(self) -> AsyncTriggerResourceWithStreamingResponse:
        return AsyncTriggerResourceWithStreamingResponse(self._internal.trigger)

    @cached_property
    def action_execution(self) -> AsyncActionExecutionResourceWithStreamingResponse:
        return AsyncActionExecutionResourceWithStreamingResponse(self._internal.action_execution)
