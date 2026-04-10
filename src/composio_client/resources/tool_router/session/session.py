# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.tool_router import (
    session_link_params,
    session_create_params,
    session_search_params,
    session_execute_params,
    session_toolkits_params,
    session_execute_meta_params,
    session_proxy_execute_params,
)
from ....types.tool_router.session_link_response import SessionLinkResponse
from ....types.tool_router.session_tools_response import SessionToolsResponse
from ....types.tool_router.session_create_response import SessionCreateResponse
from ....types.tool_router.session_search_response import SessionSearchResponse
from ....types.tool_router.session_execute_response import SessionExecuteResponse
from ....types.tool_router.session_retrieve_response import SessionRetrieveResponse
from ....types.tool_router.session_toolkits_response import SessionToolkitsResponse
from ....types.tool_router.session_execute_meta_response import SessionExecuteMetaResponse
from ....types.tool_router.session_proxy_execute_response import SessionProxyExecuteResponse

__all__ = ["SessionResource", "AsyncSessionResource"]


class SessionResource(SyncAPIResource):
    """(Labs) Tool router endpoints"""

    @cached_property
    def files(self) -> FilesResource:
        """(Labs) Tool router endpoints"""
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return SessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return SessionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        user_id: str,
        auth_configs: Dict[str, str] | Omit = omit,
        connected_accounts: Dict[str, str] | Omit = omit,
        experimental: session_create_params.Experimental | Omit = omit,
        manage_connections: session_create_params.ManageConnections | Omit = omit,
        multi_account: session_create_params.MultiAccount | Omit = omit,
        tags: session_create_params.Tags | Omit = omit,
        toolkits: session_create_params.Toolkits | Omit = omit,
        tools: Dict[str, session_create_params.Tools] | Omit = omit,
        workbench: session_create_params.Workbench | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionCreateResponse:
        """Creates a new session for the tool router feature.

        This endpoint initializes a
        new session with specified toolkits and their authentication configurations. The
        session provides an isolated environment for testing and managing tool routing
        logic with scoped MCP server access.

        Args:
          user_id: The identifier of the user who is initiating the session, ideally a unique
              identifier from your database like a user ID or email address

          auth_configs: The auth configs to use for the session. This will override the default behavior
              and use the given auth config when specific toolkits are being executed

          connected_accounts: The connected accounts to use for the session. This will override the default
              behaviour and use the given connected account when specific toolkits are being
              executed

          experimental: Experimental features - not stable, may be modified or removed in future
              versions.

          manage_connections: Configuration for connection management settings

          multi_account: Configure multi-account behavior. When enabled, users can connect multiple
              accounts per toolkit.

          tags: Global MCP tool annotation hints for filtering. Array format is treated as
              enabled list. Object format supports both enabled (tool must have at least one)
              and disabled (tool must NOT have any) lists. Toolkit-level tags override this.
              Toolkit enabled/disabled lists take precedence over tag filtering.

          toolkits: Toolkit configuration - specify either enable toolkits (allowlist) or disable
              toolkits (denylist). Mutually exclusive.

          tools: Tool-level configuration per toolkit - either specify enable tools (whitelist),
              disable tools (blacklist), or filter by MCP tags for each toolkit

          workbench: Configuration for workbench behavior

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/tool_router/session",
            body=maybe_transform(
                {
                    "user_id": user_id,
                    "auth_configs": auth_configs,
                    "connected_accounts": connected_accounts,
                    "experimental": experimental,
                    "manage_connections": manage_connections,
                    "multi_account": multi_account,
                    "tags": tags,
                    "toolkits": toolkits,
                    "tools": tools,
                    "workbench": workbench,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCreateResponse,
        )

    def retrieve(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveResponse:
        """Retrieves an existing tool router session by its ID.

        Returns the session
        configuration, MCP server URL, and available tools.

        Args:
          session_id: The session ID returned when creating the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/v3/tool_router/session/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRetrieveResponse,
        )

    def execute(
        self,
        session_id: str,
        *,
        tool_slug: str,
        account: str | Omit = omit,
        arguments: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExecuteResponse:
        """Executes a specific tool within a tool router session.

        The toolkit is
        automatically inferred from the tool slug. The tool must belong to an allowed
        toolkit and must not be disabled in the session configuration. This endpoint
        validates permissions, resolves connected accounts, and executes the tool with
        the session context.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          tool_slug: The unique slug identifier of the tool to execute

          account: Account identifier to specify which connected account to use. Use the account ID
              (e.g. "coup_hurricane_dal_analytical") or an alias. When omitted with a single
              account, the default is used. When omitted with multiple accounts, an error
              lists available accounts.

          arguments: The arguments required by the tool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/v3/tool_router/session/{session_id}/execute", session_id=session_id),
            body=maybe_transform(
                {
                    "tool_slug": tool_slug,
                    "account": account,
                    "arguments": arguments,
                },
                session_execute_params.SessionExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionExecuteResponse,
        )

    def execute_meta(
        self,
        session_id: str,
        *,
        slug: Literal[
            "COMPOSIO_SEARCH_TOOLS",
            "COMPOSIO_MULTI_EXECUTE_TOOL",
            "COMPOSIO_MANAGE_CONNECTIONS",
            "COMPOSIO_WAIT_FOR_CONNECTIONS",
            "COMPOSIO_REMOTE_WORKBENCH",
            "COMPOSIO_REMOTE_BASH_TOOL",
            "COMPOSIO_GET_TOOL_SCHEMAS",
            "COMPOSIO_UPSERT_RECIPE",
            "COMPOSIO_GET_RECIPE",
        ],
        arguments: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExecuteMetaResponse:
        """
        Executes a Composio meta tool (COMPOSIO\\__\\**) within a tool router session.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          slug: The unique slug identifier of the meta tool to execute

          arguments: The arguments required by the meta tool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/v3/tool_router/session/{session_id}/execute_meta", session_id=session_id),
            body=maybe_transform(
                {
                    "slug": slug,
                    "arguments": arguments,
                },
                session_execute_meta_params.SessionExecuteMetaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionExecuteMetaResponse,
        )

    def link(
        self,
        session_id: str,
        *,
        toolkit: str,
        alias: str | Omit = omit,
        callback_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionLinkResponse:
        """
        Initiates an authentication link session for a specific toolkit within a tool
        router session. Returns a link token and redirect URL that users can use to
        complete the OAuth flow.

        Args:
          session_id: The session ID returned when creating the session

          toolkit: The unique slug identifier of the toolkit to connect

          alias: A human-readable alias for this connected account. Must be unique per entity and
              toolkit within the project.

          callback_url: URL where users will be redirected after completing auth

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/v3/tool_router/session/{session_id}/link", session_id=session_id),
            body=maybe_transform(
                {
                    "toolkit": toolkit,
                    "alias": alias,
                    "callback_url": callback_url,
                },
                session_link_params.SessionLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionLinkResponse,
        )

    def proxy_execute(
        self,
        session_id: str,
        *,
        endpoint: str,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD"],
        toolkit_slug: str,
        binary_body: session_proxy_execute_params.BinaryBody | Omit = omit,
        body: object | Omit = omit,
        custom_connection_data: session_proxy_execute_params.CustomConnectionData | Omit = omit,
        parameters: Iterable[session_proxy_execute_params.Parameter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionProxyExecuteResponse:
        """
        Execute any native API call on a toolkit with authentication automatically
        injected from Composio. This endpoint proxies HTTP requests to third-party APIs
        using connected account credentials resolved from the session context. Provide
        the toolkit slug, API endpoint, and HTTP method — Composio handles
        authentication injection, abstracting away credential management. Supports all
        HTTP methods, custom headers/query parameters, and binary request/response
        bodies.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          endpoint: The API endpoint to call (absolute URL or path relative to base URL of the
              connected account)

          method: The HTTP method to use for the request

          toolkit_slug: The slug of the toolkit to use for the request

          binary_body: Binary body to send. For binary upload via URL: use {url: "https://...",
              content_type?: "..."}. For binary upload via base64: use {base64: "...",
              content_type?: "..."}.

          body: The request body (for POST, PUT, and PATCH requests)

          parameters: Additional HTTP headers or query parameters to include in the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/v3/tool_router/session/{session_id}/proxy_execute", session_id=session_id),
            body=maybe_transform(
                {
                    "endpoint": endpoint,
                    "method": method,
                    "toolkit_slug": toolkit_slug,
                    "binary_body": binary_body,
                    "body": body,
                    "custom_connection_data": custom_connection_data,
                    "parameters": parameters,
                },
                session_proxy_execute_params.SessionProxyExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionProxyExecuteResponse,
        )

    def search(
        self,
        session_id: str,
        *,
        queries: Iterable[session_search_params.Query],
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSearchResponse:
        """
        Search for tools matching a given use case query within a tool router session.
        Returns matching tool slugs, full tool schemas, toolkit connection statuses, and
        workflow guidance in a predictable format.

        Args:
          session_id: Tool router session ID (trs\\__\\**)

          queries: List of search queries to execute in parallel. Up to 7 queries supported.

          model: Optional model hint for search/planning behavior (e.g., "gpt-4o"). Ignored if
              invalid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/v3/tool_router/session/{session_id}/search", session_id=session_id),
            body=maybe_transform(
                {
                    "queries": queries,
                    "model": model,
                },
                session_search_params.SessionSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionSearchResponse,
        )

    def toolkits(
        self,
        session_id: str,
        *,
        cursor: str | Omit = omit,
        is_connected: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        toolkits: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionToolkitsResponse:
        """
        Retrieves a cursor-paginated list of toolkits available in the tool router
        session. Includes toolkit metadata, composio-managed auth schemes, and connected
        accounts if available. Optionally filter by specific toolkit slugs.

        Args:
          session_id: The session ID returned when creating the session

          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          is_connected: Whether to filter by connected toolkits. If provided, only connected toolkits
              will be returned.

          limit: Number of items per page, max allowed is 50

          search: Search query to filter toolkits by name, slug, or description

          toolkits: Optional comma-separated list of toolkit slugs to filter by. If provided, only
              these toolkits will be returned, overriding the session configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/v3/tool_router/session/{session_id}/toolkits", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "is_connected": is_connected,
                        "limit": limit,
                        "search": search,
                        "toolkits": toolkits,
                    },
                    session_toolkits_params.SessionToolkitsParams,
                ),
            ),
            cast_to=SessionToolkitsResponse,
        )

    def tools(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionToolsResponse:
        """
        Returns the meta tools available in a tool router session with their complete
        schemas. This includes request and response schemas specific to the session
        context.

        Args:
          session_id: Tool router session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/v3/tool_router/session/{session_id}/tools", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionToolsResponse,
        )


class AsyncSessionResource(AsyncAPIResource):
    """(Labs) Tool router endpoints"""

    @cached_property
    def files(self) -> AsyncFilesResource:
        """(Labs) Tool router endpoints"""
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncSessionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        user_id: str,
        auth_configs: Dict[str, str] | Omit = omit,
        connected_accounts: Dict[str, str] | Omit = omit,
        experimental: session_create_params.Experimental | Omit = omit,
        manage_connections: session_create_params.ManageConnections | Omit = omit,
        multi_account: session_create_params.MultiAccount | Omit = omit,
        tags: session_create_params.Tags | Omit = omit,
        toolkits: session_create_params.Toolkits | Omit = omit,
        tools: Dict[str, session_create_params.Tools] | Omit = omit,
        workbench: session_create_params.Workbench | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionCreateResponse:
        """Creates a new session for the tool router feature.

        This endpoint initializes a
        new session with specified toolkits and their authentication configurations. The
        session provides an isolated environment for testing and managing tool routing
        logic with scoped MCP server access.

        Args:
          user_id: The identifier of the user who is initiating the session, ideally a unique
              identifier from your database like a user ID or email address

          auth_configs: The auth configs to use for the session. This will override the default behavior
              and use the given auth config when specific toolkits are being executed

          connected_accounts: The connected accounts to use for the session. This will override the default
              behaviour and use the given connected account when specific toolkits are being
              executed

          experimental: Experimental features - not stable, may be modified or removed in future
              versions.

          manage_connections: Configuration for connection management settings

          multi_account: Configure multi-account behavior. When enabled, users can connect multiple
              accounts per toolkit.

          tags: Global MCP tool annotation hints for filtering. Array format is treated as
              enabled list. Object format supports both enabled (tool must have at least one)
              and disabled (tool must NOT have any) lists. Toolkit-level tags override this.
              Toolkit enabled/disabled lists take precedence over tag filtering.

          toolkits: Toolkit configuration - specify either enable toolkits (allowlist) or disable
              toolkits (denylist). Mutually exclusive.

          tools: Tool-level configuration per toolkit - either specify enable tools (whitelist),
              disable tools (blacklist), or filter by MCP tags for each toolkit

          workbench: Configuration for workbench behavior

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/tool_router/session",
            body=await async_maybe_transform(
                {
                    "user_id": user_id,
                    "auth_configs": auth_configs,
                    "connected_accounts": connected_accounts,
                    "experimental": experimental,
                    "manage_connections": manage_connections,
                    "multi_account": multi_account,
                    "tags": tags,
                    "toolkits": toolkits,
                    "tools": tools,
                    "workbench": workbench,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCreateResponse,
        )

    async def retrieve(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveResponse:
        """Retrieves an existing tool router session by its ID.

        Returns the session
        configuration, MCP server URL, and available tools.

        Args:
          session_id: The session ID returned when creating the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/v3/tool_router/session/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRetrieveResponse,
        )

    async def execute(
        self,
        session_id: str,
        *,
        tool_slug: str,
        account: str | Omit = omit,
        arguments: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExecuteResponse:
        """Executes a specific tool within a tool router session.

        The toolkit is
        automatically inferred from the tool slug. The tool must belong to an allowed
        toolkit and must not be disabled in the session configuration. This endpoint
        validates permissions, resolves connected accounts, and executes the tool with
        the session context.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          tool_slug: The unique slug identifier of the tool to execute

          account: Account identifier to specify which connected account to use. Use the account ID
              (e.g. "coup_hurricane_dal_analytical") or an alias. When omitted with a single
              account, the default is used. When omitted with multiple accounts, an error
              lists available accounts.

          arguments: The arguments required by the tool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/v3/tool_router/session/{session_id}/execute", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "tool_slug": tool_slug,
                    "account": account,
                    "arguments": arguments,
                },
                session_execute_params.SessionExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionExecuteResponse,
        )

    async def execute_meta(
        self,
        session_id: str,
        *,
        slug: Literal[
            "COMPOSIO_SEARCH_TOOLS",
            "COMPOSIO_MULTI_EXECUTE_TOOL",
            "COMPOSIO_MANAGE_CONNECTIONS",
            "COMPOSIO_WAIT_FOR_CONNECTIONS",
            "COMPOSIO_REMOTE_WORKBENCH",
            "COMPOSIO_REMOTE_BASH_TOOL",
            "COMPOSIO_GET_TOOL_SCHEMAS",
            "COMPOSIO_UPSERT_RECIPE",
            "COMPOSIO_GET_RECIPE",
        ],
        arguments: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExecuteMetaResponse:
        """
        Executes a Composio meta tool (COMPOSIO\\__\\**) within a tool router session.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          slug: The unique slug identifier of the meta tool to execute

          arguments: The arguments required by the meta tool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/v3/tool_router/session/{session_id}/execute_meta", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "slug": slug,
                    "arguments": arguments,
                },
                session_execute_meta_params.SessionExecuteMetaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionExecuteMetaResponse,
        )

    async def link(
        self,
        session_id: str,
        *,
        toolkit: str,
        alias: str | Omit = omit,
        callback_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionLinkResponse:
        """
        Initiates an authentication link session for a specific toolkit within a tool
        router session. Returns a link token and redirect URL that users can use to
        complete the OAuth flow.

        Args:
          session_id: The session ID returned when creating the session

          toolkit: The unique slug identifier of the toolkit to connect

          alias: A human-readable alias for this connected account. Must be unique per entity and
              toolkit within the project.

          callback_url: URL where users will be redirected after completing auth

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/v3/tool_router/session/{session_id}/link", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "toolkit": toolkit,
                    "alias": alias,
                    "callback_url": callback_url,
                },
                session_link_params.SessionLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionLinkResponse,
        )

    async def proxy_execute(
        self,
        session_id: str,
        *,
        endpoint: str,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD"],
        toolkit_slug: str,
        binary_body: session_proxy_execute_params.BinaryBody | Omit = omit,
        body: object | Omit = omit,
        custom_connection_data: session_proxy_execute_params.CustomConnectionData | Omit = omit,
        parameters: Iterable[session_proxy_execute_params.Parameter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionProxyExecuteResponse:
        """
        Execute any native API call on a toolkit with authentication automatically
        injected from Composio. This endpoint proxies HTTP requests to third-party APIs
        using connected account credentials resolved from the session context. Provide
        the toolkit slug, API endpoint, and HTTP method — Composio handles
        authentication injection, abstracting away credential management. Supports all
        HTTP methods, custom headers/query parameters, and binary request/response
        bodies.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          endpoint: The API endpoint to call (absolute URL or path relative to base URL of the
              connected account)

          method: The HTTP method to use for the request

          toolkit_slug: The slug of the toolkit to use for the request

          binary_body: Binary body to send. For binary upload via URL: use {url: "https://...",
              content_type?: "..."}. For binary upload via base64: use {base64: "...",
              content_type?: "..."}.

          body: The request body (for POST, PUT, and PATCH requests)

          parameters: Additional HTTP headers or query parameters to include in the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/v3/tool_router/session/{session_id}/proxy_execute", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "endpoint": endpoint,
                    "method": method,
                    "toolkit_slug": toolkit_slug,
                    "binary_body": binary_body,
                    "body": body,
                    "custom_connection_data": custom_connection_data,
                    "parameters": parameters,
                },
                session_proxy_execute_params.SessionProxyExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionProxyExecuteResponse,
        )

    async def search(
        self,
        session_id: str,
        *,
        queries: Iterable[session_search_params.Query],
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSearchResponse:
        """
        Search for tools matching a given use case query within a tool router session.
        Returns matching tool slugs, full tool schemas, toolkit connection statuses, and
        workflow guidance in a predictable format.

        Args:
          session_id: Tool router session ID (trs\\__\\**)

          queries: List of search queries to execute in parallel. Up to 7 queries supported.

          model: Optional model hint for search/planning behavior (e.g., "gpt-4o"). Ignored if
              invalid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/v3/tool_router/session/{session_id}/search", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "queries": queries,
                    "model": model,
                },
                session_search_params.SessionSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionSearchResponse,
        )

    async def toolkits(
        self,
        session_id: str,
        *,
        cursor: str | Omit = omit,
        is_connected: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        toolkits: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionToolkitsResponse:
        """
        Retrieves a cursor-paginated list of toolkits available in the tool router
        session. Includes toolkit metadata, composio-managed auth schemes, and connected
        accounts if available. Optionally filter by specific toolkit slugs.

        Args:
          session_id: The session ID returned when creating the session

          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          is_connected: Whether to filter by connected toolkits. If provided, only connected toolkits
              will be returned.

          limit: Number of items per page, max allowed is 50

          search: Search query to filter toolkits by name, slug, or description

          toolkits: Optional comma-separated list of toolkit slugs to filter by. If provided, only
              these toolkits will be returned, overriding the session configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/v3/tool_router/session/{session_id}/toolkits", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "is_connected": is_connected,
                        "limit": limit,
                        "search": search,
                        "toolkits": toolkits,
                    },
                    session_toolkits_params.SessionToolkitsParams,
                ),
            ),
            cast_to=SessionToolkitsResponse,
        )

    async def tools(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionToolsResponse:
        """
        Returns the meta tools available in a tool router session with their complete
        schemas. This includes request and response schemas specific to the session
        context.

        Args:
          session_id: Tool router session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/v3/tool_router/session/{session_id}/tools", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionToolsResponse,
        )


class SessionResourceWithRawResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_raw_response_wrapper(
            session.create,
        )
        self.retrieve = to_raw_response_wrapper(
            session.retrieve,
        )
        self.execute = to_raw_response_wrapper(
            session.execute,
        )
        self.execute_meta = to_raw_response_wrapper(
            session.execute_meta,
        )
        self.link = to_raw_response_wrapper(
            session.link,
        )
        self.proxy_execute = to_raw_response_wrapper(
            session.proxy_execute,
        )
        self.search = to_raw_response_wrapper(
            session.search,
        )
        self.toolkits = to_raw_response_wrapper(
            session.toolkits,
        )
        self.tools = to_raw_response_wrapper(
            session.tools,
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        """(Labs) Tool router endpoints"""
        return FilesResourceWithRawResponse(self._session.files)


class AsyncSessionResourceWithRawResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_raw_response_wrapper(
            session.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            session.retrieve,
        )
        self.execute = async_to_raw_response_wrapper(
            session.execute,
        )
        self.execute_meta = async_to_raw_response_wrapper(
            session.execute_meta,
        )
        self.link = async_to_raw_response_wrapper(
            session.link,
        )
        self.proxy_execute = async_to_raw_response_wrapper(
            session.proxy_execute,
        )
        self.search = async_to_raw_response_wrapper(
            session.search,
        )
        self.toolkits = async_to_raw_response_wrapper(
            session.toolkits,
        )
        self.tools = async_to_raw_response_wrapper(
            session.tools,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        """(Labs) Tool router endpoints"""
        return AsyncFilesResourceWithRawResponse(self._session.files)


class SessionResourceWithStreamingResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_streamed_response_wrapper(
            session.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            session.retrieve,
        )
        self.execute = to_streamed_response_wrapper(
            session.execute,
        )
        self.execute_meta = to_streamed_response_wrapper(
            session.execute_meta,
        )
        self.link = to_streamed_response_wrapper(
            session.link,
        )
        self.proxy_execute = to_streamed_response_wrapper(
            session.proxy_execute,
        )
        self.search = to_streamed_response_wrapper(
            session.search,
        )
        self.toolkits = to_streamed_response_wrapper(
            session.toolkits,
        )
        self.tools = to_streamed_response_wrapper(
            session.tools,
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        """(Labs) Tool router endpoints"""
        return FilesResourceWithStreamingResponse(self._session.files)


class AsyncSessionResourceWithStreamingResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_streamed_response_wrapper(
            session.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            session.retrieve,
        )
        self.execute = async_to_streamed_response_wrapper(
            session.execute,
        )
        self.execute_meta = async_to_streamed_response_wrapper(
            session.execute_meta,
        )
        self.link = async_to_streamed_response_wrapper(
            session.link,
        )
        self.proxy_execute = async_to_streamed_response_wrapper(
            session.proxy_execute,
        )
        self.search = async_to_streamed_response_wrapper(
            session.search,
        )
        self.toolkits = async_to_streamed_response_wrapper(
            session.toolkits,
        )
        self.tools = async_to_streamed_response_wrapper(
            session.tools,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        """(Labs) Tool router endpoints"""
        return AsyncFilesResourceWithStreamingResponse(self._session.files)
