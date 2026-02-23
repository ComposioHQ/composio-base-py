# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.cli import RealtimeAuthResponse, RealtimeCredentialsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRealtime:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_auth(self, client: Composio) -> None:
        realtime = client.cli.realtime.auth(
            channel_name="channel_name",
            socket_id="socket_id",
        )
        assert_matches_type(RealtimeAuthResponse, realtime, path=["response"])

    @parametrize
    def test_raw_response_auth(self, client: Composio) -> None:
        response = client.cli.realtime.with_raw_response.auth(
            channel_name="channel_name",
            socket_id="socket_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        realtime = response.parse()
        assert_matches_type(RealtimeAuthResponse, realtime, path=["response"])

    @parametrize
    def test_streaming_response_auth(self, client: Composio) -> None:
        with client.cli.realtime.with_streaming_response.auth(
            channel_name="channel_name",
            socket_id="socket_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            realtime = response.parse()
            assert_matches_type(RealtimeAuthResponse, realtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_credentials(self, client: Composio) -> None:
        realtime = client.cli.realtime.credentials()
        assert_matches_type(RealtimeCredentialsResponse, realtime, path=["response"])

    @parametrize
    def test_raw_response_credentials(self, client: Composio) -> None:
        response = client.cli.realtime.with_raw_response.credentials()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        realtime = response.parse()
        assert_matches_type(RealtimeCredentialsResponse, realtime, path=["response"])

    @parametrize
    def test_streaming_response_credentials(self, client: Composio) -> None:
        with client.cli.realtime.with_streaming_response.credentials() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            realtime = response.parse()
            assert_matches_type(RealtimeCredentialsResponse, realtime, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRealtime:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_auth(self, async_client: AsyncComposio) -> None:
        realtime = await async_client.cli.realtime.auth(
            channel_name="channel_name",
            socket_id="socket_id",
        )
        assert_matches_type(RealtimeAuthResponse, realtime, path=["response"])

    @parametrize
    async def test_raw_response_auth(self, async_client: AsyncComposio) -> None:
        response = await async_client.cli.realtime.with_raw_response.auth(
            channel_name="channel_name",
            socket_id="socket_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        realtime = await response.parse()
        assert_matches_type(RealtimeAuthResponse, realtime, path=["response"])

    @parametrize
    async def test_streaming_response_auth(self, async_client: AsyncComposio) -> None:
        async with async_client.cli.realtime.with_streaming_response.auth(
            channel_name="channel_name",
            socket_id="socket_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            realtime = await response.parse()
            assert_matches_type(RealtimeAuthResponse, realtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_credentials(self, async_client: AsyncComposio) -> None:
        realtime = await async_client.cli.realtime.credentials()
        assert_matches_type(RealtimeCredentialsResponse, realtime, path=["response"])

    @parametrize
    async def test_raw_response_credentials(self, async_client: AsyncComposio) -> None:
        response = await async_client.cli.realtime.with_raw_response.credentials()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        realtime = await response.parse()
        assert_matches_type(RealtimeCredentialsResponse, realtime, path=["response"])

    @parametrize
    async def test_streaming_response_credentials(self, async_client: AsyncComposio) -> None:
        async with async_client.cli.realtime.with_streaming_response.credentials() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            realtime = await response.parse()
            assert_matches_type(RealtimeCredentialsResponse, realtime, path=["response"])

        assert cast(Any, response.is_closed) is True
