# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

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
from ...types.project import config_update_params
from ...types.project.config_update_response import ConfigUpdateResponse
from ...types.project.config_retrieve_response import ConfigRetrieveResponse

__all__ = ["ConfigResource", "AsyncConfigResource"]


class ConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return ConfigResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRetrieveResponse:
        """Retrieves the current project configuration including 2FA settings."""
        return self._get(
            "/api/v3/org/project/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveResponse,
        )

    def update(
        self,
        *,
        display_name: str | Omit = omit,
        is_2_fa_enabled: bool | Omit = omit,
        is_composio_link_enabled_for_managed_auth: bool | Omit = omit,
        log_visibility_setting: Literal["show_all", "dont_store_data"] | Omit = omit,
        logo_url: str | Omit = omit,
        mask_secret_keys_in_connected_account: bool | Omit = omit,
        require_mcp_api_key: bool | Omit = omit,
        signed_url_file_expiry_in_seconds: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigUpdateResponse:
        """
        Updates the project configuration settings.

        Args:
          is_composio_link_enabled_for_managed_auth: Whether to enable composio link for managed authentication. This key will be
              deprecated in the future. Please don't use this key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/api/v3/org/project/config",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "is_2_fa_enabled": is_2_fa_enabled,
                    "is_composio_link_enabled_for_managed_auth": is_composio_link_enabled_for_managed_auth,
                    "log_visibility_setting": log_visibility_setting,
                    "logo_url": logo_url,
                    "mask_secret_keys_in_connected_account": mask_secret_keys_in_connected_account,
                    "require_mcp_api_key": require_mcp_api_key,
                    "signed_url_file_expiry_in_seconds": signed_url_file_expiry_in_seconds,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateResponse,
        )


class AsyncConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncConfigResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRetrieveResponse:
        """Retrieves the current project configuration including 2FA settings."""
        return await self._get(
            "/api/v3/org/project/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveResponse,
        )

    async def update(
        self,
        *,
        display_name: str | Omit = omit,
        is_2_fa_enabled: bool | Omit = omit,
        is_composio_link_enabled_for_managed_auth: bool | Omit = omit,
        log_visibility_setting: Literal["show_all", "dont_store_data"] | Omit = omit,
        logo_url: str | Omit = omit,
        mask_secret_keys_in_connected_account: bool | Omit = omit,
        require_mcp_api_key: bool | Omit = omit,
        signed_url_file_expiry_in_seconds: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigUpdateResponse:
        """
        Updates the project configuration settings.

        Args:
          is_composio_link_enabled_for_managed_auth: Whether to enable composio link for managed authentication. This key will be
              deprecated in the future. Please don't use this key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/api/v3/org/project/config",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "is_2_fa_enabled": is_2_fa_enabled,
                    "is_composio_link_enabled_for_managed_auth": is_composio_link_enabled_for_managed_auth,
                    "log_visibility_setting": log_visibility_setting,
                    "logo_url": logo_url,
                    "mask_secret_keys_in_connected_account": mask_secret_keys_in_connected_account,
                    "require_mcp_api_key": require_mcp_api_key,
                    "signed_url_file_expiry_in_seconds": signed_url_file_expiry_in_seconds,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateResponse,
        )


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.retrieve = to_raw_response_wrapper(
            config.retrieve,
        )
        self.update = to_raw_response_wrapper(
            config.update,
        )


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.retrieve = async_to_raw_response_wrapper(
            config.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            config.update,
        )


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.retrieve = to_streamed_response_wrapper(
            config.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            config.update,
        )


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.retrieve = async_to_streamed_response_wrapper(
            config.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            config.update,
        )
