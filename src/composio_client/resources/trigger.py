# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import trigger_log_params
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
from ..types.trigger_log_response import TriggerLogResponse

__all__ = ["TriggerResource", "AsyncTriggerResource"]


class TriggerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TriggerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return TriggerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TriggerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return TriggerResourceWithStreamingResponse(self)

    def log(
        self,
        *,
        cursor: Optional[str],
        entity_id: str | NotGiven = NOT_GIVEN,
        integration_id: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        status: Literal["all", "success", "error"] | NotGiven = NOT_GIVEN,
        time: Literal["5m", "30m", "6h", "1d", "1w", "1month", "1y"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerLogResponse:
        """
        Search and retrieve trigger event logs

        Args:
          cursor: cursor that can be used to paginate through the logs

          limit: number of logs to return

          search: Search term to filter logs

          status: Filter logs by their status level

          time: Return logs from the last N time units

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/internal/trigger/logs",
            body=maybe_transform(
                {
                    "cursor": cursor,
                    "entity_id": entity_id,
                    "integration_id": integration_id,
                    "limit": limit,
                    "search": search,
                    "status": status,
                    "time": time,
                },
                trigger_log_params.TriggerLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerLogResponse,
        )


class AsyncTriggerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTriggerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncTriggerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTriggerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncTriggerResourceWithStreamingResponse(self)

    async def log(
        self,
        *,
        cursor: Optional[str],
        entity_id: str | NotGiven = NOT_GIVEN,
        integration_id: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        status: Literal["all", "success", "error"] | NotGiven = NOT_GIVEN,
        time: Literal["5m", "30m", "6h", "1d", "1w", "1month", "1y"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerLogResponse:
        """
        Search and retrieve trigger event logs

        Args:
          cursor: cursor that can be used to paginate through the logs

          limit: number of logs to return

          search: Search term to filter logs

          status: Filter logs by their status level

          time: Return logs from the last N time units

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/internal/trigger/logs",
            body=await async_maybe_transform(
                {
                    "cursor": cursor,
                    "entity_id": entity_id,
                    "integration_id": integration_id,
                    "limit": limit,
                    "search": search,
                    "status": status,
                    "time": time,
                },
                trigger_log_params.TriggerLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerLogResponse,
        )


class TriggerResourceWithRawResponse:
    def __init__(self, trigger: TriggerResource) -> None:
        self._trigger = trigger

        self.log = to_raw_response_wrapper(
            trigger.log,
        )


class AsyncTriggerResourceWithRawResponse:
    def __init__(self, trigger: AsyncTriggerResource) -> None:
        self._trigger = trigger

        self.log = async_to_raw_response_wrapper(
            trigger.log,
        )


class TriggerResourceWithStreamingResponse:
    def __init__(self, trigger: TriggerResource) -> None:
        self._trigger = trigger

        self.log = to_streamed_response_wrapper(
            trigger.log,
        )


class AsyncTriggerResourceWithStreamingResponse:
    def __init__(self, trigger: AsyncTriggerResource) -> None:
        self._trigger = trigger

        self.log = async_to_streamed_response_wrapper(
            trigger.log,
        )
