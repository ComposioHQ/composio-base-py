# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, overload

import httpx

from ..types import auth_config_list_params, auth_config_create_params, auth_config_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
        auth_config: auth_config_create_params.AuthConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        credentials: Dict[str, Optional[object]],
        type: Literal["custom"],
        tool_access_config: auth_config_update_params.Variant0ToolAccessConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Modifies an existing authentication configuration with new credentials or other
        settings. Only specified fields will be updated.

        Args:
          nanoid: The unique identifier of the authentication configuration to update

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
        scopes: str | NotGiven = NOT_GIVEN,
        tool_access_config: auth_config_update_params.Variant1ToolAccessConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Modifies an existing authentication configuration with new credentials or other
        settings. Only specified fields will be updated.

        Args:
          nanoid: The unique identifier of the authentication configuration to update

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
        credentials: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        type: Literal["custom"] | Literal["default"],
        tool_access_config: auth_config_update_params.Variant0ToolAccessConfig | NotGiven = NOT_GIVEN,
        scopes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return self._patch(
            f"/api/v3/auth_configs/{nanoid}",
            body=maybe_transform(
                {
                    "credentials": credentials,
                    "type": type,
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
        cursor: str | NotGiven = NOT_GIVEN,
        deprecated_app_id: str | NotGiven = NOT_GIVEN,
        deprecated_status: str | NotGiven = NOT_GIVEN,
        is_composio_managed: Union[str, bool] | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        show_disabled: Optional[bool] | NotGiven = NOT_GIVEN,
        toolkit_slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthConfigListResponse:
        """
        List authentication configurations with optional filters

        Args:
          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          deprecated_app_id: The app id to filter by

          is_composio_managed: Whether to filter by composio managed auth configs

          limit: Number of items per page

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        auth_config: auth_config_create_params.AuthConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        credentials: Dict[str, Optional[object]],
        type: Literal["custom"],
        tool_access_config: auth_config_update_params.Variant0ToolAccessConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Modifies an existing authentication configuration with new credentials or other
        settings. Only specified fields will be updated.

        Args:
          nanoid: The unique identifier of the authentication configuration to update

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
        scopes: str | NotGiven = NOT_GIVEN,
        tool_access_config: auth_config_update_params.Variant1ToolAccessConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Modifies an existing authentication configuration with new credentials or other
        settings. Only specified fields will be updated.

        Args:
          nanoid: The unique identifier of the authentication configuration to update

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
        credentials: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        type: Literal["custom"] | Literal["default"],
        tool_access_config: auth_config_update_params.Variant0ToolAccessConfig | NotGiven = NOT_GIVEN,
        scopes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return await self._patch(
            f"/api/v3/auth_configs/{nanoid}",
            body=await async_maybe_transform(
                {
                    "credentials": credentials,
                    "type": type,
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
        cursor: str | NotGiven = NOT_GIVEN,
        deprecated_app_id: str | NotGiven = NOT_GIVEN,
        deprecated_status: str | NotGiven = NOT_GIVEN,
        is_composio_managed: Union[str, bool] | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        show_disabled: Optional[bool] | NotGiven = NOT_GIVEN,
        toolkit_slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthConfigListResponse:
        """
        List authentication configurations with optional filters

        Args:
          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          deprecated_app_id: The app id to filter by

          is_composio_managed: Whether to filter by composio managed auth configs

          limit: Number of items per page

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
