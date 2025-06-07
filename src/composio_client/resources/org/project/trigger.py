# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.org.project import trigger_update_params
from ....types.org.project.trigger_list_response import TriggerListResponse
from ....types.org.project.trigger_update_response import TriggerUpdateResponse

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

    def update(
        self,
        *,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerUpdateResponse:
        """Updates the trigger enablement status for the current project.

        Use this endpoint
        to enable or disable triggers for automated workflows within a project.

        Args:
          enabled: Boolean flag indicating whether triggers should be enabled (true) or disabled
              (false) for the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/api/v3/org/project/trigger",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"enabled": enabled}, trigger_update_params.TriggerUpdateParams),
            ),
            cast_to=TriggerUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerListResponse:
        """
        Retrieves the current project details including its trigger enablement status.
        Use this endpoint to check whether triggers are currently enabled or disabled
        for a project.
        """
        return self._get(
            "/api/v3/org/project/trigger",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerListResponse,
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

    async def update(
        self,
        *,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerUpdateResponse:
        """Updates the trigger enablement status for the current project.

        Use this endpoint
        to enable or disable triggers for automated workflows within a project.

        Args:
          enabled: Boolean flag indicating whether triggers should be enabled (true) or disabled
              (false) for the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/api/v3/org/project/trigger",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"enabled": enabled}, trigger_update_params.TriggerUpdateParams),
            ),
            cast_to=TriggerUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerListResponse:
        """
        Retrieves the current project details including its trigger enablement status.
        Use this endpoint to check whether triggers are currently enabled or disabled
        for a project.
        """
        return await self._get(
            "/api/v3/org/project/trigger",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerListResponse,
        )


class TriggerResourceWithRawResponse:
    def __init__(self, trigger: TriggerResource) -> None:
        self._trigger = trigger

        self.update = to_raw_response_wrapper(
            trigger.update,
        )
        self.list = to_raw_response_wrapper(
            trigger.list,
        )


class AsyncTriggerResourceWithRawResponse:
    def __init__(self, trigger: AsyncTriggerResource) -> None:
        self._trigger = trigger

        self.update = async_to_raw_response_wrapper(
            trigger.update,
        )
        self.list = async_to_raw_response_wrapper(
            trigger.list,
        )


class TriggerResourceWithStreamingResponse:
    def __init__(self, trigger: TriggerResource) -> None:
        self._trigger = trigger

        self.update = to_streamed_response_wrapper(
            trigger.update,
        )
        self.list = to_streamed_response_wrapper(
            trigger.list,
        )


class AsyncTriggerResourceWithStreamingResponse:
    def __init__(self, trigger: AsyncTriggerResource) -> None:
        self._trigger = trigger

        self.update = async_to_streamed_response_wrapper(
            trigger.update,
        )
        self.list = async_to_streamed_response_wrapper(
            trigger.list,
        )
