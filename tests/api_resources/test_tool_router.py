# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import ToolRouterCreateSessionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToolRouter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_session(self, client: Composio) -> None:
        tool_router = client.tool_router.create_session(
            user_id="user_123456789",
        )
        assert_matches_type(ToolRouterCreateSessionResponse, tool_router, path=["response"])

    @parametrize
    def test_method_create_session_with_all_params(self, client: Composio) -> None:
        tool_router = client.tool_router.create_session(
            user_id="user_123456789",
            config={
                "manually_manage_connections": False,
                "toolkits": [
                    {
                        "toolkit": "gmail",
                        "auth_config_id": "auth_config_123",
                    },
                    {
                        "toolkit": "slack",
                        "auth_config_id": "auth_config_456",
                    },
                    {
                        "toolkit": "github",
                        "auth_config_id": "auth_config_123",
                    },
                ],
            },
        )
        assert_matches_type(ToolRouterCreateSessionResponse, tool_router, path=["response"])

    @parametrize
    def test_raw_response_create_session(self, client: Composio) -> None:
        response = client.tool_router.with_raw_response.create_session(
            user_id="user_123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_router = response.parse()
        assert_matches_type(ToolRouterCreateSessionResponse, tool_router, path=["response"])

    @parametrize
    def test_streaming_response_create_session(self, client: Composio) -> None:
        with client.tool_router.with_streaming_response.create_session(
            user_id="user_123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_router = response.parse()
            assert_matches_type(ToolRouterCreateSessionResponse, tool_router, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncToolRouter:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_session(self, async_client: AsyncComposio) -> None:
        tool_router = await async_client.tool_router.create_session(
            user_id="user_123456789",
        )
        assert_matches_type(ToolRouterCreateSessionResponse, tool_router, path=["response"])

    @parametrize
    async def test_method_create_session_with_all_params(self, async_client: AsyncComposio) -> None:
        tool_router = await async_client.tool_router.create_session(
            user_id="user_123456789",
            config={
                "manually_manage_connections": False,
                "toolkits": [
                    {
                        "toolkit": "gmail",
                        "auth_config_id": "auth_config_123",
                    },
                    {
                        "toolkit": "slack",
                        "auth_config_id": "auth_config_456",
                    },
                    {
                        "toolkit": "github",
                        "auth_config_id": "auth_config_123",
                    },
                ],
            },
        )
        assert_matches_type(ToolRouterCreateSessionResponse, tool_router, path=["response"])

    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncComposio) -> None:
        response = await async_client.tool_router.with_raw_response.create_session(
            user_id="user_123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_router = await response.parse()
        assert_matches_type(ToolRouterCreateSessionResponse, tool_router, path=["response"])

    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncComposio) -> None:
        async with async_client.tool_router.with_streaming_response.create_session(
            user_id="user_123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_router = await response.parse()
            assert_matches_type(ToolRouterCreateSessionResponse, tool_router, path=["response"])

        assert cast(Any, response.is_closed) is True
