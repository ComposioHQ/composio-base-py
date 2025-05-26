# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import migration_retrieve_nanoid_params
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
from ..types.migration_retrieve_nanoid_response import MigrationRetrieveNanoidResponse

__all__ = ["MigrationResource", "AsyncMigrationResource"]


class MigrationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MigrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return MigrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MigrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return MigrationResourceWithStreamingResponse(self)

    def retrieve_nanoid(
        self,
        *,
        type: Literal["CONNECTED_ACCOUNT", "AUTH_CONFIG", "TRIGGER_INSTANCE"],
        uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationRetrieveNanoidResponse:
        """Convert a legacy UUID to its corresponding NanoId for migration purposes.

        This
        endpoint facilitates the transition from UUID-based identifiers to the more
        compact NanoId format used in the v3 API.

        Args:
          type: The type of resource that the UUID belongs to

          uuid: The legacy UUID that needs to be converted to a NanoId

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/migration/get-nanoid",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "type": type,
                        "uuid": uuid,
                    },
                    migration_retrieve_nanoid_params.MigrationRetrieveNanoidParams,
                ),
            ),
            cast_to=MigrationRetrieveNanoidResponse,
        )


class AsyncMigrationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMigrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncMigrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMigrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncMigrationResourceWithStreamingResponse(self)

    async def retrieve_nanoid(
        self,
        *,
        type: Literal["CONNECTED_ACCOUNT", "AUTH_CONFIG", "TRIGGER_INSTANCE"],
        uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationRetrieveNanoidResponse:
        """Convert a legacy UUID to its corresponding NanoId for migration purposes.

        This
        endpoint facilitates the transition from UUID-based identifiers to the more
        compact NanoId format used in the v3 API.

        Args:
          type: The type of resource that the UUID belongs to

          uuid: The legacy UUID that needs to be converted to a NanoId

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/migration/get-nanoid",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "type": type,
                        "uuid": uuid,
                    },
                    migration_retrieve_nanoid_params.MigrationRetrieveNanoidParams,
                ),
            ),
            cast_to=MigrationRetrieveNanoidResponse,
        )


class MigrationResourceWithRawResponse:
    def __init__(self, migration: MigrationResource) -> None:
        self._migration = migration

        self.retrieve_nanoid = to_raw_response_wrapper(
            migration.retrieve_nanoid,
        )


class AsyncMigrationResourceWithRawResponse:
    def __init__(self, migration: AsyncMigrationResource) -> None:
        self._migration = migration

        self.retrieve_nanoid = async_to_raw_response_wrapper(
            migration.retrieve_nanoid,
        )


class MigrationResourceWithStreamingResponse:
    def __init__(self, migration: MigrationResource) -> None:
        self._migration = migration

        self.retrieve_nanoid = to_streamed_response_wrapper(
            migration.retrieve_nanoid,
        )


class AsyncMigrationResourceWithStreamingResponse:
    def __init__(self, migration: AsyncMigrationResource) -> None:
        self._migration = migration

        self.retrieve_nanoid = async_to_streamed_response_wrapper(
            migration.retrieve_nanoid,
        )
