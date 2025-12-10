# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, overload

import httpx

from ..types import auth_config_list_params, auth_config_create_params, auth_config_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.auth_config_list_response import AuthConfigListResponse
from ..types.auth_config_create_response import AuthConfigCreateResponse
from ..types.auth_config_retrieve_response import AuthConfigRetrieveResponse

__all__ = ["AuthConfigsResource", "AsyncAuthConfigsResource"]


class AuthConfigsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AuthConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AuthConfigsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        toolkit: auth_config_create_params.Toolkit,
        auth_config: auth_config_create_params.AuthConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthConfigCreateResponse:
        """
        Create new authentication configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/auth_configs",
            body=maybe_transform(
                {
                    "toolkit": toolkit,
                    "auth_config": auth_config,
                },
                auth_config_create_params.AuthConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthConfigCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthConfigRetrieveResponse:
        """
        Retrieves detailed information about a specific authentication configuration
        using its unique identifier.

        Args:
          nanoid: The unique identifier of the authentication configuration to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return self._get(
            f"/api/v3/auth_configs/{nanoid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthConfigRetrieveResponse,
        )

    @overload
    def update(
        self,
        nanoid: str,
        *,
        credentials: auth_config_update_params.Variant0Credentials,
        type: Literal["custom"],
        proxy_config: auth_config_update_params.Variant0ProxyConfig | Omit = omit,
        restrict_to_following_tools: SequenceNotStr[str] | Omit = omit,
        shared_credentials: Dict[str, Optional[object]] | Omit = omit,
        tool_access_config: auth_config_update_params.Variant0ToolAccessConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Modifies an existing authentication configuration with new credentials or other
        settings. Only specified fields will be updated.

        Args:
          nanoid: The unique identifier of the authentication configuration to update

          restrict_to_following_tools: Use tool_access_config instead. This field will be deprecated in the future.

          shared_credentials: Shared credentials that will be inherited by connected accounts. For eg: this
              can be used to share the API key for a tool with all connected accounts using
              this auth config.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        nanoid: str,
        *,
        type: Literal["default"],
        restrict_to_following_tools: SequenceNotStr[str] | Omit = omit,
        scopes: Union[str, SequenceNotStr[str]] | Omit = omit,
        shared_credentials: Dict[str, Optional[object]] | Omit = omit,
        tool_access_config: auth_config_update_params.Variant1ToolAccessConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Modifies an existing authentication configuration with new credentials or other
        settings. Only specified fields will be updated.

        Args:
          nanoid: The unique identifier of the authentication configuration to update

          restrict_to_following_tools: Use tool_access_config instead. This field will be deprecated in the future.

          shared_credentials: Shared credentials that will be inherited by connected accounts. For eg: this
              can be used to share the API key for a tool with all connected accounts using
              this auth config.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["credentials", "type"], ["type"])
    def update(
        self,
        nanoid: str,
        *,
        credentials: auth_config_update_params.Variant0Credentials | Omit = omit,
        type: Literal["custom"] | Literal["default"],
        proxy_config: auth_config_update_params.Variant0ProxyConfig | Omit = omit,
        restrict_to_following_tools: SequenceNotStr[str] | Omit = omit,
        shared_credentials: Dict[str, Optional[object]] | Omit = omit,
        tool_access_config: auth_config_update_params.Variant0ToolAccessConfig
        | auth_config_update_params.Variant1ToolAccessConfig
        | Omit = omit,
        scopes: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return self._patch(
            f"/api/v3/auth_configs/{nanoid}",
            body=maybe_transform(
                {
                    "credentials": credentials,
                    "type": type,
                    "proxy_config": proxy_config,
                    "restrict_to_following_tools": restrict_to_following_tools,
                    "shared_credentials": shared_credentials,
                    "tool_access_config": tool_access_config,
                    "scopes": scopes,
                },
                auth_config_update_params.AuthConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        deprecated_app_id: str | Omit = omit,
        deprecated_status: str | Omit = omit,
        is_composio_managed: Union[str, bool] | Omit = omit,
        limit: Optional[float] | Omit = omit,
        search: str | Omit = omit,
        show_disabled: Optional[bool] | Omit = omit,
        toolkit_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthConfigListResponse:
        """
        List authentication configurations with optional filters

        Args:
          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          deprecated_app_id: The app id to filter by

          deprecated_status: DEPRECATED: This parameter will be removed in a future version.

          is_composio_managed: Whether to filter by composio managed auth configs

          limit: Number of items per page, max allowed is 1000

          search: Search auth configs by name

          show_disabled: Show disabled auth configs

          toolkit_slug: Comma-separated list of toolkit slugs to filter auth configs by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/auth_configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "deprecated_app_id": deprecated_app_id,
                        "deprecated_status": deprecated_status,
                        "is_composio_managed": is_composio_managed,
                        "limit": limit,
                        "search": search,
                        "show_disabled": show_disabled,
                        "toolkit_slug": toolkit_slug,
                    },
                    auth_config_list_params.AuthConfigListParams,
                ),
            ),
            cast_to=AuthConfigListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Soft-deletes an authentication configuration by marking it as deleted in the
        database. This operation cannot be undone.

        Args:
          nanoid: The unique identifier of the authentication configuration to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return self._delete(
            f"/api/v3/auth_configs/{nanoid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_status(
        self,
        status: Literal["ENABLED", "DISABLED"],
        *,
        nanoid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates the status of an authentication configuration to either enabled or
        disabled. Disabled configurations cannot be used for new connections.

        Args:
          nanoid: The unique identifier of the authentication configuration to update

          status: The new status to set for the auth configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        if not status:
            raise ValueError(f"Expected a non-empty value for `status` but received {status!r}")
        return self._patch(
            f"/api/v3/auth_configs/{nanoid}/{status}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAuthConfigsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncAuthConfigsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        toolkit: auth_config_create_params.Toolkit,
        auth_config: auth_config_create_params.AuthConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthConfigCreateResponse:
        """
        Create new authentication configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/auth_configs",
            body=await async_maybe_transform(
                {
                    "toolkit": toolkit,
                    "auth_config": auth_config,
                },
                auth_config_create_params.AuthConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthConfigCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthConfigRetrieveResponse:
        """
        Retrieves detailed information about a specific authentication configuration
        using its unique identifier.

        Args:
          nanoid: The unique identifier of the authentication configuration to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return await self._get(
            f"/api/v3/auth_configs/{nanoid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthConfigRetrieveResponse,
        )

    @overload
    async def update(
        self,
        nanoid: str,
        *,
        credentials: auth_config_update_params.Variant0Credentials,
        type: Literal["custom"],
        proxy_config: auth_config_update_params.Variant0ProxyConfig | Omit = omit,
        restrict_to_following_tools: SequenceNotStr[str] | Omit = omit,
        shared_credentials: Dict[str, Optional[object]] | Omit = omit,
        tool_access_config: auth_config_update_params.Variant0ToolAccessConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Modifies an existing authentication configuration with new credentials or other
        settings. Only specified fields will be updated.

        Args:
          nanoid: The unique identifier of the authentication configuration to update

          restrict_to_following_tools: Use tool_access_config instead. This field will be deprecated in the future.

          shared_credentials: Shared credentials that will be inherited by connected accounts. For eg: this
              can be used to share the API key for a tool with all connected accounts using
              this auth config.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        nanoid: str,
        *,
        type: Literal["default"],
        restrict_to_following_tools: SequenceNotStr[str] | Omit = omit,
        scopes: Union[str, SequenceNotStr[str]] | Omit = omit,
        shared_credentials: Dict[str, Optional[object]] | Omit = omit,
        tool_access_config: auth_config_update_params.Variant1ToolAccessConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Modifies an existing authentication configuration with new credentials or other
        settings. Only specified fields will be updated.

        Args:
          nanoid: The unique identifier of the authentication configuration to update

          restrict_to_following_tools: Use tool_access_config instead. This field will be deprecated in the future.

          shared_credentials: Shared credentials that will be inherited by connected accounts. For eg: this
              can be used to share the API key for a tool with all connected accounts using
              this auth config.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["credentials", "type"], ["type"])
    async def update(
        self,
        nanoid: str,
        *,
        credentials: auth_config_update_params.Variant0Credentials | Omit = omit,
        type: Literal["custom"] | Literal["default"],
        proxy_config: auth_config_update_params.Variant0ProxyConfig | Omit = omit,
        restrict_to_following_tools: SequenceNotStr[str] | Omit = omit,
        shared_credentials: Dict[str, Optional[object]] | Omit = omit,
        tool_access_config: auth_config_update_params.Variant0ToolAccessConfig
        | auth_config_update_params.Variant1ToolAccessConfig
        | Omit = omit,
        scopes: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return await self._patch(
            f"/api/v3/auth_configs/{nanoid}",
            body=await async_maybe_transform(
                {
                    "credentials": credentials,
                    "type": type,
                    "proxy_config": proxy_config,
                    "restrict_to_following_tools": restrict_to_following_tools,
                    "shared_credentials": shared_credentials,
                    "tool_access_config": tool_access_config,
                    "scopes": scopes,
                },
                auth_config_update_params.AuthConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        deprecated_app_id: str | Omit = omit,
        deprecated_status: str | Omit = omit,
        is_composio_managed: Union[str, bool] | Omit = omit,
        limit: Optional[float] | Omit = omit,
        search: str | Omit = omit,
        show_disabled: Optional[bool] | Omit = omit,
        toolkit_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthConfigListResponse:
        """
        List authentication configurations with optional filters

        Args:
          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          deprecated_app_id: The app id to filter by

          deprecated_status: DEPRECATED: This parameter will be removed in a future version.

          is_composio_managed: Whether to filter by composio managed auth configs

          limit: Number of items per page, max allowed is 1000

          search: Search auth configs by name

          show_disabled: Show disabled auth configs

          toolkit_slug: Comma-separated list of toolkit slugs to filter auth configs by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/auth_configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "deprecated_app_id": deprecated_app_id,
                        "deprecated_status": deprecated_status,
                        "is_composio_managed": is_composio_managed,
                        "limit": limit,
                        "search": search,
                        "show_disabled": show_disabled,
                        "toolkit_slug": toolkit_slug,
                    },
                    auth_config_list_params.AuthConfigListParams,
                ),
            ),
            cast_to=AuthConfigListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Soft-deletes an authentication configuration by marking it as deleted in the
        database. This operation cannot be undone.

        Args:
          nanoid: The unique identifier of the authentication configuration to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return await self._delete(
            f"/api/v3/auth_configs/{nanoid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_status(
        self,
        status: Literal["ENABLED", "DISABLED"],
        *,
        nanoid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates the status of an authentication configuration to either enabled or
        disabled. Disabled configurations cannot be used for new connections.

        Args:
          nanoid: The unique identifier of the authentication configuration to update

          status: The new status to set for the auth configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        if not status:
            raise ValueError(f"Expected a non-empty value for `status` but received {status!r}")
        return await self._patch(
            f"/api/v3/auth_configs/{nanoid}/{status}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AuthConfigsResourceWithRawResponse:
    def __init__(self, auth_configs: AuthConfigsResource) -> None:
        self._auth_configs = auth_configs

        self.create = to_raw_response_wrapper(
            auth_configs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            auth_configs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            auth_configs.update,
        )
        self.list = to_raw_response_wrapper(
            auth_configs.list,
        )
        self.delete = to_raw_response_wrapper(
            auth_configs.delete,
        )
        self.update_status = to_raw_response_wrapper(
            auth_configs.update_status,
        )


class AsyncAuthConfigsResourceWithRawResponse:
    def __init__(self, auth_configs: AsyncAuthConfigsResource) -> None:
        self._auth_configs = auth_configs

        self.create = async_to_raw_response_wrapper(
            auth_configs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            auth_configs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            auth_configs.update,
        )
        self.list = async_to_raw_response_wrapper(
            auth_configs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            auth_configs.delete,
        )
        self.update_status = async_to_raw_response_wrapper(
            auth_configs.update_status,
        )


class AuthConfigsResourceWithStreamingResponse:
    def __init__(self, auth_configs: AuthConfigsResource) -> None:
        self._auth_configs = auth_configs

        self.create = to_streamed_response_wrapper(
            auth_configs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            auth_configs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            auth_configs.update,
        )
        self.list = to_streamed_response_wrapper(
            auth_configs.list,
        )
        self.delete = to_streamed_response_wrapper(
            auth_configs.delete,
        )
        self.update_status = to_streamed_response_wrapper(
            auth_configs.update_status,
        )


class AsyncAuthConfigsResourceWithStreamingResponse:
    def __init__(self, auth_configs: AsyncAuthConfigsResource) -> None:
        self._auth_configs = auth_configs

        self.create = async_to_streamed_response_wrapper(
            auth_configs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            auth_configs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            auth_configs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            auth_configs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            auth_configs.delete,
        )
        self.update_status = async_to_streamed_response_wrapper(
            auth_configs.update_status,
        )
