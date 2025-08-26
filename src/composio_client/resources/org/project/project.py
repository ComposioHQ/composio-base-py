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
from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ProjectResource", "AsyncProjectResource"]


class ProjectResource(SyncAPIResource):
    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def trigger(self) -> TriggerResource:
        return TriggerResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return ProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return ProjectResourceWithStreamingResponse(self)


class AsyncProjectResource(AsyncAPIResource):
    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def trigger(self) -> AsyncTriggerResource:
        return AsyncTriggerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncProjectResourceWithStreamingResponse(self)


class ProjectResourceWithRawResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._project.api_keys)

    @cached_property
    def trigger(self) -> TriggerResourceWithRawResponse:
        return TriggerResourceWithRawResponse(self._project.trigger)


class AsyncProjectResourceWithRawResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._project.api_keys)

    @cached_property
    def trigger(self) -> AsyncTriggerResourceWithRawResponse:
        return AsyncTriggerResourceWithRawResponse(self._project.trigger)


class ProjectResourceWithStreamingResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._project.api_keys)

    @cached_property
    def trigger(self) -> TriggerResourceWithStreamingResponse:
        return TriggerResourceWithStreamingResponse(self._project.trigger)


class AsyncProjectResourceWithStreamingResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._project.api_keys)

    @cached_property
    def trigger(self) -> AsyncTriggerResourceWithStreamingResponse:
        return AsyncTriggerResourceWithStreamingResponse(self._project.trigger)
