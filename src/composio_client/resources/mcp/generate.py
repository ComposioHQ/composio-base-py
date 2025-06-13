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
from ...types.mcp import generate_url_params
from ..._base_client import make_request_options
from ...types.mcp.generate_url_response import GenerateURLResponse

__all__ = ["GenerateResource", "AsyncGenerateResource"]


class GenerateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return GenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return GenerateResourceWithStreamingResponse(self)

    def url(
        self,
        *,
        mcp_server_id: str,
        connected_account_ids: List[str] | NotGiven = NOT_GIVEN,
        managed_auth_by_composio: bool | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerateURLResponse:
        """
        Generates a Model Control Protocol (MCP) URL for an existing server with custom
        query parameters. The URL includes user-specific parameters and configuration
        flags that control the behavior of the MCP connection.

        Args:
          mcp_server_id: Unique identifier of the MCP server to generate URL for

          connected_account_ids: List of connected account identifiers

          managed_auth_by_composio: Flag indicating if Composio manages authentication

          user_ids: List of user identifiers for whom the URL is generated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/mcp/servers/generate",
            body=maybe_transform(
                {
                    "mcp_server_id": mcp_server_id,
                    "connected_account_ids": connected_account_ids,
                    "managed_auth_by_composio": managed_auth_by_composio,
                    "user_ids": user_ids,
                },
                generate_url_params.GenerateURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateURLResponse,
        )


class AsyncGenerateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncGenerateResourceWithStreamingResponse(self)

    async def url(
        self,
        *,
        mcp_server_id: str,
        connected_account_ids: List[str] | NotGiven = NOT_GIVEN,
        managed_auth_by_composio: bool | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerateURLResponse:
        """
        Generates a Model Control Protocol (MCP) URL for an existing server with custom
        query parameters. The URL includes user-specific parameters and configuration
        flags that control the behavior of the MCP connection.

        Args:
          mcp_server_id: Unique identifier of the MCP server to generate URL for

          connected_account_ids: List of connected account identifiers

          managed_auth_by_composio: Flag indicating if Composio manages authentication

          user_ids: List of user identifiers for whom the URL is generated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/mcp/servers/generate",
            body=await async_maybe_transform(
                {
                    "mcp_server_id": mcp_server_id,
                    "connected_account_ids": connected_account_ids,
                    "managed_auth_by_composio": managed_auth_by_composio,
                    "user_ids": user_ids,
                },
                generate_url_params.GenerateURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateURLResponse,
        )


class GenerateResourceWithRawResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.url = to_raw_response_wrapper(
            generate.url,
        )


class AsyncGenerateResourceWithRawResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.url = async_to_raw_response_wrapper(
            generate.url,
        )


class GenerateResourceWithStreamingResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.url = to_streamed_response_wrapper(
            generate.url,
        )


class AsyncGenerateResourceWithStreamingResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.url = async_to_streamed_response_wrapper(
            generate.url,
        )
