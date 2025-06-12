# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v3 import admin_list_connections_params, admin_refresh_auth_tokens_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v3.admin_list_connections_response import AdminListConnectionsResponse
from ...types.v3.admin_refresh_auth_tokens_response import AdminRefreshAuthTokensResponse

__all__ = ["AdminResource", "AsyncAdminResource"]


class AdminResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AdminResourceWithStreamingResponse(self)

    def list_connections(
        self,
        *,
        toolkit_slug: str,
        x_composio_admin_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminListConnectionsResponse:
        """
        Administrative endpoint that retrieves all active connections for a given
        toolkit slug. This is primarily used for token refresh operations and system
        maintenance. Only includes non-deleted connections with OAuth2 or JWT
        authentication types.

        Args:
          toolkit_slug: The unique identifier slug of the toolkit to filter connections by

          x_composio_admin_token: Admin authentication token required for administrative operations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-composio-admin-token": x_composio_admin_token, **(extra_headers or {})}
        return self._get(
            "/api/v3/admin/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"toolkit_slug": toolkit_slug}, admin_list_connections_params.AdminListConnectionsParams
                ),
            ),
            cast_to=AdminListConnectionsResponse,
        )

    def refresh_auth_tokens(
        self,
        *,
        connection_ids: List[str],
        x_composio_admin_token: str,
        parallelism: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminRefreshAuthTokensResponse:
        """
        Administrative endpoint that refreshes authentication tokens for multiple
        connected accounts in parallel. This is useful for proactive token refresh to
        prevent authentication failures or for recovering from authentication issues
        across multiple connections.

        Args:
          connection_ids: List of connection identifiers that need token refresh

          x_composio_admin_token: Admin authentication token required for administrative operations

          parallelism: Controls processing speed and system load. Higher values process faster but
              increase load.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-composio-admin-token": x_composio_admin_token, **(extra_headers or {})}
        return self._post(
            "/api/v3/admin/auth-refresh",
            body=maybe_transform(
                {
                    "connection_ids": connection_ids,
                    "parallelism": parallelism,
                },
                admin_refresh_auth_tokens_params.AdminRefreshAuthTokensParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminRefreshAuthTokensResponse,
        )


class AsyncAdminResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncAdminResourceWithStreamingResponse(self)

    async def list_connections(
        self,
        *,
        toolkit_slug: str,
        x_composio_admin_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminListConnectionsResponse:
        """
        Administrative endpoint that retrieves all active connections for a given
        toolkit slug. This is primarily used for token refresh operations and system
        maintenance. Only includes non-deleted connections with OAuth2 or JWT
        authentication types.

        Args:
          toolkit_slug: The unique identifier slug of the toolkit to filter connections by

          x_composio_admin_token: Admin authentication token required for administrative operations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-composio-admin-token": x_composio_admin_token, **(extra_headers or {})}
        return await self._get(
            "/api/v3/admin/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"toolkit_slug": toolkit_slug}, admin_list_connections_params.AdminListConnectionsParams
                ),
            ),
            cast_to=AdminListConnectionsResponse,
        )

    async def refresh_auth_tokens(
        self,
        *,
        connection_ids: List[str],
        x_composio_admin_token: str,
        parallelism: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminRefreshAuthTokensResponse:
        """
        Administrative endpoint that refreshes authentication tokens for multiple
        connected accounts in parallel. This is useful for proactive token refresh to
        prevent authentication failures or for recovering from authentication issues
        across multiple connections.

        Args:
          connection_ids: List of connection identifiers that need token refresh

          x_composio_admin_token: Admin authentication token required for administrative operations

          parallelism: Controls processing speed and system load. Higher values process faster but
              increase load.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-composio-admin-token": x_composio_admin_token, **(extra_headers or {})}
        return await self._post(
            "/api/v3/admin/auth-refresh",
            body=await async_maybe_transform(
                {
                    "connection_ids": connection_ids,
                    "parallelism": parallelism,
                },
                admin_refresh_auth_tokens_params.AdminRefreshAuthTokensParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminRefreshAuthTokensResponse,
        )


class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.list_connections = to_raw_response_wrapper(
            admin.list_connections,
        )
        self.refresh_auth_tokens = to_raw_response_wrapper(
            admin.refresh_auth_tokens,
        )


class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.list_connections = async_to_raw_response_wrapper(
            admin.list_connections,
        )
        self.refresh_auth_tokens = async_to_raw_response_wrapper(
            admin.refresh_auth_tokens,
        )


class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.list_connections = to_streamed_response_wrapper(
            admin.list_connections,
        )
        self.refresh_auth_tokens = to_streamed_response_wrapper(
            admin.refresh_auth_tokens,
        )


class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.list_connections = async_to_streamed_response_wrapper(
            admin.list_connections,
        )
        self.refresh_auth_tokens = async_to_streamed_response_wrapper(
            admin.refresh_auth_tokens,
        )
