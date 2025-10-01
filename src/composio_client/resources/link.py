# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import link_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.link_create_response import LinkCreateResponse

__all__ = ["LinkResource", "AsyncLinkResource"]


class LinkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return LinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return LinkResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        auth_config_id: str,
        user_id: str,
        callback_url: str | Omit = omit,
        connection_data: link_create_params.ConnectionData | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkCreateResponse:
        """
        Creates a new authentication link session that users can use to connect their
        accounts

        Args:
          auth_config_id: The auth config id to create a link for

          user_id: The user id to create a link for

          callback_url: The callback url to create a link for

          connection_data: Optional data to pre-fill connection fields with default values

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/connected_accounts/link",
            body=maybe_transform(
                {
                    "auth_config_id": auth_config_id,
                    "user_id": user_id,
                    "callback_url": callback_url,
                    "connection_data": connection_data,
                },
                link_create_params.LinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkCreateResponse,
        )


class AsyncLinkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncLinkResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        auth_config_id: str,
        user_id: str,
        callback_url: str | Omit = omit,
        connection_data: link_create_params.ConnectionData | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkCreateResponse:
        """
        Creates a new authentication link session that users can use to connect their
        accounts

        Args:
          auth_config_id: The auth config id to create a link for

          user_id: The user id to create a link for

          callback_url: The callback url to create a link for

          connection_data: Optional data to pre-fill connection fields with default values

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/connected_accounts/link",
            body=await async_maybe_transform(
                {
                    "auth_config_id": auth_config_id,
                    "user_id": user_id,
                    "callback_url": callback_url,
                    "connection_data": connection_data,
                },
                link_create_params.LinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkCreateResponse,
        )


class LinkResourceWithRawResponse:
    def __init__(self, link: LinkResource) -> None:
        self._link = link

        self.create = to_raw_response_wrapper(
            link.create,
        )


class AsyncLinkResourceWithRawResponse:
    def __init__(self, link: AsyncLinkResource) -> None:
        self._link = link

        self.create = async_to_raw_response_wrapper(
            link.create,
        )


class LinkResourceWithStreamingResponse:
    def __init__(self, link: LinkResource) -> None:
        self._link = link

        self.create = to_streamed_response_wrapper(
            link.create,
        )


class AsyncLinkResourceWithStreamingResponse:
    def __init__(self, link: AsyncLinkResource) -> None:
        self._link = link

        self.create = async_to_streamed_response_wrapper(
            link.create,
        )
