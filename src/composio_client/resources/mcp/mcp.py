# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ...types import mcp_retrieve_app_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.mcp_retrieve_response import McpRetrieveResponse
from ...types.mcp_validate_response import McpValidateResponse
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

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def retrieve_app(
        self,
        app_key: str,
        *,
        auth_config_ids: str | Omit = omit,
        limit: Optional[float] | Omit = omit,
        name: str | Omit = omit,
        order_by: Literal["created_at", "updated_at"] | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        page_no: Optional[float] | Omit = omit,
        toolkits: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpRetrieveAppResponse:
        """
        Retrieves a paginated list of Model Control Protocol (MCP) servers that are
        configured for a specific application or toolkit. This endpoint allows you to
        find all MCP server instances that have access to a particular application, such
        as GitHub, Slack, or Jira.

        Args:
          app_key: Toolkit or application slug identifier to filter MCP servers by

          auth_config_ids: Comma-separated list of auth config IDs to filter servers by

          limit: Number of items per page (default: 10)

          name: Filter MCP servers by name (case-insensitive partial match)

          order_by: Field to order results by

          order_direction: Direction of ordering

          page_no: Page number for pagination (1-based)

          toolkits: Comma-separated list of toolkit slugs to filter servers by

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
                        "auth_config_ids": auth_config_ids,
                        "limit": limit,
                        "name": name,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "page_no": page_no,
                        "toolkits": toolkits,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpValidateResponse:
        """
        Admin-only endpoint that validates a Model Control Protocol (MCP) server and
        retrieves its complete configuration details, including authentication
        information. This endpoint is typically used by the MCP service itself to
        authenticate and authorize connection requests from clients.

        Args:
          uuid: Unique identifier of the MCP server to validate and retrieve connection details
              for

          x_composio_admin_token: Administrative access token required for validating MCP servers

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

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    async def retrieve_app(
        self,
        app_key: str,
        *,
        auth_config_ids: str | Omit = omit,
        limit: Optional[float] | Omit = omit,
        name: str | Omit = omit,
        order_by: Literal["created_at", "updated_at"] | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        page_no: Optional[float] | Omit = omit,
        toolkits: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpRetrieveAppResponse:
        """
        Retrieves a paginated list of Model Control Protocol (MCP) servers that are
        configured for a specific application or toolkit. This endpoint allows you to
        find all MCP server instances that have access to a particular application, such
        as GitHub, Slack, or Jira.

        Args:
          app_key: Toolkit or application slug identifier to filter MCP servers by

          auth_config_ids: Comma-separated list of auth config IDs to filter servers by

          limit: Number of items per page (default: 10)

          name: Filter MCP servers by name (case-insensitive partial match)

          order_by: Field to order results by

          order_direction: Direction of ordering

          page_no: Page number for pagination (1-based)

          toolkits: Comma-separated list of toolkit slugs to filter servers by

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
                        "auth_config_ids": auth_config_ids,
                        "limit": limit,
                        "name": name,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "page_no": page_no,
                        "toolkits": toolkits,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpValidateResponse:
        """
        Admin-only endpoint that validates a Model Control Protocol (MCP) server and
        retrieves its complete configuration details, including authentication
        information. This endpoint is typically used by the MCP service itself to
        authenticate and authorize connection requests from clients.

        Args:
          uuid: Unique identifier of the MCP server to validate and retrieve connection details
              for

          x_composio_admin_token: Administrative access token required for validating MCP servers

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
        self.retrieve_app = to_raw_response_wrapper(
            mcp.retrieve_app,
        )
        self.validate = to_raw_response_wrapper(
            mcp.validate,
        )

    @cached_property
    def custom(self) -> CustomResourceWithRawResponse:
        return CustomResourceWithRawResponse(self._mcp.custom)


class AsyncMcpResourceWithRawResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.retrieve = async_to_raw_response_wrapper(
            mcp.retrieve,
        )
        self.retrieve_app = async_to_raw_response_wrapper(
            mcp.retrieve_app,
        )
        self.validate = async_to_raw_response_wrapper(
            mcp.validate,
        )

    @cached_property
    def custom(self) -> AsyncCustomResourceWithRawResponse:
        return AsyncCustomResourceWithRawResponse(self._mcp.custom)


class McpResourceWithStreamingResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.retrieve = to_streamed_response_wrapper(
            mcp.retrieve,
        )
        self.retrieve_app = to_streamed_response_wrapper(
            mcp.retrieve_app,
        )
        self.validate = to_streamed_response_wrapper(
            mcp.validate,
        )

    @cached_property
    def custom(self) -> CustomResourceWithStreamingResponse:
        return CustomResourceWithStreamingResponse(self._mcp.custom)


class AsyncMcpResourceWithStreamingResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.retrieve = async_to_streamed_response_wrapper(
            mcp.retrieve,
        )
        self.retrieve_app = async_to_streamed_response_wrapper(
            mcp.retrieve_app,
        )
        self.validate = async_to_streamed_response_wrapper(
            mcp.validate,
        )

    @cached_property
    def custom(self) -> AsyncCustomResourceWithStreamingResponse:
        return AsyncCustomResourceWithStreamingResponse(self._mcp.custom)
