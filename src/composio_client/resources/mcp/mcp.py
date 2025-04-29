# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

from ...types import mcp_list_params, mcp_create_params, mcp_update_params
from .command import (
    CommandResource,
    AsyncCommandResource,
    CommandResourceWithRawResponse,
    AsyncCommandResourceWithRawResponse,
    CommandResourceWithStreamingResponse,
    AsyncCommandResourceWithStreamingResponse,
)
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
from ...types.mcp_list_response import McpListResponse
from ...types.mcp_create_response import McpCreateResponse
from ...types.mcp_delete_response import McpDeleteResponse
from ...types.mcp_update_response import McpUpdateResponse
from ...types.mcp_retrieve_response import McpRetrieveResponse
from ...types.mcp_validate_response import McpValidateResponse
from ...types.mcp_retrieve_app_response import McpRetrieveAppResponse

__all__ = ["McpResource", "AsyncMcpResource"]


class McpResource(SyncAPIResource):
    @cached_property
    def command(self) -> CommandResource:
        return CommandResource(self._client)

    @cached_property
    def with_raw_response(self) -> McpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return McpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return McpResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        actions: List[str] | NotGiven = NOT_GIVEN,
        apps: List[str] | NotGiven = NOT_GIVEN,
        auth_configs: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        connected_account_ids: List[str] | NotGiven = NOT_GIVEN,
        custom_auth_headers: bool | NotGiven = NOT_GIVEN,
        entity_ids: List[str] | NotGiven = NOT_GIVEN,
        ttl: Literal["1d", "3d", "1 month", "no expiration"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpCreateResponse:
        """
        Create a new MCP server

        Args:
          name: Name of the MCP server

          actions: Actions available for the server

          apps: App IDs associated with the server

          auth_configs: Auth configurations

          connected_account_ids: Connected account IDs

          custom_auth_headers: Whether to use custom auth headers

          entity_ids: Entity IDs

          ttl: Time to live for the server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/mcp/create",
            body=maybe_transform(
                {
                    "name": name,
                    "actions": actions,
                    "apps": apps,
                    "auth_configs": auth_configs,
                    "connected_account_ids": connected_account_ids,
                    "custom_auth_headers": custom_auth_headers,
                    "entity_ids": entity_ids,
                    "ttl": ttl,
                },
                mcp_create_params.McpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpRetrieveResponse:
        """
        Get MCP server details by ID

        Args:
          id: The ID of the MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v3/mcp/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        actions: List[str] | NotGiven = NOT_GIVEN,
        apps: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpUpdateResponse:
        """
        Update MCP server configuration

        Args:
          id: The ID of the MCP server

          actions: Actions available for the server

          apps: App IDs associated with the server

          name: Name of the MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/v3/mcp/{id}",
            body=maybe_transform(
                {
                    "actions": actions,
                    "apps": apps,
                    "name": name,
                },
                mcp_update_params.McpUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpUpdateResponse,
        )

    def list(
        self,
        *,
        app_id: List[str] | NotGiven = NOT_GIVEN,
        connected_account_id: List[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[float] | NotGiven = NOT_GIVEN,
        entity_id: List[str] | NotGiven = NOT_GIVEN,
        integration_id: str | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpListResponse:
        """
        List MCP servers with optional filters

        Args:
          app_id: App IDs to filter by

          connected_account_id: Connected account IDs to filter by

          cursor: Cursor for pagination

          entity_id: Entity IDs to filter by

          integration_id: Integration ID to filter by

          limit: Limit for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/mcp/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id": app_id,
                        "connected_account_id": connected_account_id,
                        "cursor": cursor,
                        "entity_id": entity_id,
                        "integration_id": integration_id,
                        "limit": limit,
                    },
                    mcp_list_params.McpListParams,
                ),
            ),
            cast_to=McpListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpDeleteResponse:
        """
        Delete an MCP server

        Args:
          id: The ID of the MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v3/mcp/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpDeleteResponse,
        )

    def retrieve_app(
        self,
        app_key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpRetrieveAppResponse:
        """
        List MCP servers for a specific app

        Args:
          app_key: The key of the app to find MCP servers for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_key:
            raise ValueError(f"Expected a non-empty value for `app_key` but received {app_key!r}")
        return self._get(
            f"/api/v3/mcp/app/{app_key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpRetrieveAppResponse,
        )

    def validate(
        self,
        uuid: str,
        *,
        x_composio_admin_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpValidateResponse:
        """
        Validate MCP server and retrieve connection details

        Args:
          uuid: UUID of the MCP server to validate

          x_composio_admin_token: Admin token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        extra_headers = {"x-composio-admin-token": x_composio_admin_token, **(extra_headers or {})}
        return self._get(
            f"/api/v3/mcp/validate/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpValidateResponse,
        )


class AsyncMcpResource(AsyncAPIResource):
    @cached_property
    def command(self) -> AsyncCommandResource:
        return AsyncCommandResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMcpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncMcpResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        actions: List[str] | NotGiven = NOT_GIVEN,
        apps: List[str] | NotGiven = NOT_GIVEN,
        auth_configs: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        connected_account_ids: List[str] | NotGiven = NOT_GIVEN,
        custom_auth_headers: bool | NotGiven = NOT_GIVEN,
        entity_ids: List[str] | NotGiven = NOT_GIVEN,
        ttl: Literal["1d", "3d", "1 month", "no expiration"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpCreateResponse:
        """
        Create a new MCP server

        Args:
          name: Name of the MCP server

          actions: Actions available for the server

          apps: App IDs associated with the server

          auth_configs: Auth configurations

          connected_account_ids: Connected account IDs

          custom_auth_headers: Whether to use custom auth headers

          entity_ids: Entity IDs

          ttl: Time to live for the server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/mcp/create",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "actions": actions,
                    "apps": apps,
                    "auth_configs": auth_configs,
                    "connected_account_ids": connected_account_ids,
                    "custom_auth_headers": custom_auth_headers,
                    "entity_ids": entity_ids,
                    "ttl": ttl,
                },
                mcp_create_params.McpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpRetrieveResponse:
        """
        Get MCP server details by ID

        Args:
          id: The ID of the MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v3/mcp/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        actions: List[str] | NotGiven = NOT_GIVEN,
        apps: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpUpdateResponse:
        """
        Update MCP server configuration

        Args:
          id: The ID of the MCP server

          actions: Actions available for the server

          apps: App IDs associated with the server

          name: Name of the MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/v3/mcp/{id}",
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "apps": apps,
                    "name": name,
                },
                mcp_update_params.McpUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpUpdateResponse,
        )

    async def list(
        self,
        *,
        app_id: List[str] | NotGiven = NOT_GIVEN,
        connected_account_id: List[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[float] | NotGiven = NOT_GIVEN,
        entity_id: List[str] | NotGiven = NOT_GIVEN,
        integration_id: str | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpListResponse:
        """
        List MCP servers with optional filters

        Args:
          app_id: App IDs to filter by

          connected_account_id: Connected account IDs to filter by

          cursor: Cursor for pagination

          entity_id: Entity IDs to filter by

          integration_id: Integration ID to filter by

          limit: Limit for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/mcp/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "app_id": app_id,
                        "connected_account_id": connected_account_id,
                        "cursor": cursor,
                        "entity_id": entity_id,
                        "integration_id": integration_id,
                        "limit": limit,
                    },
                    mcp_list_params.McpListParams,
                ),
            ),
            cast_to=McpListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpDeleteResponse:
        """
        Delete an MCP server

        Args:
          id: The ID of the MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v3/mcp/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpDeleteResponse,
        )

    async def retrieve_app(
        self,
        app_key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpRetrieveAppResponse:
        """
        List MCP servers for a specific app

        Args:
          app_key: The key of the app to find MCP servers for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_key:
            raise ValueError(f"Expected a non-empty value for `app_key` but received {app_key!r}")
        return await self._get(
            f"/api/v3/mcp/app/{app_key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpRetrieveAppResponse,
        )

    async def validate(
        self,
        uuid: str,
        *,
        x_composio_admin_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpValidateResponse:
        """
        Validate MCP server and retrieve connection details

        Args:
          uuid: UUID of the MCP server to validate

          x_composio_admin_token: Admin token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        extra_headers = {"x-composio-admin-token": x_composio_admin_token, **(extra_headers or {})}
        return await self._get(
            f"/api/v3/mcp/validate/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpValidateResponse,
        )


class McpResourceWithRawResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.create = to_raw_response_wrapper(
            mcp.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mcp.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mcp.update,
        )
        self.list = to_raw_response_wrapper(
            mcp.list,
        )
        self.delete = to_raw_response_wrapper(
            mcp.delete,
        )
        self.retrieve_app = to_raw_response_wrapper(
            mcp.retrieve_app,
        )
        self.validate = to_raw_response_wrapper(
            mcp.validate,
        )

    @cached_property
    def command(self) -> CommandResourceWithRawResponse:
        return CommandResourceWithRawResponse(self._mcp.command)


class AsyncMcpResourceWithRawResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.create = async_to_raw_response_wrapper(
            mcp.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mcp.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mcp.update,
        )
        self.list = async_to_raw_response_wrapper(
            mcp.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mcp.delete,
        )
        self.retrieve_app = async_to_raw_response_wrapper(
            mcp.retrieve_app,
        )
        self.validate = async_to_raw_response_wrapper(
            mcp.validate,
        )

    @cached_property
    def command(self) -> AsyncCommandResourceWithRawResponse:
        return AsyncCommandResourceWithRawResponse(self._mcp.command)


class McpResourceWithStreamingResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.create = to_streamed_response_wrapper(
            mcp.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mcp.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mcp.update,
        )
        self.list = to_streamed_response_wrapper(
            mcp.list,
        )
        self.delete = to_streamed_response_wrapper(
            mcp.delete,
        )
        self.retrieve_app = to_streamed_response_wrapper(
            mcp.retrieve_app,
        )
        self.validate = to_streamed_response_wrapper(
            mcp.validate,
        )

    @cached_property
    def command(self) -> CommandResourceWithStreamingResponse:
        return CommandResourceWithStreamingResponse(self._mcp.command)


class AsyncMcpResourceWithStreamingResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.create = async_to_streamed_response_wrapper(
            mcp.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mcp.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mcp.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mcp.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mcp.delete,
        )
        self.retrieve_app = async_to_streamed_response_wrapper(
            mcp.retrieve_app,
        )
        self.validate = async_to_streamed_response_wrapper(
            mcp.validate,
        )

    @cached_property
    def command(self) -> AsyncCommandResourceWithStreamingResponse:
        return AsyncCommandResourceWithStreamingResponse(self._mcp.command)
