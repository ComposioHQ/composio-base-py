# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

from .handle import (
    HandleResource,
    AsyncHandleResource,
    HandleResourceWithRawResponse,
    AsyncHandleResourceWithRawResponse,
    HandleResourceWithStreamingResponse,
    AsyncHandleResourceWithStreamingResponse,
)
from ...types import trigger_instance_upsert_params, trigger_instance_list_active_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.trigger_instance_upsert_response import TriggerInstanceUpsertResponse
from ...types.trigger_instance_list_active_response import TriggerInstanceListActiveResponse
from ...types.trigger_instance_remove_upsert_response import TriggerInstanceRemoveUpsertResponse
from ...types.trigger_instance_update_status_response import TriggerInstanceUpdateStatusResponse

__all__ = ["TriggerInstancesResource", "AsyncTriggerInstancesResource"]


class TriggerInstancesResource(SyncAPIResource):
    @cached_property
    def handle(self) -> HandleResource:
        return HandleResource(self._client)

    @cached_property
    def with_raw_response(self) -> TriggerInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return TriggerInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TriggerInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return TriggerInstancesResourceWithStreamingResponse(self)

    def list_active(
        self,
        *,
        auth_config_ids: str | List[str] | NotGiven = NOT_GIVEN,
        connected_account_ids: str | List[str] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        show_disabled: Optional[bool] | NotGiven = NOT_GIVEN,
        trigger_ids: str | List[str] | NotGiven = NOT_GIVEN,
        trigger_names: str | List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceListActiveResponse:
        """
        Args:
          auth_config_ids: List of auth config IDs to filter triggers by

          connected_account_ids: List of connected account IDs to filter triggers by

          limit: Number of items to return per page.

          page: Page number for pagination. Starts from 1.

          show_disabled: When set to true, includes disabled triggers in the response.

          trigger_ids: List of trigger IDs to filter triggers by

          trigger_names: List of trigger names to filter triggers by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/trigger_instances/active",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "auth_config_ids": auth_config_ids,
                        "connected_account_ids": connected_account_ids,
                        "limit": limit,
                        "page": page,
                        "show_disabled": show_disabled,
                        "trigger_ids": trigger_ids,
                        "trigger_names": trigger_names,
                    },
                    trigger_instance_list_active_params.TriggerInstanceListActiveParams,
                ),
            ),
            cast_to=TriggerInstanceListActiveResponse,
        )

    def remove_upsert(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceRemoveUpsertResponse:
        """
        Args:
          slug: The slug of the trigger instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            f"/api/v3/trigger_instances/{slug}/upsert",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerInstanceRemoveUpsertResponse,
        )

    def update_status(
        self,
        status: Literal["enable", "disable"],
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceUpdateStatusResponse:
        """
        Args:
          slug: The slug of the trigger instance

          status: The new status of the trigger

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not status:
            raise ValueError(f"Expected a non-empty value for `status` but received {status!r}")
        return self._patch(
            f"/api/v3/trigger_instances/{slug}/status/{status}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerInstanceUpdateStatusResponse,
        )

    def upsert(
        self,
        slug: str,
        *,
        connected_auth_id: str,
        trigger_config: Dict[str, Optional[object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceUpsertResponse:
        """
        Args:
          slug: The slug of the trigger instance

          connected_auth_id: Connection ID

          trigger_config: Trigger configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            f"/api/v3/trigger_instances/{slug}/upsert",
            body=maybe_transform(
                {
                    "connected_auth_id": connected_auth_id,
                    "trigger_config": trigger_config,
                },
                trigger_instance_upsert_params.TriggerInstanceUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerInstanceUpsertResponse,
        )


class AsyncTriggerInstancesResource(AsyncAPIResource):
    @cached_property
    def handle(self) -> AsyncHandleResource:
        return AsyncHandleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTriggerInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncTriggerInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTriggerInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncTriggerInstancesResourceWithStreamingResponse(self)

    async def list_active(
        self,
        *,
        auth_config_ids: str | List[str] | NotGiven = NOT_GIVEN,
        connected_account_ids: str | List[str] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        show_disabled: Optional[bool] | NotGiven = NOT_GIVEN,
        trigger_ids: str | List[str] | NotGiven = NOT_GIVEN,
        trigger_names: str | List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceListActiveResponse:
        """
        Args:
          auth_config_ids: List of auth config IDs to filter triggers by

          connected_account_ids: List of connected account IDs to filter triggers by

          limit: Number of items to return per page.

          page: Page number for pagination. Starts from 1.

          show_disabled: When set to true, includes disabled triggers in the response.

          trigger_ids: List of trigger IDs to filter triggers by

          trigger_names: List of trigger names to filter triggers by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/trigger_instances/active",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "auth_config_ids": auth_config_ids,
                        "connected_account_ids": connected_account_ids,
                        "limit": limit,
                        "page": page,
                        "show_disabled": show_disabled,
                        "trigger_ids": trigger_ids,
                        "trigger_names": trigger_names,
                    },
                    trigger_instance_list_active_params.TriggerInstanceListActiveParams,
                ),
            ),
            cast_to=TriggerInstanceListActiveResponse,
        )

    async def remove_upsert(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceRemoveUpsertResponse:
        """
        Args:
          slug: The slug of the trigger instance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            f"/api/v3/trigger_instances/{slug}/upsert",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerInstanceRemoveUpsertResponse,
        )

    async def update_status(
        self,
        status: Literal["enable", "disable"],
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceUpdateStatusResponse:
        """
        Args:
          slug: The slug of the trigger instance

          status: The new status of the trigger

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not status:
            raise ValueError(f"Expected a non-empty value for `status` but received {status!r}")
        return await self._patch(
            f"/api/v3/trigger_instances/{slug}/status/{status}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerInstanceUpdateStatusResponse,
        )

    async def upsert(
        self,
        slug: str,
        *,
        connected_auth_id: str,
        trigger_config: Dict[str, Optional[object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceUpsertResponse:
        """
        Args:
          slug: The slug of the trigger instance

          connected_auth_id: Connection ID

          trigger_config: Trigger configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            f"/api/v3/trigger_instances/{slug}/upsert",
            body=await async_maybe_transform(
                {
                    "connected_auth_id": connected_auth_id,
                    "trigger_config": trigger_config,
                },
                trigger_instance_upsert_params.TriggerInstanceUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerInstanceUpsertResponse,
        )


class TriggerInstancesResourceWithRawResponse:
    def __init__(self, trigger_instances: TriggerInstancesResource) -> None:
        self._trigger_instances = trigger_instances

        self.list_active = to_raw_response_wrapper(
            trigger_instances.list_active,
        )
        self.remove_upsert = to_raw_response_wrapper(
            trigger_instances.remove_upsert,
        )
        self.update_status = to_raw_response_wrapper(
            trigger_instances.update_status,
        )
        self.upsert = to_raw_response_wrapper(
            trigger_instances.upsert,
        )

    @cached_property
    def handle(self) -> HandleResourceWithRawResponse:
        return HandleResourceWithRawResponse(self._trigger_instances.handle)


class AsyncTriggerInstancesResourceWithRawResponse:
    def __init__(self, trigger_instances: AsyncTriggerInstancesResource) -> None:
        self._trigger_instances = trigger_instances

        self.list_active = async_to_raw_response_wrapper(
            trigger_instances.list_active,
        )
        self.remove_upsert = async_to_raw_response_wrapper(
            trigger_instances.remove_upsert,
        )
        self.update_status = async_to_raw_response_wrapper(
            trigger_instances.update_status,
        )
        self.upsert = async_to_raw_response_wrapper(
            trigger_instances.upsert,
        )

    @cached_property
    def handle(self) -> AsyncHandleResourceWithRawResponse:
        return AsyncHandleResourceWithRawResponse(self._trigger_instances.handle)


class TriggerInstancesResourceWithStreamingResponse:
    def __init__(self, trigger_instances: TriggerInstancesResource) -> None:
        self._trigger_instances = trigger_instances

        self.list_active = to_streamed_response_wrapper(
            trigger_instances.list_active,
        )
        self.remove_upsert = to_streamed_response_wrapper(
            trigger_instances.remove_upsert,
        )
        self.update_status = to_streamed_response_wrapper(
            trigger_instances.update_status,
        )
        self.upsert = to_streamed_response_wrapper(
            trigger_instances.upsert,
        )

    @cached_property
    def handle(self) -> HandleResourceWithStreamingResponse:
        return HandleResourceWithStreamingResponse(self._trigger_instances.handle)


class AsyncTriggerInstancesResourceWithStreamingResponse:
    def __init__(self, trigger_instances: AsyncTriggerInstancesResource) -> None:
        self._trigger_instances = trigger_instances

        self.list_active = async_to_streamed_response_wrapper(
            trigger_instances.list_active,
        )
        self.remove_upsert = async_to_streamed_response_wrapper(
            trigger_instances.remove_upsert,
        )
        self.update_status = async_to_streamed_response_wrapper(
            trigger_instances.update_status,
        )
        self.upsert = async_to_streamed_response_wrapper(
            trigger_instances.upsert,
        )

    @cached_property
    def handle(self) -> AsyncHandleResourceWithStreamingResponse:
        return AsyncHandleResourceWithStreamingResponse(self._trigger_instances.handle)
