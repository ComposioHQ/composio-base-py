# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ....types.org.project import webhook_delete_params, webhook_update_params, webhook_retrieve_params
from ....types.org.project.webhook_delete_response import WebhookDeleteResponse
from ....types.org.project.webhook_update_response import WebhookUpdateResponse
from ....types.org.project.webhook_refresh_response import WebhookRefreshResponse
from ....types.org.project.webhook_retrieve_response import WebhookRetrieveResponse

__all__ = ["WebhookResource", "AsyncWebhookResource"]


class WebhookResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhookResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return WebhookResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return WebhookResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        type: Literal["trigger", "event"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookRetrieveResponse:
        """
        Get the webhook URL for a project

        Args:
          type: Type of the webhook

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/org/project/webhook",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, webhook_retrieve_params.WebhookRetrieveParams),
            ),
            cast_to=WebhookRetrieveResponse,
        )

    def update(
        self,
        *,
        type: Literal["trigger", "event"],
        webhook_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookUpdateResponse:
        """
        Args:
          type: Type of the webhook

          webhook_url: Webhook URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/org/project/webhook/update",
            body=maybe_transform(
                {
                    "type": type,
                    "webhook_url": webhook_url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookUpdateResponse,
        )

    def delete(
        self,
        *,
        type: Literal["trigger", "event"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookDeleteResponse:
        """
        Args:
          type: Type of the webhook

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/api/v3/org/project/webhook",
            body=maybe_transform({"type": type}, webhook_delete_params.WebhookDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    def refresh(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookRefreshResponse:
        return self._post(
            "/api/v3/org/project/webhook/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRefreshResponse,
        )


class AsyncWebhookResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhookResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncWebhookResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        type: Literal["trigger", "event"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookRetrieveResponse:
        """
        Get the webhook URL for a project

        Args:
          type: Type of the webhook

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/org/project/webhook",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, webhook_retrieve_params.WebhookRetrieveParams),
            ),
            cast_to=WebhookRetrieveResponse,
        )

    async def update(
        self,
        *,
        type: Literal["trigger", "event"],
        webhook_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookUpdateResponse:
        """
        Args:
          type: Type of the webhook

          webhook_url: Webhook URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/org/project/webhook/update",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "webhook_url": webhook_url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookUpdateResponse,
        )

    async def delete(
        self,
        *,
        type: Literal["trigger", "event"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookDeleteResponse:
        """
        Args:
          type: Type of the webhook

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/api/v3/org/project/webhook",
            body=await async_maybe_transform({"type": type}, webhook_delete_params.WebhookDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    async def refresh(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookRefreshResponse:
        return await self._post(
            "/api/v3/org/project/webhook/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRefreshResponse,
        )


class WebhookResourceWithRawResponse:
    def __init__(self, webhook: WebhookResource) -> None:
        self._webhook = webhook

        self.retrieve = to_raw_response_wrapper(
            webhook.retrieve,
        )
        self.update = to_raw_response_wrapper(
            webhook.update,
        )
        self.delete = to_raw_response_wrapper(
            webhook.delete,
        )
        self.refresh = to_raw_response_wrapper(
            webhook.refresh,
        )


class AsyncWebhookResourceWithRawResponse:
    def __init__(self, webhook: AsyncWebhookResource) -> None:
        self._webhook = webhook

        self.retrieve = async_to_raw_response_wrapper(
            webhook.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            webhook.update,
        )
        self.delete = async_to_raw_response_wrapper(
            webhook.delete,
        )
        self.refresh = async_to_raw_response_wrapper(
            webhook.refresh,
        )


class WebhookResourceWithStreamingResponse:
    def __init__(self, webhook: WebhookResource) -> None:
        self._webhook = webhook

        self.retrieve = to_streamed_response_wrapper(
            webhook.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            webhook.update,
        )
        self.delete = to_streamed_response_wrapper(
            webhook.delete,
        )
        self.refresh = to_streamed_response_wrapper(
            webhook.refresh,
        )


class AsyncWebhookResourceWithStreamingResponse:
    def __init__(self, webhook: AsyncWebhookResource) -> None:
        self._webhook = webhook

        self.retrieve = async_to_streamed_response_wrapper(
            webhook.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            webhook.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhook.delete,
        )
        self.refresh = async_to_streamed_response_wrapper(
            webhook.refresh,
        )
