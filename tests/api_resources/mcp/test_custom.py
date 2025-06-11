# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.mcp import CustomCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Composio) -> None:
        custom = client.mcp.custom.create(
            name="name",
            toolkits=["github", "jira"],
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Composio) -> None:
        custom = client.mcp.custom.create(
            name="name",
            toolkits=["github", "jira"],
            custom_tools=["custom-api-tool", "internal-database-tool"],
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Composio) -> None:
        response = client.mcp.custom.with_raw_response.create(
            name="name",
            toolkits=["github", "jira"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Composio) -> None:
        with client.mcp.custom.with_streaming_response.create(
            name="name",
            toolkits=["github", "jira"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomCreateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustom:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncComposio) -> None:
        custom = await async_client.mcp.custom.create(
            name="name",
            toolkits=["github", "jira"],
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncComposio) -> None:
        custom = await async_client.mcp.custom.create(
            name="name",
            toolkits=["github", "jira"],
            custom_tools=["custom-api-tool", "internal-database-tool"],
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.custom.with_raw_response.create(
            name="name",
            toolkits=["github", "jira"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.custom.with_streaming_response.create(
            name="name",
            toolkits=["github", "jira"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomCreateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True
