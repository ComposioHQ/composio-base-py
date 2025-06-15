# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

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
from ...types.mcp import custom_create_params
from ..._base_client import make_request_options
from ...types.mcp.custom_create_response import CustomCreateResponse

__all__ = ["CustomResource", "AsyncCustomResource"]


class CustomResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return CustomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return CustomResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        toolkits: List[str],
        auth_config_ids: List[str] | NotGiven = NOT_GIVEN,
        custom_tools: List[str] | NotGiven = NOT_GIVEN,
        managed_auth_via_composio: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCreateResponse:
        """
        Creates a new Model Control Protocol (MCP) server instance that can integrate
        with multiple applications or toolkits simultaneously. This endpoint allows you
        to create a server that can access tools from different applications, making it
        suitable for complex workflows that span multiple services.

        Args:
          name: Human-readable name to identify this custom MCP server (4-30 characters,
              alphanumeric, spaces, and hyphens only)

          toolkits: List of application/toolkit identifiers to enable for this server

          auth_config_ids: ID references to existing authentication configurations

          custom_tools: Additional custom tool identifiers to enable that aren't part of standard
              toolkits

          managed_auth_via_composio: Whether to manage authentication via Composio

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/mcp/servers/custom",
            body=maybe_transform(
                {
                    "name": name,
                    "toolkits": toolkits,
                    "auth_config_ids": auth_config_ids,
                    "custom_tools": custom_tools,
                    "managed_auth_via_composio": managed_auth_via_composio,
                },
                custom_create_params.CustomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCreateResponse,
        )


class AsyncCustomResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncCustomResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        toolkits: List[str],
        auth_config_ids: List[str] | NotGiven = NOT_GIVEN,
        custom_tools: List[str] | NotGiven = NOT_GIVEN,
        managed_auth_via_composio: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCreateResponse:
        """
        Creates a new Model Control Protocol (MCP) server instance that can integrate
        with multiple applications or toolkits simultaneously. This endpoint allows you
        to create a server that can access tools from different applications, making it
        suitable for complex workflows that span multiple services.

        Args:
          name: Human-readable name to identify this custom MCP server (4-30 characters,
              alphanumeric, spaces, and hyphens only)

          toolkits: List of application/toolkit identifiers to enable for this server

          auth_config_ids: ID references to existing authentication configurations

          custom_tools: Additional custom tool identifiers to enable that aren't part of standard
              toolkits

          managed_auth_via_composio: Whether to manage authentication via Composio

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/mcp/servers/custom",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "toolkits": toolkits,
                    "auth_config_ids": auth_config_ids,
                    "custom_tools": custom_tools,
                    "managed_auth_via_composio": managed_auth_via_composio,
                },
                custom_create_params.CustomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCreateResponse,
        )


class CustomResourceWithRawResponse:
    def __init__(self, custom: CustomResource) -> None:
        self._custom = custom

        self.create = to_raw_response_wrapper(
            custom.create,
        )


class AsyncCustomResourceWithRawResponse:
    def __init__(self, custom: AsyncCustomResource) -> None:
        self._custom = custom

        self.create = async_to_raw_response_wrapper(
            custom.create,
        )


class CustomResourceWithStreamingResponse:
    def __init__(self, custom: CustomResource) -> None:
        self._custom = custom

        self.create = to_streamed_response_wrapper(
            custom.create,
        )


class AsyncCustomResourceWithStreamingResponse:
    def __init__(self, custom: AsyncCustomResource) -> None:
        self._custom = custom

        self.create = async_to_streamed_response_wrapper(
            custom.create,
        )
