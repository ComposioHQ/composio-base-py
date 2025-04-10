# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_sdk import ComposioSDK, AsyncComposioSDK
from composio_sdk.types import (
    AuthOneTapResponse,
    AuthRetrieveCallbackResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_method_login(self, client: ComposioSDK) -> None:
        auth = client.auth.login(
            provider_name="provider_name",
        )
        assert auth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_method_login_with_all_params(self, client: ComposioSDK) -> None:
        auth = client.auth.login(
            provider_name="provider_name",
            redirect_uri="redirectUri",
        )
        assert auth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_raw_response_login(self, client: ComposioSDK) -> None:
        response = client.auth.with_raw_response.login(
            provider_name="provider_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_streaming_response_login(self, client: ComposioSDK) -> None:
        with client.auth.with_streaming_response.login(
            provider_name="provider_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_path_params_login(self, client: ComposioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_name` but received ''"):
            client.auth.with_raw_response.login(
                provider_name="",
            )

    @parametrize
    def test_method_one_tap_overload_1(self, client: ComposioSDK) -> None:
        auth = client.auth.one_tap(
            provider_name="github",
            data={"jwt": "jwt"},
            type="jwt",
        )
        assert_matches_type(AuthOneTapResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_one_tap_overload_1(self, client: ComposioSDK) -> None:
        response = client.auth.with_raw_response.one_tap(
            provider_name="github",
            data={"jwt": "jwt"},
            type="jwt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthOneTapResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_one_tap_overload_1(self, client: ComposioSDK) -> None:
        with client.auth.with_streaming_response.one_tap(
            provider_name="github",
            data={"jwt": "jwt"},
            type="jwt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthOneTapResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_one_tap_overload_2(self, client: ComposioSDK) -> None:
        auth = client.auth.one_tap(
            provider_name="github",
            data={"auth_code": "authCode"},
            type="auth-code",
        )
        assert_matches_type(AuthOneTapResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_one_tap_overload_2(self, client: ComposioSDK) -> None:
        response = client.auth.with_raw_response.one_tap(
            provider_name="github",
            data={"auth_code": "authCode"},
            type="auth-code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthOneTapResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_one_tap_overload_2(self, client: ComposioSDK) -> None:
        with client.auth.with_streaming_response.one_tap(
            provider_name="github",
            data={"auth_code": "authCode"},
            type="auth-code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthOneTapResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_callback(self, client: ComposioSDK) -> None:
        auth = client.auth.retrieve_callback(
            provider_name="github",
        )
        assert_matches_type(AuthRetrieveCallbackResponse, auth, path=["response"])

    @parametrize
    def test_method_retrieve_callback_with_all_params(self, client: ComposioSDK) -> None:
        auth = client.auth.retrieve_callback(
            provider_name="github",
            auth_code="authCode",
            code="code",
            error="error",
            error_description="error_description",
            state="state",
        )
        assert_matches_type(AuthRetrieveCallbackResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_retrieve_callback(self, client: ComposioSDK) -> None:
        response = client.auth.with_raw_response.retrieve_callback(
            provider_name="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthRetrieveCallbackResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_callback(self, client: ComposioSDK) -> None:
        with client.auth.with_streaming_response.retrieve_callback(
            provider_name="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthRetrieveCallbackResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_method_login(self, async_client: AsyncComposioSDK) -> None:
        auth = await async_client.auth.login(
            provider_name="provider_name",
        )
        assert auth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_method_login_with_all_params(self, async_client: AsyncComposioSDK) -> None:
        auth = await async_client.auth.login(
            provider_name="provider_name",
            redirect_uri="redirectUri",
        )
        assert auth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_raw_response_login(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.auth.with_raw_response.login(
            provider_name="provider_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.auth.with_streaming_response.login(
            provider_name="provider_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_path_params_login(self, async_client: AsyncComposioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_name` but received ''"):
            await async_client.auth.with_raw_response.login(
                provider_name="",
            )

    @parametrize
    async def test_method_one_tap_overload_1(self, async_client: AsyncComposioSDK) -> None:
        auth = await async_client.auth.one_tap(
            provider_name="github",
            data={"jwt": "jwt"},
            type="jwt",
        )
        assert_matches_type(AuthOneTapResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_one_tap_overload_1(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.auth.with_raw_response.one_tap(
            provider_name="github",
            data={"jwt": "jwt"},
            type="jwt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthOneTapResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_one_tap_overload_1(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.auth.with_streaming_response.one_tap(
            provider_name="github",
            data={"jwt": "jwt"},
            type="jwt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthOneTapResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_one_tap_overload_2(self, async_client: AsyncComposioSDK) -> None:
        auth = await async_client.auth.one_tap(
            provider_name="github",
            data={"auth_code": "authCode"},
            type="auth-code",
        )
        assert_matches_type(AuthOneTapResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_one_tap_overload_2(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.auth.with_raw_response.one_tap(
            provider_name="github",
            data={"auth_code": "authCode"},
            type="auth-code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthOneTapResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_one_tap_overload_2(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.auth.with_streaming_response.one_tap(
            provider_name="github",
            data={"auth_code": "authCode"},
            type="auth-code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthOneTapResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_callback(self, async_client: AsyncComposioSDK) -> None:
        auth = await async_client.auth.retrieve_callback(
            provider_name="github",
        )
        assert_matches_type(AuthRetrieveCallbackResponse, auth, path=["response"])

    @parametrize
    async def test_method_retrieve_callback_with_all_params(self, async_client: AsyncComposioSDK) -> None:
        auth = await async_client.auth.retrieve_callback(
            provider_name="github",
            auth_code="authCode",
            code="code",
            error="error",
            error_description="error_description",
            state="state",
        )
        assert_matches_type(AuthRetrieveCallbackResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_callback(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.auth.with_raw_response.retrieve_callback(
            provider_name="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthRetrieveCallbackResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_callback(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.auth.with_streaming_response.retrieve_callback(
            provider_name="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthRetrieveCallbackResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
