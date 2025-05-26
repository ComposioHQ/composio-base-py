# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.trigger_instances.manage_delete_response import ManageDeleteResponse

__all__ = ["ManageResource", "AsyncManageResource"]


class ManageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return ManageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return ManageResourceWithStreamingResponse(self)

    def delete(
        self,
        trigger_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManageDeleteResponse:
        """
        Args:
          trigger_id: The ID of the trigger instance to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return self._delete(
            f"/api/v3/trigger_instances/manage/{trigger_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManageDeleteResponse,
        )


class AsyncManageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncManageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncManageResourceWithStreamingResponse(self)

    async def delete(
        self,
        trigger_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManageDeleteResponse:
        """
        Args:
          trigger_id: The ID of the trigger instance to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return await self._delete(
            f"/api/v3/trigger_instances/manage/{trigger_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManageDeleteResponse,
        )


class ManageResourceWithRawResponse:
    def __init__(self, manage: ManageResource) -> None:
        self._manage = manage

        self.delete = to_raw_response_wrapper(
            manage.delete,
        )


class AsyncManageResourceWithRawResponse:
    def __init__(self, manage: AsyncManageResource) -> None:
        self._manage = manage

        self.delete = async_to_raw_response_wrapper(
            manage.delete,
        )


class ManageResourceWithStreamingResponse:
    def __init__(self, manage: ManageResource) -> None:
        self._manage = manage

        self.delete = to_streamed_response_wrapper(
            manage.delete,
        )


class AsyncManageResourceWithStreamingResponse:
    def __init__(self, manage: AsyncManageResource) -> None:
        self._manage = manage

        self.delete = async_to_streamed_response_wrapper(
            manage.delete,
        )
