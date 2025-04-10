# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..types import auth_config_list_params, auth_config_create_params, auth_config_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ..types.auth_config_delete_response import AuthConfigDeleteResponse
from ..types.auth_config_update_response import AuthConfigUpdateResponse
from ..types.auth_config_retrieve_response import AuthConfigRetrieveResponse
from ..types.auth_config_update_status_response import AuthConfigUpdateStatusResponse

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
        Args:
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

    def update(
        self,
        nanoid: str,
        *,
        auth_config: auth_config_update_params.AuthConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthConfigUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return self._patch(
            f"/api/v3/auth_configs/{nanoid}",
            body=maybe_transform({"auth_config": auth_config}, auth_config_update_params.AuthConfigUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthConfigUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        is_composio_managed: Union[str, bool] | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        toolkit_slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthConfigListResponse:
        """
        Args:
          cursor: The cursor to paginate through the auth configs

          is_composio_managed: Whether to filter by composio managed auth configs

          limit: The number of auth configs to return

          toolkit_slug: The slug of the toolkit to filter by

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
                        "is_composio_managed": is_composio_managed,
                        "limit": limit,
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
    ) -> AuthConfigDeleteResponse:
        """
        Args:
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
            cast_to=AuthConfigDeleteResponse,
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
    ) -> AuthConfigUpdateStatusResponse:
        """
        Args:
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
            cast_to=AuthConfigUpdateStatusResponse,
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
        Args:
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

    async def update(
        self,
        nanoid: str,
        *,
        auth_config: auth_config_update_params.AuthConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthConfigUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nanoid:
            raise ValueError(f"Expected a non-empty value for `nanoid` but received {nanoid!r}")
        return await self._patch(
            f"/api/v3/auth_configs/{nanoid}",
            body=await async_maybe_transform(
                {"auth_config": auth_config}, auth_config_update_params.AuthConfigUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthConfigUpdateResponse,
        )

    async def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        is_composio_managed: Union[str, bool] | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        toolkit_slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthConfigListResponse:
        """
        Args:
          cursor: The cursor to paginate through the auth configs

          is_composio_managed: Whether to filter by composio managed auth configs

          limit: The number of auth configs to return

          toolkit_slug: The slug of the toolkit to filter by

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
                        "is_composio_managed": is_composio_managed,
                        "limit": limit,
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
    ) -> AuthConfigDeleteResponse:
        """
        Args:
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
            cast_to=AuthConfigDeleteResponse,
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
    ) -> AuthConfigUpdateStatusResponse:
        """
        Args:
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
            cast_to=AuthConfigUpdateStatusResponse,
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
