# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.mcp import GenerateURLResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_url(self, client: Composio) -> None:
        generate = client.mcp.generate.url(
            mcp_server_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(GenerateURLResponse, generate, path=["response"])

    @parametrize
    def test_method_url_with_all_params(self, client: Composio) -> None:
        generate = client.mcp.generate.url(
            mcp_server_id="550e8400-e29b-41d4-a716-446655440000",
            connected_account_ids=["account_1", "account_2"],
            managed_auth_by_composio=True,
            user_ids=["user_123456"],
        )
        assert_matches_type(GenerateURLResponse, generate, path=["response"])

    @parametrize
    def test_raw_response_url(self, client: Composio) -> None:
        response = client.mcp.generate.with_raw_response.url(
            mcp_server_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(GenerateURLResponse, generate, path=["response"])

    @parametrize
    def test_streaming_response_url(self, client: Composio) -> None:
        with client.mcp.generate.with_streaming_response.url(
            mcp_server_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(GenerateURLResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_url(self, async_client: AsyncComposio) -> None:
        generate = await async_client.mcp.generate.url(
            mcp_server_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(GenerateURLResponse, generate, path=["response"])

    @parametrize
    async def test_method_url_with_all_params(self, async_client: AsyncComposio) -> None:
        generate = await async_client.mcp.generate.url(
            mcp_server_id="550e8400-e29b-41d4-a716-446655440000",
            connected_account_ids=["account_1", "account_2"],
            managed_auth_by_composio=True,
            user_ids=["user_123456"],
        )
        assert_matches_type(GenerateURLResponse, generate, path=["response"])

    @parametrize
    async def test_raw_response_url(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.generate.with_raw_response.url(
            mcp_server_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(GenerateURLResponse, generate, path=["response"])

    @parametrize
    async def test_streaming_response_url(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.generate.with_streaming_response.url(
            mcp_server_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(GenerateURLResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True
