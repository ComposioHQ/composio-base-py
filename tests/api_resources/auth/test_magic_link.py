# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_sdk import ComposioSDK, AsyncComposioSDK
from composio_sdk.types.auth import (
    MagicLinkSendResponse,
    MagicLinkVerifyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMagicLink:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_send(self, client: ComposioSDK) -> None:
        magic_link = client.auth.magic_link.send(
            email="dev@stainless.com",
        )
        assert_matches_type(MagicLinkSendResponse, magic_link, path=["response"])

    @parametrize
    def test_method_send_with_all_params(self, client: ComposioSDK) -> None:
        magic_link = client.auth.magic_link.send(
            email="dev@stainless.com",
            verify_host="verifyHost",
        )
        assert_matches_type(MagicLinkSendResponse, magic_link, path=["response"])

    @parametrize
    def test_raw_response_send(self, client: ComposioSDK) -> None:
        response = client.auth.magic_link.with_raw_response.send(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magic_link = response.parse()
        assert_matches_type(MagicLinkSendResponse, magic_link, path=["response"])

    @parametrize
    def test_streaming_response_send(self, client: ComposioSDK) -> None:
        with client.auth.magic_link.with_streaming_response.send(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magic_link = response.parse()
            assert_matches_type(MagicLinkSendResponse, magic_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_verify(self, client: ComposioSDK) -> None:
        magic_link = client.auth.magic_link.verify(
            token="token",
        )
        assert_matches_type(MagicLinkVerifyResponse, magic_link, path=["response"])

    @parametrize
    def test_raw_response_verify(self, client: ComposioSDK) -> None:
        response = client.auth.magic_link.with_raw_response.verify(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magic_link = response.parse()
        assert_matches_type(MagicLinkVerifyResponse, magic_link, path=["response"])

    @parametrize
    def test_streaming_response_verify(self, client: ComposioSDK) -> None:
        with client.auth.magic_link.with_streaming_response.verify(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magic_link = response.parse()
            assert_matches_type(MagicLinkVerifyResponse, magic_link, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMagicLink:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_send(self, async_client: AsyncComposioSDK) -> None:
        magic_link = await async_client.auth.magic_link.send(
            email="dev@stainless.com",
        )
        assert_matches_type(MagicLinkSendResponse, magic_link, path=["response"])

    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncComposioSDK) -> None:
        magic_link = await async_client.auth.magic_link.send(
            email="dev@stainless.com",
            verify_host="verifyHost",
        )
        assert_matches_type(MagicLinkSendResponse, magic_link, path=["response"])

    @parametrize
    async def test_raw_response_send(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.auth.magic_link.with_raw_response.send(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magic_link = await response.parse()
        assert_matches_type(MagicLinkSendResponse, magic_link, path=["response"])

    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.auth.magic_link.with_streaming_response.send(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magic_link = await response.parse()
            assert_matches_type(MagicLinkSendResponse, magic_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_verify(self, async_client: AsyncComposioSDK) -> None:
        magic_link = await async_client.auth.magic_link.verify(
            token="token",
        )
        assert_matches_type(MagicLinkVerifyResponse, magic_link, path=["response"])

    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.auth.magic_link.with_raw_response.verify(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magic_link = await response.parse()
        assert_matches_type(MagicLinkVerifyResponse, magic_link, path=["response"])

    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.auth.magic_link.with_streaming_response.verify(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magic_link = await response.parse()
            assert_matches_type(MagicLinkVerifyResponse, magic_link, path=["response"])

        assert cast(Any, response.is_closed) is True
