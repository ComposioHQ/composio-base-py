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
from ...types.org.api_key_retrieve_response import APIKeyRetrieveResponse
from ...types.org.api_key_regenerate_response import APIKeyRegenerateResponse

__all__ = ["APIKeyResource", "AsyncAPIKeyResource"]


class APIKeyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return APIKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return APIKeyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIKeyRetrieveResponse:
        """Retrieve the API key for the current organization.

        This endpoint is restricted
        to organization administrators only. The returned API key can be used for
        authenticating organization-level API requests.
        """
        return self._get(
            "/api/v3/org/api_key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyRetrieveResponse,
        )

    def regenerate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIKeyRegenerateResponse:
        """
        Generate a new API key for the organization, invalidating the previous one
        (admin only). This operation cannot be undone and will immediately invalidate
        the previous API key.
        """
        return self._post(
            "/api/v3/org/api_key/regenerate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyRegenerateResponse,
        )


class AsyncAPIKeyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncAPIKeyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIKeyRetrieveResponse:
        """Retrieve the API key for the current organization.

        This endpoint is restricted
        to organization administrators only. The returned API key can be used for
        authenticating organization-level API requests.
        """
        return await self._get(
            "/api/v3/org/api_key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyRetrieveResponse,
        )

    async def regenerate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIKeyRegenerateResponse:
        """
        Generate a new API key for the organization, invalidating the previous one
        (admin only). This operation cannot be undone and will immediately invalidate
        the previous API key.
        """
        return await self._post(
            "/api/v3/org/api_key/regenerate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyRegenerateResponse,
        )


class APIKeyResourceWithRawResponse:
    def __init__(self, api_key: APIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = to_raw_response_wrapper(
            api_key.retrieve,
        )
        self.regenerate = to_raw_response_wrapper(
            api_key.regenerate,
        )


class AsyncAPIKeyResourceWithRawResponse:
    def __init__(self, api_key: AsyncAPIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = async_to_raw_response_wrapper(
            api_key.retrieve,
        )
        self.regenerate = async_to_raw_response_wrapper(
            api_key.regenerate,
        )


class APIKeyResourceWithStreamingResponse:
    def __init__(self, api_key: APIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = to_streamed_response_wrapper(
            api_key.retrieve,
        )
        self.regenerate = to_streamed_response_wrapper(
            api_key.regenerate,
        )


class AsyncAPIKeyResourceWithStreamingResponse:
    def __init__(self, api_key: AsyncAPIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = async_to_streamed_response_wrapper(
            api_key.retrieve,
        )
        self.regenerate = async_to_streamed_response_wrapper(
            api_key.regenerate,
        )
