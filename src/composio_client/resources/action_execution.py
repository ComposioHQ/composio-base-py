# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import action_execution_log_params
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
from ..types.action_execution_log_response import ActionExecutionLogResponse
from ..types.action_execution_retrieve_log_response import ActionExecutionRetrieveLogResponse
from ..types.action_execution_retrieve_fields_response import ActionExecutionRetrieveFieldsResponse

__all__ = ["ActionExecutionResource", "AsyncActionExecutionResource"]


class ActionExecutionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionExecutionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return ActionExecutionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionExecutionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return ActionExecutionResourceWithStreamingResponse(self)

    def log(
        self,
        *,
        cursor: Optional[float],
        case_sensitive: bool | NotGiven = NOT_GIVEN,
        from_: float | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        search_params: Iterable[action_execution_log_params.SearchParam] | NotGiven = NOT_GIVEN,
        to: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionExecutionLogResponse:
        """
        Search and retrieve action execution logs

        Args:
          cursor: cursor_that_can_be_used_to_paginate_through_the_logs

          case_sensitive: whether_the_search_is_case_sensitive_or_not

          from_: start_time_of_the_logs_in_epoch_time

          limit: number_of_logs_to_return

          to: end_time_of_the_logs_in_epoch_time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/internal/action_execution/logs",
            body=maybe_transform(
                {
                    "cursor": cursor,
                    "case_sensitive": case_sensitive,
                    "from_": from_,
                    "limit": limit,
                    "search_params": search_params,
                    "to": to,
                },
                action_execution_log_params.ActionExecutionLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionExecutionLogResponse,
        )

    def retrieve_fields(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionExecutionRetrieveFieldsResponse:
        """Get action log fields for filtering"""
        return self._get(
            "/api/v3/internal/action_execution/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionExecutionRetrieveFieldsResponse,
        )

    def retrieve_log(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionExecutionRetrieveLogResponse:
        """
        Get detailed execution log by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v3/internal/action_execution/log/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionExecutionRetrieveLogResponse,
        )


class AsyncActionExecutionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionExecutionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncActionExecutionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionExecutionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncActionExecutionResourceWithStreamingResponse(self)

    async def log(
        self,
        *,
        cursor: Optional[float],
        case_sensitive: bool | NotGiven = NOT_GIVEN,
        from_: float | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        search_params: Iterable[action_execution_log_params.SearchParam] | NotGiven = NOT_GIVEN,
        to: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionExecutionLogResponse:
        """
        Search and retrieve action execution logs

        Args:
          cursor: cursor_that_can_be_used_to_paginate_through_the_logs

          case_sensitive: whether_the_search_is_case_sensitive_or_not

          from_: start_time_of_the_logs_in_epoch_time

          limit: number_of_logs_to_return

          to: end_time_of_the_logs_in_epoch_time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/internal/action_execution/logs",
            body=await async_maybe_transform(
                {
                    "cursor": cursor,
                    "case_sensitive": case_sensitive,
                    "from_": from_,
                    "limit": limit,
                    "search_params": search_params,
                    "to": to,
                },
                action_execution_log_params.ActionExecutionLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionExecutionLogResponse,
        )

    async def retrieve_fields(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionExecutionRetrieveFieldsResponse:
        """Get action log fields for filtering"""
        return await self._get(
            "/api/v3/internal/action_execution/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionExecutionRetrieveFieldsResponse,
        )

    async def retrieve_log(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionExecutionRetrieveLogResponse:
        """
        Get detailed execution log by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v3/internal/action_execution/log/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionExecutionRetrieveLogResponse,
        )


class ActionExecutionResourceWithRawResponse:
    def __init__(self, action_execution: ActionExecutionResource) -> None:
        self._action_execution = action_execution

        self.log = to_raw_response_wrapper(
            action_execution.log,
        )
        self.retrieve_fields = to_raw_response_wrapper(
            action_execution.retrieve_fields,
        )
        self.retrieve_log = to_raw_response_wrapper(
            action_execution.retrieve_log,
        )


class AsyncActionExecutionResourceWithRawResponse:
    def __init__(self, action_execution: AsyncActionExecutionResource) -> None:
        self._action_execution = action_execution

        self.log = async_to_raw_response_wrapper(
            action_execution.log,
        )
        self.retrieve_fields = async_to_raw_response_wrapper(
            action_execution.retrieve_fields,
        )
        self.retrieve_log = async_to_raw_response_wrapper(
            action_execution.retrieve_log,
        )


class ActionExecutionResourceWithStreamingResponse:
    def __init__(self, action_execution: ActionExecutionResource) -> None:
        self._action_execution = action_execution

        self.log = to_streamed_response_wrapper(
            action_execution.log,
        )
        self.retrieve_fields = to_streamed_response_wrapper(
            action_execution.retrieve_fields,
        )
        self.retrieve_log = to_streamed_response_wrapper(
            action_execution.retrieve_log,
        )


class AsyncActionExecutionResourceWithStreamingResponse:
    def __init__(self, action_execution: AsyncActionExecutionResource) -> None:
        self._action_execution = action_execution

        self.log = async_to_streamed_response_wrapper(
            action_execution.log,
        )
        self.retrieve_fields = async_to_streamed_response_wrapper(
            action_execution.retrieve_fields,
        )
        self.retrieve_log = async_to_streamed_response_wrapper(
            action_execution.retrieve_log,
        )
