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
from ...types.trigger_instance_delete_response import TriggerInstanceDeleteResponse
from ...types.trigger_instance_upsert_response import TriggerInstanceUpsertResponse
from ...types.trigger_instance_list_active_response import TriggerInstanceListActiveResponse
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
    ) -> TriggerInstanceDeleteResponse:
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
            f"/api/v3/trigger_instances/delete/{trigger_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerInstanceDeleteResponse,
        )

    def list_active(
        self,
        *,
        query_auth_config_ids_1: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_auth_config_ids_2: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_connected_account_ids_1: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_connected_account_ids_2: Optional[List[str]] | NotGiven = NOT_GIVEN,
        deprecated_auth_config_uuids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        deprecated_connected_account_uuids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        query_show_disabled_1: Optional[bool] | NotGiven = NOT_GIVEN,
        query_show_disabled_2: Optional[bool] | NotGiven = NOT_GIVEN,
        query_trigger_ids_1: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_trigger_names_1: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_trigger_ids_2: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_trigger_names_2: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceListActiveResponse:
        """
        Args:
          query_auth_config_ids_1: Array of auth config IDs to filter triggers by

          query_auth_config_ids_2: DEPRECATED: This parameter will be removed in a future version. Please use
              auth_config_ids instead.

          query_connected_account_ids_1: Array of connected account IDs to filter triggers by

          query_connected_account_ids_2: DEPRECATED: This parameter will be removed in a future version. Please use
              connected_account_ids instead.

          deprecated_auth_config_uuids: Array of auth config UUIDs to filter triggers by

          deprecated_connected_account_uuids: Array of connected account UUIDs to filter triggers by

          limit: Number of items to return per page.

          page: Page number for pagination. Starts from 1.

          query_show_disabled_1: When set to true, includes disabled triggers in the response.

          query_show_disabled_2: DEPRECATED: This parameter will be removed in a future version. Please use
              show_disabled instead.

          query_trigger_ids_1: Array of trigger IDs to filter triggers by

          query_trigger_names_1: Array of trigger names to filter triggers by

          query_trigger_ids_2: DEPRECATED: This parameter will be removed in a future version. Please use
              trigger_ids instead.

          query_trigger_names_2: DEPRECATED: This parameter will be removed in a future version. Please use
              trigger_names instead.

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
                        "query_auth_config_ids_1": query_auth_config_ids_1,
                        "query_auth_config_ids_2": query_auth_config_ids_2,
                        "query_connected_account_ids_1": query_connected_account_ids_1,
                        "query_connected_account_ids_2": query_connected_account_ids_2,
                        "deprecated_auth_config_uuids": deprecated_auth_config_uuids,
                        "deprecated_connected_account_uuids": deprecated_connected_account_uuids,
                        "limit": limit,
                        "page": page,
                        "query_show_disabled_1": query_show_disabled_1,
                        "query_show_disabled_2": query_show_disabled_2,
                        "query_trigger_ids_1": query_trigger_ids_1,
                        "query_trigger_names_1": query_trigger_names_1,
                        "query_trigger_ids_2": query_trigger_ids_2,
                        "query_trigger_names_2": query_trigger_names_2,
                    },
                    trigger_instance_list_active_params.TriggerInstanceListActiveParams,
                ),
            ),
            cast_to=TriggerInstanceListActiveResponse,
        )

    def update_status(
        self,
        status: Literal["enable", "disable"],
        *,
        trigger_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceUpdateStatusResponse:
        """
        Args:
          trigger_id: The ID of the trigger instance to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        if not status:
            raise ValueError(f"Expected a non-empty value for `status` but received {status!r}")
        return self._patch(
            f"/api/v3/trigger_instances/id/{trigger_id}/{status}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerInstanceUpdateStatusResponse,
        )

    def upsert(
        self,
        slug: str,
        *,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        connected_auth_id: str | NotGiven = NOT_GIVEN,
        body_trigger_config_1: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        body_trigger_config_2: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
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

          connected_account_id: Connected account nanoid

          connected_auth_id: DEPRECATED: This parameter will be removed in a future version. Please use
              connected_account_id instead.

          body_trigger_config_1: Trigger configuration

          body_trigger_config_2: Trigger configuration (deprecated)

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
                    "connected_account_id": connected_account_id,
                    "connected_auth_id": connected_auth_id,
                    "body_trigger_config_1": body_trigger_config_1,
                    "body_trigger_config_2": body_trigger_config_2,
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
    ) -> TriggerInstanceDeleteResponse:
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
            f"/api/v3/trigger_instances/delete/{trigger_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerInstanceDeleteResponse,
        )

    async def list_active(
        self,
        *,
        query_auth_config_ids_1: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_auth_config_ids_2: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_connected_account_ids_1: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_connected_account_ids_2: Optional[List[str]] | NotGiven = NOT_GIVEN,
        deprecated_auth_config_uuids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        deprecated_connected_account_uuids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        query_show_disabled_1: Optional[bool] | NotGiven = NOT_GIVEN,
        query_show_disabled_2: Optional[bool] | NotGiven = NOT_GIVEN,
        query_trigger_ids_1: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_trigger_names_1: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_trigger_ids_2: Optional[List[str]] | NotGiven = NOT_GIVEN,
        query_trigger_names_2: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceListActiveResponse:
        """
        Args:
          query_auth_config_ids_1: Array of auth config IDs to filter triggers by

          query_auth_config_ids_2: DEPRECATED: This parameter will be removed in a future version. Please use
              auth_config_ids instead.

          query_connected_account_ids_1: Array of connected account IDs to filter triggers by

          query_connected_account_ids_2: DEPRECATED: This parameter will be removed in a future version. Please use
              connected_account_ids instead.

          deprecated_auth_config_uuids: Array of auth config UUIDs to filter triggers by

          deprecated_connected_account_uuids: Array of connected account UUIDs to filter triggers by

          limit: Number of items to return per page.

          page: Page number for pagination. Starts from 1.

          query_show_disabled_1: When set to true, includes disabled triggers in the response.

          query_show_disabled_2: DEPRECATED: This parameter will be removed in a future version. Please use
              show_disabled instead.

          query_trigger_ids_1: Array of trigger IDs to filter triggers by

          query_trigger_names_1: Array of trigger names to filter triggers by

          query_trigger_ids_2: DEPRECATED: This parameter will be removed in a future version. Please use
              trigger_ids instead.

          query_trigger_names_2: DEPRECATED: This parameter will be removed in a future version. Please use
              trigger_names instead.

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
                        "query_auth_config_ids_1": query_auth_config_ids_1,
                        "query_auth_config_ids_2": query_auth_config_ids_2,
                        "query_connected_account_ids_1": query_connected_account_ids_1,
                        "query_connected_account_ids_2": query_connected_account_ids_2,
                        "deprecated_auth_config_uuids": deprecated_auth_config_uuids,
                        "deprecated_connected_account_uuids": deprecated_connected_account_uuids,
                        "limit": limit,
                        "page": page,
                        "query_show_disabled_1": query_show_disabled_1,
                        "query_show_disabled_2": query_show_disabled_2,
                        "query_trigger_ids_1": query_trigger_ids_1,
                        "query_trigger_names_1": query_trigger_names_1,
                        "query_trigger_ids_2": query_trigger_ids_2,
                        "query_trigger_names_2": query_trigger_names_2,
                    },
                    trigger_instance_list_active_params.TriggerInstanceListActiveParams,
                ),
            ),
            cast_to=TriggerInstanceListActiveResponse,
        )

    async def update_status(
        self,
        status: Literal["enable", "disable"],
        *,
        trigger_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TriggerInstanceUpdateStatusResponse:
        """
        Args:
          trigger_id: The ID of the trigger instance to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        if not status:
            raise ValueError(f"Expected a non-empty value for `status` but received {status!r}")
        return await self._patch(
            f"/api/v3/trigger_instances/id/{trigger_id}/{status}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerInstanceUpdateStatusResponse,
        )

    async def upsert(
        self,
        slug: str,
        *,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        connected_auth_id: str | NotGiven = NOT_GIVEN,
        body_trigger_config_1: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        body_trigger_config_2: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
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

          connected_account_id: Connected account nanoid

          connected_auth_id: DEPRECATED: This parameter will be removed in a future version. Please use
              connected_account_id instead.

          body_trigger_config_1: Trigger configuration

          body_trigger_config_2: Trigger configuration (deprecated)

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
                    "connected_account_id": connected_account_id,
                    "connected_auth_id": connected_auth_id,
                    "body_trigger_config_1": body_trigger_config_1,
                    "body_trigger_config_2": body_trigger_config_2,
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

        self.delete = to_raw_response_wrapper(
            trigger_instances.delete,
        )
        self.list_active = to_raw_response_wrapper(
            trigger_instances.list_active,
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

        self.delete = async_to_raw_response_wrapper(
            trigger_instances.delete,
        )
        self.list_active = async_to_raw_response_wrapper(
            trigger_instances.list_active,
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

        self.delete = to_streamed_response_wrapper(
            trigger_instances.delete,
        )
        self.list_active = to_streamed_response_wrapper(
            trigger_instances.list_active,
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

        self.delete = async_to_streamed_response_wrapper(
            trigger_instances.delete,
        )
        self.list_active = async_to_streamed_response_wrapper(
            trigger_instances.list_active,
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
