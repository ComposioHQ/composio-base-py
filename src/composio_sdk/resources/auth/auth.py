# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ...types import auth_login_params, auth_one_tap_params, auth_retrieve_callback_params
from .session import (
    SessionResource,
    AsyncSessionResource,
    SessionResourceWithRawResponse,
    AsyncSessionResourceWithRawResponse,
    SessionResourceWithStreamingResponse,
    AsyncSessionResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .magic_link import (
    MagicLinkResource,
    AsyncMagicLinkResource,
    MagicLinkResourceWithRawResponse,
    AsyncMagicLinkResourceWithRawResponse,
    MagicLinkResourceWithStreamingResponse,
    AsyncMagicLinkResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.auth_one_tap_response import AuthOneTapResponse
from ...types.auth_retrieve_callback_response import AuthRetrieveCallbackResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def magic_link(self) -> MagicLinkResource:
        return MagicLinkResource(self._client)

    @cached_property
    def session(self) -> SessionResource:
        return SessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/composiohq/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/composiohq/composio-base-py#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def login(
        self,
        provider_name: str,
        *,
        redirect_uri: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_name:
            raise ValueError(f"Expected a non-empty value for `provider_name` but received {provider_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v3/auth/{provider_name}/login",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"redirect_uri": redirect_uri}, auth_login_params.AuthLoginParams),
            ),
            cast_to=NoneType,
        )

    @overload
    def one_tap(
        self,
        provider_name: Literal["github", "google"],
        *,
        data: auth_one_tap_params.Variant0Data,
        type: Literal["jwt"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthOneTapResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def one_tap(
        self,
        provider_name: Literal["github", "google"],
        *,
        data: auth_one_tap_params.Variant1Data,
        type: Literal["auth-code"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthOneTapResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["data", "type"])
    def one_tap(
        self,
        provider_name: Literal["github", "google"],
        *,
        data: auth_one_tap_params.Variant0Data | auth_one_tap_params.Variant1Data,
        type: Literal["jwt"] | Literal["auth-code"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthOneTapResponse:
        if not provider_name:
            raise ValueError(f"Expected a non-empty value for `provider_name` but received {provider_name!r}")
        return self._post(
            f"/api/v3/auth/{provider_name}/one-tap",
            body=maybe_transform(
                {
                    "data": data,
                    "type": type,
                },
                auth_one_tap_params.AuthOneTapParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthOneTapResponse,
        )

    def retrieve_callback(
        self,
        provider_name: Literal["github", "google"],
        *,
        auth_code: str | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        error: str | NotGiven = NOT_GIVEN,
        error_description: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRetrieveCallbackResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_name:
            raise ValueError(f"Expected a non-empty value for `provider_name` but received {provider_name!r}")
        return self._get(
            f"/api/v3/auth/{provider_name}/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "auth_code": auth_code,
                        "code": code,
                        "error": error,
                        "error_description": error_description,
                        "state": state,
                    },
                    auth_retrieve_callback_params.AuthRetrieveCallbackParams,
                ),
            ),
            cast_to=AuthRetrieveCallbackResponse,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def magic_link(self) -> AsyncMagicLinkResource:
        return AsyncMagicLinkResource(self._client)

    @cached_property
    def session(self) -> AsyncSessionResource:
        return AsyncSessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/composiohq/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/composiohq/composio-base-py#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def login(
        self,
        provider_name: str,
        *,
        redirect_uri: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_name:
            raise ValueError(f"Expected a non-empty value for `provider_name` but received {provider_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/v3/auth/{provider_name}/login",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"redirect_uri": redirect_uri}, auth_login_params.AuthLoginParams),
            ),
            cast_to=NoneType,
        )

    @overload
    async def one_tap(
        self,
        provider_name: Literal["github", "google"],
        *,
        data: auth_one_tap_params.Variant0Data,
        type: Literal["jwt"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthOneTapResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def one_tap(
        self,
        provider_name: Literal["github", "google"],
        *,
        data: auth_one_tap_params.Variant1Data,
        type: Literal["auth-code"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthOneTapResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["data", "type"])
    async def one_tap(
        self,
        provider_name: Literal["github", "google"],
        *,
        data: auth_one_tap_params.Variant0Data | auth_one_tap_params.Variant1Data,
        type: Literal["jwt"] | Literal["auth-code"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthOneTapResponse:
        if not provider_name:
            raise ValueError(f"Expected a non-empty value for `provider_name` but received {provider_name!r}")
        return await self._post(
            f"/api/v3/auth/{provider_name}/one-tap",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "type": type,
                },
                auth_one_tap_params.AuthOneTapParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthOneTapResponse,
        )

    async def retrieve_callback(
        self,
        provider_name: Literal["github", "google"],
        *,
        auth_code: str | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        error: str | NotGiven = NOT_GIVEN,
        error_description: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRetrieveCallbackResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_name:
            raise ValueError(f"Expected a non-empty value for `provider_name` but received {provider_name!r}")
        return await self._get(
            f"/api/v3/auth/{provider_name}/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "auth_code": auth_code,
                        "code": code,
                        "error": error,
                        "error_description": error_description,
                        "state": state,
                    },
                    auth_retrieve_callback_params.AuthRetrieveCallbackParams,
                ),
            ),
            cast_to=AuthRetrieveCallbackResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.login = to_raw_response_wrapper(
            auth.login,
        )
        self.one_tap = to_raw_response_wrapper(
            auth.one_tap,
        )
        self.retrieve_callback = to_raw_response_wrapper(
            auth.retrieve_callback,
        )

    @cached_property
    def magic_link(self) -> MagicLinkResourceWithRawResponse:
        return MagicLinkResourceWithRawResponse(self._auth.magic_link)

    @cached_property
    def session(self) -> SessionResourceWithRawResponse:
        return SessionResourceWithRawResponse(self._auth.session)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.login = async_to_raw_response_wrapper(
            auth.login,
        )
        self.one_tap = async_to_raw_response_wrapper(
            auth.one_tap,
        )
        self.retrieve_callback = async_to_raw_response_wrapper(
            auth.retrieve_callback,
        )

    @cached_property
    def magic_link(self) -> AsyncMagicLinkResourceWithRawResponse:
        return AsyncMagicLinkResourceWithRawResponse(self._auth.magic_link)

    @cached_property
    def session(self) -> AsyncSessionResourceWithRawResponse:
        return AsyncSessionResourceWithRawResponse(self._auth.session)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.login = to_streamed_response_wrapper(
            auth.login,
        )
        self.one_tap = to_streamed_response_wrapper(
            auth.one_tap,
        )
        self.retrieve_callback = to_streamed_response_wrapper(
            auth.retrieve_callback,
        )

    @cached_property
    def magic_link(self) -> MagicLinkResourceWithStreamingResponse:
        return MagicLinkResourceWithStreamingResponse(self._auth.magic_link)

    @cached_property
    def session(self) -> SessionResourceWithStreamingResponse:
        return SessionResourceWithStreamingResponse(self._auth.session)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.login = async_to_streamed_response_wrapper(
            auth.login,
        )
        self.one_tap = async_to_streamed_response_wrapper(
            auth.one_tap,
        )
        self.retrieve_callback = async_to_streamed_response_wrapper(
            auth.retrieve_callback,
        )

    @cached_property
    def magic_link(self) -> AsyncMagicLinkResourceWithStreamingResponse:
        return AsyncMagicLinkResourceWithStreamingResponse(self._auth.magic_link)

    @cached_property
    def session(self) -> AsyncSessionResourceWithStreamingResponse:
        return AsyncSessionResourceWithStreamingResponse(self._auth.session)
