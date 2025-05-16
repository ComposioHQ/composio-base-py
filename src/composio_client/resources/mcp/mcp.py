# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ...types import mcp_update_params, mcp_retrieve_app_params
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
from ...types.mcp_delete_response import McpDeleteResponse
from ...types.mcp_update_response import McpUpdateResponse
from ...types.mcp_retrieve_response import McpRetrieveResponse
from ...types.mcp_validate_response import McpValidateResponse
from ...types.mcp_retrieve_app_response import McpRetrieveAppResponse

__all__ = ["McpResource", "AsyncMcpResource"]


class McpResource(SyncAPIResource):
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
        auth_config_id: str | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page_no: Optional[float] | NotGiven = NOT_GIVEN,
        toolkit: str | NotGiven = NOT_GIVEN,
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

          auth_config_id: Auth configuration ID to filter by

          limit: Number of items per page

          name: Name of the MCP server to filter by

          page_no: Page number for pagination

          toolkit: Toolkit slug to filter by

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "auth_config_id": auth_config_id,
                        "limit": limit,
                        "name": name,
                        "page_no": page_no,
                        "toolkit": toolkit,
                    },
                    mcp_retrieve_app_params.McpRetrieveAppParams,
                ),
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
        auth_config_id: str | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page_no: Optional[float] | NotGiven = NOT_GIVEN,
        toolkit: str | NotGiven = NOT_GIVEN,
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

          auth_config_id: Auth configuration ID to filter by

          limit: Number of items per page

          name: Name of the MCP server to filter by

          page_no: Page number for pagination

          toolkit: Toolkit slug to filter by

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "auth_config_id": auth_config_id,
                        "limit": limit,
                        "name": name,
                        "page_no": page_no,
                        "toolkit": toolkit,
                    },
                    mcp_retrieve_app_params.McpRetrieveAppParams,
                ),
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

        self.retrieve = to_raw_response_wrapper(
            mcp.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mcp.update,
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


class AsyncMcpResourceWithRawResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.retrieve = async_to_raw_response_wrapper(
            mcp.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mcp.update,
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


class McpResourceWithStreamingResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.retrieve = to_streamed_response_wrapper(
            mcp.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mcp.update,
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


class AsyncMcpResourceWithStreamingResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.retrieve = async_to_streamed_response_wrapper(
            mcp.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mcp.update,
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
