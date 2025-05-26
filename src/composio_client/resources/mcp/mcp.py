# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from .custom import (
    CustomResource,
    AsyncCustomResource,
    CustomResourceWithRawResponse,
    AsyncCustomResourceWithRawResponse,
    CustomResourceWithStreamingResponse,
    AsyncCustomResourceWithStreamingResponse,
)
from ...types import mcp_list_params, mcp_create_params, mcp_update_params, mcp_retrieve_app_params
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
from ...types.mcp_retrieve_app_response import McpRetrieveAppResponse

__all__ = ["McpResource", "AsyncMcpResource"]


class McpResource(SyncAPIResource):
    @cached_property
    def custom(self) -> CustomResource:
        return CustomResource(self._client)

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
        allowed_tools: List[str] | NotGiven = NOT_GIVEN,
        auth_config_id: str | NotGiven = NOT_GIVEN,
        ttl: Literal["1d", "3d", "1 month", "no expiration"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpCreateResponse:
        """
        Creates a new Model Control Protocol (MCP) server instance for the authenticated
        project. An MCP server provides a connection point for AI assistants to access
        your applications and services. The server is configured with specific
        authentication and tool permissions that determine what actions the connected
        assistants can perform.

        Args:
          name: Human-readable name to identify this MCP server instance (4-25 characters,
              alphanumeric and hyphens only)

          allowed_tools: List of tool slugs that should be allowed for this server. If not provided, all
              available tools for the authentication configuration will be enabled.

          auth_config_id: ID reference to an existing authentication configuration

          ttl: Time-to-live duration for this MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/mcp/servers",
            body=maybe_transform(
                {
                    "name": name,
                    "allowed_tools": allowed_tools,
                    "auth_config_id": auth_config_id,
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
        Retrieves detailed configuration information for a specific Model Control
        Protocol (MCP) server. The returned data includes connection details, associated
        applications, enabled tools, and authentication configuration.

        Args:
          id: Unique identifier of the MCP server to retrieve, update, or delete

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
        Updates the configuration of an existing Model Control Protocol (MCP) server.
        You can modify the server name, associated applications, and enabled tools. Only
        the fields included in the request will be updated.

        Args:
          id: Unique identifier of the MCP server to retrieve, update, or delete

          actions: List of action identifiers that should be enabled for this server

          apps: List of application identifiers this server should be configured to work with

          name: Human-readable name to identify this MCP server instance (4-25 characters,
              alphanumeric and hyphens only)

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
    ) -> McpListResponse:
        """
        Retrieves a paginated list of MCP servers associated with the authenticated
        project. Results can be filtered by name, toolkit, or authentication
        configuration ID. MCP servers are used to provide Model Control Protocol
        integration points for connecting AI assistants to your applications and
        services.

        Args:
          auth_config_id: Filter MCP servers by authentication configuration ID

          limit: Number of items per page (default: 10)

          name: Filter MCP servers by name (case-insensitive partial match)

          page_no: Page number for pagination (1-based)

          toolkit: Filter MCP servers by toolkit slug

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/mcp/servers",
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
        Performs a soft delete on a Model Control Protocol (MCP) server, making it
        unavailable for future use. This operation is reversible in the database but
        cannot be undone through the API. Any applications or services connected to this
        server will lose access after deletion.

        Args:
          id: Unique identifier of the MCP server to retrieve, update, or delete

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
        Retrieves a paginated list of Model Control Protocol (MCP) servers that are
        configured for a specific application or toolkit. This endpoint allows you to
        find all MCP server instances that have access to a particular application, such
        as GitHub, Slack, or Jira.

        Args:
          app_key: Toolkit or application slug identifier to filter MCP servers by

          auth_config_id: Filter MCP servers by authentication configuration ID

          limit: Number of items per page (default: 10)

          name: Filter MCP servers by name (case-insensitive partial match)

          page_no: Page number for pagination (1-based)

          toolkit: Filter MCP servers by toolkit slug

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


class AsyncMcpResource(AsyncAPIResource):
    @cached_property
    def custom(self) -> AsyncCustomResource:
        return AsyncCustomResource(self._client)

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
        allowed_tools: List[str] | NotGiven = NOT_GIVEN,
        auth_config_id: str | NotGiven = NOT_GIVEN,
        ttl: Literal["1d", "3d", "1 month", "no expiration"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpCreateResponse:
        """
        Creates a new Model Control Protocol (MCP) server instance for the authenticated
        project. An MCP server provides a connection point for AI assistants to access
        your applications and services. The server is configured with specific
        authentication and tool permissions that determine what actions the connected
        assistants can perform.

        Args:
          name: Human-readable name to identify this MCP server instance (4-25 characters,
              alphanumeric and hyphens only)

          allowed_tools: List of tool slugs that should be allowed for this server. If not provided, all
              available tools for the authentication configuration will be enabled.

          auth_config_id: ID reference to an existing authentication configuration

          ttl: Time-to-live duration for this MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/mcp/servers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "allowed_tools": allowed_tools,
                    "auth_config_id": auth_config_id,
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
        Retrieves detailed configuration information for a specific Model Control
        Protocol (MCP) server. The returned data includes connection details, associated
        applications, enabled tools, and authentication configuration.

        Args:
          id: Unique identifier of the MCP server to retrieve, update, or delete

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
        Updates the configuration of an existing Model Control Protocol (MCP) server.
        You can modify the server name, associated applications, and enabled tools. Only
        the fields included in the request will be updated.

        Args:
          id: Unique identifier of the MCP server to retrieve, update, or delete

          actions: List of action identifiers that should be enabled for this server

          apps: List of application identifiers this server should be configured to work with

          name: Human-readable name to identify this MCP server instance (4-25 characters,
              alphanumeric and hyphens only)

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
    ) -> McpListResponse:
        """
        Retrieves a paginated list of MCP servers associated with the authenticated
        project. Results can be filtered by name, toolkit, or authentication
        configuration ID. MCP servers are used to provide Model Control Protocol
        integration points for connecting AI assistants to your applications and
        services.

        Args:
          auth_config_id: Filter MCP servers by authentication configuration ID

          limit: Number of items per page (default: 10)

          name: Filter MCP servers by name (case-insensitive partial match)

          page_no: Page number for pagination (1-based)

          toolkit: Filter MCP servers by toolkit slug

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/mcp/servers",
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
        Performs a soft delete on a Model Control Protocol (MCP) server, making it
        unavailable for future use. This operation is reversible in the database but
        cannot be undone through the API. Any applications or services connected to this
        server will lose access after deletion.

        Args:
          id: Unique identifier of the MCP server to retrieve, update, or delete

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
        Retrieves a paginated list of Model Control Protocol (MCP) servers that are
        configured for a specific application or toolkit. This endpoint allows you to
        find all MCP server instances that have access to a particular application, such
        as GitHub, Slack, or Jira.

        Args:
          app_key: Toolkit or application slug identifier to filter MCP servers by

          auth_config_id: Filter MCP servers by authentication configuration ID

          limit: Number of items per page (default: 10)

          name: Filter MCP servers by name (case-insensitive partial match)

          page_no: Page number for pagination (1-based)

          toolkit: Filter MCP servers by toolkit slug

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

    @cached_property
    def custom(self) -> CustomResourceWithRawResponse:
        return CustomResourceWithRawResponse(self._mcp.custom)


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

    @cached_property
    def custom(self) -> AsyncCustomResourceWithRawResponse:
        return AsyncCustomResourceWithRawResponse(self._mcp.custom)


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

    @cached_property
    def custom(self) -> CustomResourceWithStreamingResponse:
        return CustomResourceWithStreamingResponse(self._mcp.custom)


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

    @cached_property
    def custom(self) -> AsyncCustomResourceWithStreamingResponse:
        return AsyncCustomResourceWithStreamingResponse(self._mcp.custom)
