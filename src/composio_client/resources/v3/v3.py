# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cli import (
    CliResource,
    AsyncCliResource,
    CliResourceWithRawResponse,
    AsyncCliResourceWithRawResponse,
    CliResourceWithStreamingResponse,
    AsyncCliResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .auth.auth import (
    AuthResource,
    AsyncAuthResource,
    AuthResourceWithRawResponse,
    AsyncAuthResourceWithRawResponse,
    AuthResourceWithStreamingResponse,
    AsyncAuthResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .internal.internal import (
    InternalResource,
    AsyncInternalResource,
    InternalResourceWithRawResponse,
    AsyncInternalResourceWithRawResponse,
    InternalResourceWithStreamingResponse,
    AsyncInternalResourceWithStreamingResponse,
)

__all__ = ["V3Resource", "AsyncV3Resource"]


class V3Resource(SyncAPIResource):
    @cached_property
    def auth(self) -> AuthResource:
        return AuthResource(self._client)

    @cached_property
    def cli(self) -> CliResource:
        return CliResource(self._client)

    @cached_property
    def internal(self) -> InternalResource:
        return InternalResource(self._client)

    @cached_property
    def with_raw_response(self) -> V3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return V3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return V3ResourceWithStreamingResponse(self)


class AsyncV3Resource(AsyncAPIResource):
    @cached_property
    def auth(self) -> AsyncAuthResource:
        return AsyncAuthResource(self._client)

    @cached_property
    def cli(self) -> AsyncCliResource:
        return AsyncCliResource(self._client)

    @cached_property
    def internal(self) -> AsyncInternalResource:
        return AsyncInternalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncV3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncV3ResourceWithStreamingResponse(self)


class V3ResourceWithRawResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

    @cached_property
    def auth(self) -> AuthResourceWithRawResponse:
        return AuthResourceWithRawResponse(self._v3.auth)

    @cached_property
    def cli(self) -> CliResourceWithRawResponse:
        return CliResourceWithRawResponse(self._v3.cli)

    @cached_property
    def internal(self) -> InternalResourceWithRawResponse:
        return InternalResourceWithRawResponse(self._v3.internal)


class AsyncV3ResourceWithRawResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

    @cached_property
    def auth(self) -> AsyncAuthResourceWithRawResponse:
        return AsyncAuthResourceWithRawResponse(self._v3.auth)

    @cached_property
    def cli(self) -> AsyncCliResourceWithRawResponse:
        return AsyncCliResourceWithRawResponse(self._v3.cli)

    @cached_property
    def internal(self) -> AsyncInternalResourceWithRawResponse:
        return AsyncInternalResourceWithRawResponse(self._v3.internal)


class V3ResourceWithStreamingResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

    @cached_property
    def auth(self) -> AuthResourceWithStreamingResponse:
        return AuthResourceWithStreamingResponse(self._v3.auth)

    @cached_property
    def cli(self) -> CliResourceWithStreamingResponse:
        return CliResourceWithStreamingResponse(self._v3.cli)

    @cached_property
    def internal(self) -> InternalResourceWithStreamingResponse:
        return InternalResourceWithStreamingResponse(self._v3.internal)


class AsyncV3ResourceWithStreamingResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

    @cached_property
    def auth(self) -> AsyncAuthResourceWithStreamingResponse:
        return AsyncAuthResourceWithStreamingResponse(self._v3.auth)

    @cached_property
    def cli(self) -> AsyncCliResourceWithStreamingResponse:
        return AsyncCliResourceWithStreamingResponse(self._v3.cli)

    @cached_property
    def internal(self) -> AsyncInternalResourceWithStreamingResponse:
        return AsyncInternalResourceWithStreamingResponse(self._v3.internal)
