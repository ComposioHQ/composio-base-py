# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.mcp import CommandGenerateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommand:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate(self, client: Composio) -> None:
        command = client.mcp.command.generate(
            id="id",
            mcp_client="cursor",
        )
        assert_matches_type(CommandGenerateResponse, command, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: Composio) -> None:
        command = client.mcp.command.generate(
            id="id",
            mcp_client="cursor",
            ttl="1d",
        )
        assert_matches_type(CommandGenerateResponse, command, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Composio) -> None:
        response = client.mcp.command.with_raw_response.generate(
            id="id",
            mcp_client="cursor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(CommandGenerateResponse, command, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Composio) -> None:
        with client.mcp.command.with_streaming_response.generate(
            id="id",
            mcp_client="cursor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(CommandGenerateResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCommand:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_generate(self, async_client: AsyncComposio) -> None:
        command = await async_client.mcp.command.generate(
            id="id",
            mcp_client="cursor",
        )
        assert_matches_type(CommandGenerateResponse, command, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncComposio) -> None:
        command = await async_client.mcp.command.generate(
            id="id",
            mcp_client="cursor",
            ttl="1d",
        )
        assert_matches_type(CommandGenerateResponse, command, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.command.with_raw_response.generate(
            id="id",
            mcp_client="cursor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(CommandGenerateResponse, command, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.command.with_streaming_response.generate(
            id="id",
            mcp_client="cursor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(CommandGenerateResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True
