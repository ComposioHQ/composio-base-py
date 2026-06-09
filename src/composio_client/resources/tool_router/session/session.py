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
    session_patch_params,
    session_tools_params,
    session_attach_params,
    session_create_params,
    session_search_params,
    session_execute_params,
    session_toolkits_params,
    session_execute_meta_params,
    session_proxy_execute_params,
    session_config_history_params,
)
from ....types.tool_router.session_link_response import SessionLinkResponse
from ....types.tool_router.session_patch_response import SessionPatchResponse
from ....types.tool_router.session_tools_response import SessionToolsResponse
from ....types.tool_router.session_attach_response import SessionAttachResponse
from ....types.tool_router.session_create_response import SessionCreateResponse
from ....types.tool_router.session_search_response import SessionSearchResponse
from ....types.tool_router.session_execute_response import SessionExecuteResponse
from ....types.tool_router.session_retrieve_response import SessionRetrieveResponse
from ....types.tool_router.session_toolkits_response import SessionToolkitsResponse
from ....types.tool_router.session_execute_meta_response import SessionExecuteMetaResponse
from ....types.tool_router.session_proxy_execute_response import SessionProxyExecuteResponse
from ....types.tool_router.session_config_history_response import SessionConfigHistoryResponse

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
        connected_accounts: Dict[str, SequenceNotStr[str]] | Omit = omit,
        execute: session_create_params.Execute | Omit = omit,
        experimental: session_create_params.Experimental | Omit = omit,
        manage_connections: session_create_params.ManageConnections | Omit = omit,
        multi_account: session_create_params.MultiAccount | Omit = omit,
        preload: session_create_params.Preload | Omit = omit,
        search: session_create_params.Search | Omit = omit,
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

          connected_accounts: The connected accounts to use for the session, as an array of nano-IDs per
              toolkit. This overrides the default behaviour and pins specific connected
              accounts when toolkits are executed. Each account must exist (not deleted or
              disabled) and belong to the same `user_id` as the session. Multi-account
              sessions can pin multiple; non-multi-account sessions are capped at length 1.

          experimental: Experimental features - not stable, may be modified or removed in future
              versions.

          manage_connections: Configuration for connection management settings

          multi_account: Configure multi-account behavior. When enabled, users can connect multiple
              accounts per toolkit.

          preload: Preload configuration. Use an explicit list for frequently used tool slugs, or
              "all" to dynamically expose every app tool allowed by positive
              toolkits/tools/tags filters.

          tags: Global MCP tool annotation hints for filtering. Array format is treated as
              enabled list. Object format supports both enabled (tool must have at least one)
              and disabled (tool must NOT have any) lists. Toolkit-level tags override this.
              Toolkit enabled/disabled lists take precedence over tag filtering.

          toolkits: Toolkit configuration - specify either enable toolkits (allowlist) or disable
              toolkits (denylist). Mutually exclusive.

          tools: Tool-level configuration per toolkit. Allows you to enable, disable, or filter
              by tags for specific tools within each toolkit. Every slug passed in `enable` /
              `disable` must be a valid Composio tool slug for that toolkit — invalid or
              typo'd slugs fail session creation with a clear error listing which ones didn't
              match.

          workbench: Configuration for workbench behavior

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3.1/tool_router/session",
            body=maybe_transform(
                {
                    "user_id": user_id,
                    "auth_configs": auth_configs,
                    "connected_accounts": connected_accounts,
                    "execute": execute,
                    "experimental": experimental,
                    "manage_connections": manage_connections,
                    "multi_account": multi_account,
                    "preload": preload,
                    "search": search,
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
            path_template("/api/v3.1/tool_router/session/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRetrieveResponse,
        )

    def attach(
        self,
        session_id: str,
        *,
        experimental: session_attach_params.Experimental | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionAttachResponse:
        """
        Fetch an existing tool router session by ID.

        Args:
          session_id: The unique identifier of the tool router session

          experimental: Inline custom tools and toolkits for this request. v3.1 sessions do not persist
              customs — pass them on every request that needs them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/v3.1/tool_router/session/{session_id}/attach", session_id=session_id),
            body=maybe_transform({"experimental": experimental}, session_attach_params.SessionAttachParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionAttachResponse,
        )

    def config_history(
        self,
        session_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionConfigHistoryResponse:
        """Returns the session config history ordered by version DESC (newest first).

        The
        live (current) config appears once, on the first page only, with
        `is_current: true`; archived versions have `is_current: false`.

        Args:
          session_id: The unique identifier of the tool router session

          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          limit: Number of items per page, max allowed is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/v3.1/tool_router/session/{session_id}/config_history", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    session_config_history_params.SessionConfigHistoryParams,
                ),
            ),
            cast_to=SessionConfigHistoryResponse,
        )

    def execute(
        self,
        session_id: str,
        *,
        tool_slug: str,
        account: str | Omit = omit,
        arguments: Dict[str, Optional[object]] | Omit = omit,
        enable_auto_workbench_offload: bool | Omit = omit,
        experimental: session_execute_params.Experimental | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExecuteResponse:
        """
        Execute a tool (meta or app) within an existing tool router session.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          tool_slug: The unique slug identifier of the tool to execute. Supports both meta tools and
              app tools exposed by the session.

          account: Account identifier to specify which connected account to use for direct tool
              execution. Use the account ID (e.g. "coup_hurricane_dal_analytical") or an
              alias. When omitted with a single account, the default is used. When omitted
              with multiple accounts, an error lists available accounts. Meta/helper tools
              either ignore this top-level field or define their own account-selection fields,
              for example COMPOSIO_MULTI_EXECUTE_TOOL.tools[].account.

          arguments: The arguments required by the tool

          enable_auto_workbench_offload: When true, direct non-meta tool execution may return a workbench offload preview
              if the response exceeds the configured threshold and the session workbench is
              enabled. When omitted or false, direct tool execution returns the normal inline
              response. Meta/helper tools are unaffected, and COMPOSIO_MULTI_EXECUTE_TOOL uses
              session.workbench configuration for its own batch-level offload behavior.

          experimental: Inline custom tools and toolkits for this request. v3.1 sessions do not persist
              customs — pass them on every request that needs them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/v3.1/tool_router/session/{session_id}/execute", session_id=session_id),
            body=maybe_transform(
                {
                    "tool_slug": tool_slug,
                    "account": account,
                    "arguments": arguments,
                    "enable_auto_workbench_offload": enable_auto_workbench_offload,
                    "experimental": experimental,
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
        ],
        arguments: Dict[str, Optional[object]] | Omit = omit,
        experimental: session_execute_meta_params.Experimental | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExecuteMetaResponse:
        """
        Execute a Composio meta tool (COMPOSIO\\__\\**) within an existing tool router
        session.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          slug: The unique slug identifier of the meta tool to execute

          arguments: The arguments required by the meta tool

          experimental: Inline custom tools and toolkits for this request. v3.1 sessions do not persist
              customs — pass them on every request that needs them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/v3.1/tool_router/session/{session_id}/execute_meta", session_id=session_id),
            body=maybe_transform(
                {
                    "slug": slug,
                    "arguments": arguments,
                    "experimental": experimental,
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
        experimental: session_link_params.Experimental | Omit = omit,
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

          experimental: Experimental features - not stable, may be modified or removed in future
              versions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/v3.1/tool_router/session/{session_id}/link", session_id=session_id),
            body=maybe_transform(
                {
                    "toolkit": toolkit,
                    "alias": alias,
                    "callback_url": callback_url,
                    "experimental": experimental,
                },
                session_link_params.SessionLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionLinkResponse,
        )

    def patch(
        self,
        session_id: str,
        *,
        auth_configs: Dict[str, str] | Omit = omit,
        connected_accounts: Optional[Dict[str, SequenceNotStr[str]]] | Omit = omit,
        execute: session_patch_params.Execute | Omit = omit,
        experimental: Optional[session_patch_params.Experimental] | Omit = omit,
        manage_connections: Optional[session_patch_params.ManageConnections] | Omit = omit,
        multi_account: Optional[session_patch_params.MultiAccount] | Omit = omit,
        preload: session_patch_params.Preload | Omit = omit,
        search: session_patch_params.Search | Omit = omit,
        tags: session_patch_params.Tags | Omit = omit,
        toolkits: session_patch_params.Toolkits | Omit = omit,
        tools: Dict[str, session_patch_params.Tools] | Omit = omit,
        workbench: Optional[session_patch_params.Workbench] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionPatchResponse:
        """Partially updates the configuration of an existing tool router session.

        Only the
        fields provided in the request body will be updated. Uses optimistic concurrency
        control to prevent lost updates. The previous config is stored in config
        history.

        Args:
          session_id: The unique identifier of the tool router session

          auth_configs: The auth configs to use for the session. This will override the default behavior
              and use the given auth config when specific toolkits are being executed

          connected_accounts: The connected accounts to use for the session, as an array of nano-IDs per
              toolkit. This overrides the default behaviour and pins specific connected
              accounts when toolkits are executed. Each account must exist (not deleted or
              disabled) and belong to the same `user_id` as the session. Multi-account
              sessions can pin multiple; non-multi-account sessions are capped at length 1.

          preload: Preload configuration. Use an explicit list for frequently used tool slugs, or
              "all" to dynamically expose every app tool allowed by positive
              toolkits/tools/tags filters.

          tags: Global MCP tool annotation hints for filtering. Array format is treated as
              enabled list. Object format supports both enabled (tool must have at least one)
              and disabled (tool must NOT have any) lists. Toolkit-level tags override this.
              Toolkit enabled/disabled lists take precedence over tag filtering.

          toolkits: Toolkit configuration - specify either enable toolkits (allowlist) or disable
              toolkits (denylist). Mutually exclusive.

          tools: Tool-level configuration per toolkit. Allows you to enable, disable, or filter
              by tags for specific tools within each toolkit. Every slug passed in `enable` /
              `disable` must be a valid Composio tool slug for that toolkit — invalid or
              typo'd slugs fail session creation with a clear error listing which ones didn't
              match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._patch(
            path_template("/api/v3.1/tool_router/session/{session_id}", session_id=session_id),
            body=maybe_transform(
                {
                    "auth_configs": auth_configs,
                    "connected_accounts": connected_accounts,
                    "execute": execute,
                    "experimental": experimental,
                    "manage_connections": manage_connections,
                    "multi_account": multi_account,
                    "preload": preload,
                    "search": search,
                    "tags": tags,
                    "toolkits": toolkits,
                    "tools": tools,
                    "workbench": workbench,
                },
                session_patch_params.SessionPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionPatchResponse,
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
            path_template("/api/v3.1/tool_router/session/{session_id}/proxy_execute", session_id=session_id),
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
        experimental: session_search_params.Experimental | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSearchResponse:
        """
        Search for tools matching a use case query within an existing tool router
        session.

        Args:
          session_id: Tool router session ID (trs\\__\\**)

          queries: List of search queries to execute in parallel.

          experimental: Inline custom tools and toolkits for this request. v3.1 sessions do not persist
              customs — pass them on every request that needs them.

          model: Optional model hint for search/planning behavior (e.g., "gpt-4o").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/v3.1/tool_router/session/{session_id}/search", session_id=session_id),
            body=maybe_transform(
                {
                    "queries": queries,
                    "experimental": experimental,
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
            path_template("/api/v3.1/tool_router/session/{session_id}/toolkits", session_id=session_id),
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
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionToolsResponse:
        """Returns tools available in a tool router session with complete schemas.

        Results
        are paginated; use `next_cursor` to fetch the next page.

        Args:
          session_id: Tool router session ID

          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          limit: Number of items per page, max allowed is 500

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/v3.1/tool_router/session/{session_id}/tools", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    session_tools_params.SessionToolsParams,
                ),
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
        connected_accounts: Dict[str, SequenceNotStr[str]] | Omit = omit,
        execute: session_create_params.Execute | Omit = omit,
        experimental: session_create_params.Experimental | Omit = omit,
        manage_connections: session_create_params.ManageConnections | Omit = omit,
        multi_account: session_create_params.MultiAccount | Omit = omit,
        preload: session_create_params.Preload | Omit = omit,
        search: session_create_params.Search | Omit = omit,
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

          connected_accounts: The connected accounts to use for the session, as an array of nano-IDs per
              toolkit. This overrides the default behaviour and pins specific connected
              accounts when toolkits are executed. Each account must exist (not deleted or
              disabled) and belong to the same `user_id` as the session. Multi-account
              sessions can pin multiple; non-multi-account sessions are capped at length 1.

          experimental: Experimental features - not stable, may be modified or removed in future
              versions.

          manage_connections: Configuration for connection management settings

          multi_account: Configure multi-account behavior. When enabled, users can connect multiple
              accounts per toolkit.

          preload: Preload configuration. Use an explicit list for frequently used tool slugs, or
              "all" to dynamically expose every app tool allowed by positive
              toolkits/tools/tags filters.

          tags: Global MCP tool annotation hints for filtering. Array format is treated as
              enabled list. Object format supports both enabled (tool must have at least one)
              and disabled (tool must NOT have any) lists. Toolkit-level tags override this.
              Toolkit enabled/disabled lists take precedence over tag filtering.

          toolkits: Toolkit configuration - specify either enable toolkits (allowlist) or disable
              toolkits (denylist). Mutually exclusive.

          tools: Tool-level configuration per toolkit. Allows you to enable, disable, or filter
              by tags for specific tools within each toolkit. Every slug passed in `enable` /
              `disable` must be a valid Composio tool slug for that toolkit — invalid or
              typo'd slugs fail session creation with a clear error listing which ones didn't
              match.

          workbench: Configuration for workbench behavior

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3.1/tool_router/session",
            body=await async_maybe_transform(
                {
                    "user_id": user_id,
                    "auth_configs": auth_configs,
                    "connected_accounts": connected_accounts,
                    "execute": execute,
                    "experimental": experimental,
                    "manage_connections": manage_connections,
                    "multi_account": multi_account,
                    "preload": preload,
                    "search": search,
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
            path_template("/api/v3.1/tool_router/session/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRetrieveResponse,
        )

    async def attach(
        self,
        session_id: str,
        *,
        experimental: session_attach_params.Experimental | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionAttachResponse:
        """
        Fetch an existing tool router session by ID.

        Args:
          session_id: The unique identifier of the tool router session

          experimental: Inline custom tools and toolkits for this request. v3.1 sessions do not persist
              customs — pass them on every request that needs them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/v3.1/tool_router/session/{session_id}/attach", session_id=session_id),
            body=await async_maybe_transform({"experimental": experimental}, session_attach_params.SessionAttachParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionAttachResponse,
        )

    async def config_history(
        self,
        session_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionConfigHistoryResponse:
        """Returns the session config history ordered by version DESC (newest first).

        The
        live (current) config appears once, on the first page only, with
        `is_current: true`; archived versions have `is_current: false`.

        Args:
          session_id: The unique identifier of the tool router session

          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          limit: Number of items per page, max allowed is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/v3.1/tool_router/session/{session_id}/config_history", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    session_config_history_params.SessionConfigHistoryParams,
                ),
            ),
            cast_to=SessionConfigHistoryResponse,
        )

    async def execute(
        self,
        session_id: str,
        *,
        tool_slug: str,
        account: str | Omit = omit,
        arguments: Dict[str, Optional[object]] | Omit = omit,
        enable_auto_workbench_offload: bool | Omit = omit,
        experimental: session_execute_params.Experimental | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExecuteResponse:
        """
        Execute a tool (meta or app) within an existing tool router session.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          tool_slug: The unique slug identifier of the tool to execute. Supports both meta tools and
              app tools exposed by the session.

          account: Account identifier to specify which connected account to use for direct tool
              execution. Use the account ID (e.g. "coup_hurricane_dal_analytical") or an
              alias. When omitted with a single account, the default is used. When omitted
              with multiple accounts, an error lists available accounts. Meta/helper tools
              either ignore this top-level field or define their own account-selection fields,
              for example COMPOSIO_MULTI_EXECUTE_TOOL.tools[].account.

          arguments: The arguments required by the tool

          enable_auto_workbench_offload: When true, direct non-meta tool execution may return a workbench offload preview
              if the response exceeds the configured threshold and the session workbench is
              enabled. When omitted or false, direct tool execution returns the normal inline
              response. Meta/helper tools are unaffected, and COMPOSIO_MULTI_EXECUTE_TOOL uses
              session.workbench configuration for its own batch-level offload behavior.

          experimental: Inline custom tools and toolkits for this request. v3.1 sessions do not persist
              customs — pass them on every request that needs them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/v3.1/tool_router/session/{session_id}/execute", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "tool_slug": tool_slug,
                    "account": account,
                    "arguments": arguments,
                    "enable_auto_workbench_offload": enable_auto_workbench_offload,
                    "experimental": experimental,
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
        ],
        arguments: Dict[str, Optional[object]] | Omit = omit,
        experimental: session_execute_meta_params.Experimental | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExecuteMetaResponse:
        """
        Execute a Composio meta tool (COMPOSIO\\__\\**) within an existing tool router
        session.

        Args:
          session_id: The unique identifier of the tool router session. Required for public API
              endpoints, optional for internal endpoints where it is injected by middleware.

          slug: The unique slug identifier of the meta tool to execute

          arguments: The arguments required by the meta tool

          experimental: Inline custom tools and toolkits for this request. v3.1 sessions do not persist
              customs — pass them on every request that needs them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/v3.1/tool_router/session/{session_id}/execute_meta", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "slug": slug,
                    "arguments": arguments,
                    "experimental": experimental,
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
        experimental: session_link_params.Experimental | Omit = omit,
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

          experimental: Experimental features - not stable, may be modified or removed in future
              versions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/v3.1/tool_router/session/{session_id}/link", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "toolkit": toolkit,
                    "alias": alias,
                    "callback_url": callback_url,
                    "experimental": experimental,
                },
                session_link_params.SessionLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionLinkResponse,
        )

    async def patch(
        self,
        session_id: str,
        *,
        auth_configs: Dict[str, str] | Omit = omit,
        connected_accounts: Optional[Dict[str, SequenceNotStr[str]]] | Omit = omit,
        execute: session_patch_params.Execute | Omit = omit,
        experimental: Optional[session_patch_params.Experimental] | Omit = omit,
        manage_connections: Optional[session_patch_params.ManageConnections] | Omit = omit,
        multi_account: Optional[session_patch_params.MultiAccount] | Omit = omit,
        preload: session_patch_params.Preload | Omit = omit,
        search: session_patch_params.Search | Omit = omit,
        tags: session_patch_params.Tags | Omit = omit,
        toolkits: session_patch_params.Toolkits | Omit = omit,
        tools: Dict[str, session_patch_params.Tools] | Omit = omit,
        workbench: Optional[session_patch_params.Workbench] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionPatchResponse:
        """Partially updates the configuration of an existing tool router session.

        Only the
        fields provided in the request body will be updated. Uses optimistic concurrency
        control to prevent lost updates. The previous config is stored in config
        history.

        Args:
          session_id: The unique identifier of the tool router session

          auth_configs: The auth configs to use for the session. This will override the default behavior
              and use the given auth config when specific toolkits are being executed

          connected_accounts: The connected accounts to use for the session, as an array of nano-IDs per
              toolkit. This overrides the default behaviour and pins specific connected
              accounts when toolkits are executed. Each account must exist (not deleted or
              disabled) and belong to the same `user_id` as the session. Multi-account
              sessions can pin multiple; non-multi-account sessions are capped at length 1.

          preload: Preload configuration. Use an explicit list for frequently used tool slugs, or
              "all" to dynamically expose every app tool allowed by positive
              toolkits/tools/tags filters.

          tags: Global MCP tool annotation hints for filtering. Array format is treated as
              enabled list. Object format supports both enabled (tool must have at least one)
              and disabled (tool must NOT have any) lists. Toolkit-level tags override this.
              Toolkit enabled/disabled lists take precedence over tag filtering.

          toolkits: Toolkit configuration - specify either enable toolkits (allowlist) or disable
              toolkits (denylist). Mutually exclusive.

          tools: Tool-level configuration per toolkit. Allows you to enable, disable, or filter
              by tags for specific tools within each toolkit. Every slug passed in `enable` /
              `disable` must be a valid Composio tool slug for that toolkit — invalid or
              typo'd slugs fail session creation with a clear error listing which ones didn't
              match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._patch(
            path_template("/api/v3.1/tool_router/session/{session_id}", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "auth_configs": auth_configs,
                    "connected_accounts": connected_accounts,
                    "execute": execute,
                    "experimental": experimental,
                    "manage_connections": manage_connections,
                    "multi_account": multi_account,
                    "preload": preload,
                    "search": search,
                    "tags": tags,
                    "toolkits": toolkits,
                    "tools": tools,
                    "workbench": workbench,
                },
                session_patch_params.SessionPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionPatchResponse,
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
            path_template("/api/v3.1/tool_router/session/{session_id}/proxy_execute", session_id=session_id),
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
        experimental: session_search_params.Experimental | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSearchResponse:
        """
        Search for tools matching a use case query within an existing tool router
        session.

        Args:
          session_id: Tool router session ID (trs\\__\\**)

          queries: List of search queries to execute in parallel.

          experimental: Inline custom tools and toolkits for this request. v3.1 sessions do not persist
              customs — pass them on every request that needs them.

          model: Optional model hint for search/planning behavior (e.g., "gpt-4o").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/v3.1/tool_router/session/{session_id}/search", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "queries": queries,
                    "experimental": experimental,
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
            path_template("/api/v3.1/tool_router/session/{session_id}/toolkits", session_id=session_id),
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
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionToolsResponse:
        """Returns tools available in a tool router session with complete schemas.

        Results
        are paginated; use `next_cursor` to fetch the next page.

        Args:
          session_id: Tool router session ID

          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          limit: Number of items per page, max allowed is 500

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/v3.1/tool_router/session/{session_id}/tools", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    session_tools_params.SessionToolsParams,
                ),
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
        self.attach = to_raw_response_wrapper(
            session.attach,
        )
        self.config_history = to_raw_response_wrapper(
            session.config_history,
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
        self.patch = to_raw_response_wrapper(
            session.patch,
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
        self.attach = async_to_raw_response_wrapper(
            session.attach,
        )
        self.config_history = async_to_raw_response_wrapper(
            session.config_history,
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
        self.patch = async_to_raw_response_wrapper(
            session.patch,
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
        self.attach = to_streamed_response_wrapper(
            session.attach,
        )
        self.config_history = to_streamed_response_wrapper(
            session.config_history,
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
        self.patch = to_streamed_response_wrapper(
            session.patch,
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
        self.attach = async_to_streamed_response_wrapper(
            session.attach,
        )
        self.config_history = async_to_streamed_response_wrapper(
            session.config_history,
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
        self.patch = async_to_streamed_response_wrapper(
            session.patch,
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
