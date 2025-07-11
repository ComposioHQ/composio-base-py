# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    connected_account_list_params,
    connected_account_create_params,
    connected_account_refresh_params,
    connected_account_update_status_params,
)
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
from ..types.connected_account_list_response import ConnectedAccountListResponse
from ..types.connected_account_create_response import ConnectedAccountCreateResponse
from ..types.connected_account_delete_response import ConnectedAccountDeleteResponse
from ..types.connected_account_refresh_response import ConnectedAccountRefreshResponse
from ..types.connected_account_retrieve_response import ConnectedAccountRetrieveResponse
from ..types.connected_account_update_status_response import ConnectedAccountUpdateStatusResponse

__all__ = ["ConnectedAccountsResource", "AsyncConnectedAccountsResource"]


class ConnectedAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectedAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return ConnectedAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectedAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return ConnectedAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        auth_config: connected_account_create_params.AuthConfig,
        connection: connected_account_create_params.Connection,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountCreateResponse:
        """
        Create a new connected account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/connected_accounts",
            body=maybe_transform(
                {
                    "auth_config": auth_config,
                    "connection": connection,
                },
                connected_account_create_params.ConnectedAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccountCreateResponse,
        )

    def retrieve(
        self,
        nanoid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountRetrieveResponse:
        """
        Retrieves comprehensive details of a connected account, including authentication
        configuration, connection status, and all parameters needed for API requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return self._get(
            f"/api/v3/connected_accounts/{nanoid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccountRetrieveResponse,
        )

    def list(
        self,
        *,
        auth_config_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        labels: Optional[List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        order_by: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        statuses: Optional[List[Literal["INITIALIZING", "INITIATED", "ACTIVE", "FAILED", "EXPIRED", "INACTIVE"]]]
        | NotGiven = NOT_GIVEN,
        toolkit_slugs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        user_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountListResponse:
        """
        List connected accounts with optional filters

        Args:
          auth_config_ids: The auth config ids of the connected accounts

          cursor: The cursor to paginate through the connected accounts

          labels: The labels of the connected accounts

          limit: The limit of the connected accounts to return

          order_by: The order by of the connected accounts

          statuses: The status of the connected account

          toolkit_slugs: The toolkit slugs of the connected accounts

          user_ids: The user ids of the connected accounts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/connected_accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "auth_config_ids": auth_config_ids,
                        "cursor": cursor,
                        "labels": labels,
                        "limit": limit,
                        "order_by": order_by,
                        "statuses": statuses,
                        "toolkit_slugs": toolkit_slugs,
                        "user_ids": user_ids,
                    },
                    connected_account_list_params.ConnectedAccountListParams,
                ),
            ),
            cast_to=ConnectedAccountListResponse,
        )

    def delete(
        self,
        nanoid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountDeleteResponse:
        """Soft-deletes a connected account by marking it as deleted in the database.

        This
        prevents the account from being used for API calls but preserves the record for
        audit purposes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return self._delete(
            f"/api/v3/connected_accounts/{nanoid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccountDeleteResponse,
        )

    def refresh(
        self,
        nanoid: str,
        *,
        query_redirect_url: str | NotGiven = NOT_GIVEN,
        body_redirect_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountRefreshResponse:
        """
        Initiates a new authentication flow for a connected account when credentials
        have expired or become invalid. This may generate a new authentication URL for
        OAuth flows or refresh tokens for other auth schemes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return self._post(
            f"/api/v3/connected_accounts/{nanoid}/refresh",
            body=maybe_transform(
                {"body_redirect_url": body_redirect_url}, connected_account_refresh_params.ConnectedAccountRefreshParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"query_redirect_url": query_redirect_url},
                    connected_account_refresh_params.ConnectedAccountRefreshParams,
                ),
            ),
            cast_to=ConnectedAccountRefreshResponse,
        )

    def update_status(
        self,
        nano_id: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountUpdateStatusResponse:
        """
        Updates the status of a connected account to either enabled (active) or disabled
        (inactive). Disabled accounts cannot be used for API calls but remain in the
        database.

        Args:
          enabled: Set to true to enable the account or false to disable it

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nano_id:
            raise ValueError(f"Expected a non-empty value for `nano_id` but received {nano_id!r}")
        return self._patch(
            f"/api/v3/connected_accounts/{nano_id}/status",
            body=maybe_transform(
                {"enabled": enabled}, connected_account_update_status_params.ConnectedAccountUpdateStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccountUpdateStatusResponse,
        )


class AsyncConnectedAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectedAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectedAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectedAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncConnectedAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        auth_config: connected_account_create_params.AuthConfig,
        connection: connected_account_create_params.Connection,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountCreateResponse:
        """
        Create a new connected account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/connected_accounts",
            body=await async_maybe_transform(
                {
                    "auth_config": auth_config,
                    "connection": connection,
                },
                connected_account_create_params.ConnectedAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccountCreateResponse,
        )

    async def retrieve(
        self,
        nanoid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountRetrieveResponse:
        """
        Retrieves comprehensive details of a connected account, including authentication
        configuration, connection status, and all parameters needed for API requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return await self._get(
            f"/api/v3/connected_accounts/{nanoid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccountRetrieveResponse,
        )

    async def list(
        self,
        *,
        auth_config_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        labels: Optional[List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        order_by: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        statuses: Optional[List[Literal["INITIALIZING", "INITIATED", "ACTIVE", "FAILED", "EXPIRED", "INACTIVE"]]]
        | NotGiven = NOT_GIVEN,
        toolkit_slugs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        user_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountListResponse:
        """
        List connected accounts with optional filters

        Args:
          auth_config_ids: The auth config ids of the connected accounts

          cursor: The cursor to paginate through the connected accounts

          labels: The labels of the connected accounts

          limit: The limit of the connected accounts to return

          order_by: The order by of the connected accounts

          statuses: The status of the connected account

          toolkit_slugs: The toolkit slugs of the connected accounts

          user_ids: The user ids of the connected accounts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/connected_accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "auth_config_ids": auth_config_ids,
                        "cursor": cursor,
                        "labels": labels,
                        "limit": limit,
                        "order_by": order_by,
                        "statuses": statuses,
                        "toolkit_slugs": toolkit_slugs,
                        "user_ids": user_ids,
                    },
                    connected_account_list_params.ConnectedAccountListParams,
                ),
            ),
            cast_to=ConnectedAccountListResponse,
        )

    async def delete(
        self,
        nanoid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountDeleteResponse:
        """Soft-deletes a connected account by marking it as deleted in the database.

        This
        prevents the account from being used for API calls but preserves the record for
        audit purposes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return await self._delete(
            f"/api/v3/connected_accounts/{nanoid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccountDeleteResponse,
        )

    async def refresh(
        self,
        nanoid: str,
        *,
        query_redirect_url: str | NotGiven = NOT_GIVEN,
        body_redirect_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountRefreshResponse:
        """
        Initiates a new authentication flow for a connected account when credentials
        have expired or become invalid. This may generate a new authentication URL for
        OAuth flows or refresh tokens for other auth schemes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return await self._post(
            f"/api/v3/connected_accounts/{nanoid}/refresh",
            body=await async_maybe_transform(
                {"body_redirect_url": body_redirect_url}, connected_account_refresh_params.ConnectedAccountRefreshParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_redirect_url": query_redirect_url},
                    connected_account_refresh_params.ConnectedAccountRefreshParams,
                ),
            ),
            cast_to=ConnectedAccountRefreshResponse,
        )

    async def update_status(
        self,
        nano_id: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountUpdateStatusResponse:
        """
        Updates the status of a connected account to either enabled (active) or disabled
        (inactive). Disabled accounts cannot be used for API calls but remain in the
        database.

        Args:
          enabled: Set to true to enable the account or false to disable it

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nano_id:
            raise ValueError(f"Expected a non-empty value for `nano_id` but received {nano_id!r}")
        return await self._patch(
            f"/api/v3/connected_accounts/{nano_id}/status",
            body=await async_maybe_transform(
                {"enabled": enabled}, connected_account_update_status_params.ConnectedAccountUpdateStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccountUpdateStatusResponse,
        )


class ConnectedAccountsResourceWithRawResponse:
    def __init__(self, connected_accounts: ConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.create = to_raw_response_wrapper(
            connected_accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            connected_accounts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            connected_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            connected_accounts.delete,
        )
        self.refresh = to_raw_response_wrapper(
            connected_accounts.refresh,
        )
        self.update_status = to_raw_response_wrapper(
            connected_accounts.update_status,
        )


class AsyncConnectedAccountsResourceWithRawResponse:
    def __init__(self, connected_accounts: AsyncConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.create = async_to_raw_response_wrapper(
            connected_accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            connected_accounts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            connected_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connected_accounts.delete,
        )
        self.refresh = async_to_raw_response_wrapper(
            connected_accounts.refresh,
        )
        self.update_status = async_to_raw_response_wrapper(
            connected_accounts.update_status,
        )


class ConnectedAccountsResourceWithStreamingResponse:
    def __init__(self, connected_accounts: ConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.create = to_streamed_response_wrapper(
            connected_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            connected_accounts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            connected_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            connected_accounts.delete,
        )
        self.refresh = to_streamed_response_wrapper(
            connected_accounts.refresh,
        )
        self.update_status = to_streamed_response_wrapper(
            connected_accounts.update_status,
        )


class AsyncConnectedAccountsResourceWithStreamingResponse:
    def __init__(self, connected_accounts: AsyncConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.create = async_to_streamed_response_wrapper(
            connected_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connected_accounts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            connected_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connected_accounts.delete,
        )
        self.refresh = async_to_streamed_response_wrapper(
            connected_accounts.refresh,
        )
        self.update_status = async_to_streamed_response_wrapper(
            connected_accounts.update_status,
        )
