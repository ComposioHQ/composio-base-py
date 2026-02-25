# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

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
from ...types.logs import trigger_list_params
from ..._base_client import make_request_options
from ...types.logs.trigger_list_response import TriggerListResponse
from ...types.logs.trigger_retrieve_response import TriggerRetrieveResponse

__all__ = ["TriggersResource", "AsyncTriggersResource"]


class TriggersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TriggersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return TriggersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TriggersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return TriggersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerRetrieveResponse:
        """
        Get detailed trigger log by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v3/internal/trigger/log/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        entity_id: str | Omit = omit,
        from_: Optional[float] | Omit = omit,
        include_payload: bool | Omit = omit,
        integration_id: str | Omit = omit,
        limit: Optional[float] | Omit = omit,
        search: str | Omit = omit,
        search_params: Iterable[trigger_list_params.SearchParam] | Omit = omit,
        status: Literal["all", "success", "error"] | Omit = omit,
        time: Literal["5m", "30m", "6h", "1d", "1w", "1month", "1y"] | Omit = omit,
        to: Optional[float] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerListResponse:
        """
        Search and retrieve trigger event logs with advanced filtering capabilities
        including search parameters

        Args:
          from_: Start time for logs (epoch timestamp in milliseconds)

          include_payload: Whether to include payload fields in the response. Set to false for faster list
              views.

          limit: The limit of trigger logs to return

          search: Search term to filter logs

          search_params: Advanced search parameters for filtering logs

          status: Filter logs by their status level

          time: Return logs from the last N time units

          to: End time for logs (epoch timestamp in milliseconds)

          user_id: Filter logs by user ID

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
                    "from_": from_,
                    "include_payload": include_payload,
                    "integration_id": integration_id,
                    "limit": limit,
                    "search": search,
                    "search_params": search_params,
                    "status": status,
                    "time": time,
                    "to": to,
                    "user_id": user_id,
                },
                trigger_list_params.TriggerListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerListResponse,
        )


class AsyncTriggersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTriggersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncTriggersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTriggersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncTriggersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerRetrieveResponse:
        """
        Get detailed trigger log by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v3/internal/trigger/log/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerRetrieveResponse,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        entity_id: str | Omit = omit,
        from_: Optional[float] | Omit = omit,
        include_payload: bool | Omit = omit,
        integration_id: str | Omit = omit,
        limit: Optional[float] | Omit = omit,
        search: str | Omit = omit,
        search_params: Iterable[trigger_list_params.SearchParam] | Omit = omit,
        status: Literal["all", "success", "error"] | Omit = omit,
        time: Literal["5m", "30m", "6h", "1d", "1w", "1month", "1y"] | Omit = omit,
        to: Optional[float] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerListResponse:
        """
        Search and retrieve trigger event logs with advanced filtering capabilities
        including search parameters

        Args:
          from_: Start time for logs (epoch timestamp in milliseconds)

          include_payload: Whether to include payload fields in the response. Set to false for faster list
              views.

          limit: The limit of trigger logs to return

          search: Search term to filter logs

          search_params: Advanced search parameters for filtering logs

          status: Filter logs by their status level

          time: Return logs from the last N time units

          to: End time for logs (epoch timestamp in milliseconds)

          user_id: Filter logs by user ID

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
                    "from_": from_,
                    "include_payload": include_payload,
                    "integration_id": integration_id,
                    "limit": limit,
                    "search": search,
                    "search_params": search_params,
                    "status": status,
                    "time": time,
                    "to": to,
                    "user_id": user_id,
                },
                trigger_list_params.TriggerListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerListResponse,
        )


class TriggersResourceWithRawResponse:
    def __init__(self, triggers: TriggersResource) -> None:
        self._triggers = triggers

        self.retrieve = to_raw_response_wrapper(
            triggers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            triggers.list,
        )


class AsyncTriggersResourceWithRawResponse:
    def __init__(self, triggers: AsyncTriggersResource) -> None:
        self._triggers = triggers

        self.retrieve = async_to_raw_response_wrapper(
            triggers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            triggers.list,
        )


class TriggersResourceWithStreamingResponse:
    def __init__(self, triggers: TriggersResource) -> None:
        self._triggers = triggers

        self.retrieve = to_streamed_response_wrapper(
            triggers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            triggers.list,
        )


class AsyncTriggersResourceWithStreamingResponse:
    def __init__(self, triggers: AsyncTriggersResource) -> None:
        self._triggers = triggers

        self.retrieve = async_to_streamed_response_wrapper(
            triggers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            triggers.list,
        )
