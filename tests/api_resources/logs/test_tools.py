# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.logs import ToolListResponse, ToolRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        tool = client.logs.tools.retrieve(
            cursor=0,
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Composio) -> None:
        tool = client.logs.tools.retrieve(
            cursor=0,
            case_sensitive=True,
            from_=0,
            limit=0,
            search_params=[
                {
                    "field": "field",
                    "operation": "operation",
                    "value": "value",
                }
            ],
            to=0,
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.logs.tools.with_raw_response.retrieve(
            cursor=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.logs.tools.with_streaming_response.retrieve(
            cursor=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        tool = client.logs.tools.list(
            cursor=0,
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        tool = client.logs.tools.list(
            cursor=0,
            case_sensitive=True,
            from_=0,
            limit=0,
            search_params=[
                {
                    "field": "field",
                    "operation": "operation",
                    "value": "value",
                }
            ],
            to=0,
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.logs.tools.with_raw_response.list(
            cursor=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.logs.tools.with_streaming_response.list(
            cursor=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        tool = await async_client.logs.tools.retrieve(
            cursor=0,
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncComposio) -> None:
        tool = await async_client.logs.tools.retrieve(
            cursor=0,
            case_sensitive=True,
            from_=0,
            limit=0,
            search_params=[
                {
                    "field": "field",
                    "operation": "operation",
                    "value": "value",
                }
            ],
            to=0,
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.logs.tools.with_raw_response.retrieve(
            cursor=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.logs.tools.with_streaming_response.retrieve(
            cursor=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        tool = await async_client.logs.tools.list(
            cursor=0,
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        tool = await async_client.logs.tools.list(
            cursor=0,
            case_sensitive=True,
            from_=0,
            limit=0,
            search_params=[
                {
                    "field": "field",
                    "operation": "operation",
                    "value": "value",
                }
            ],
            to=0,
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.logs.tools.with_raw_response.list(
            cursor=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.logs.tools.with_streaming_response.list(
            cursor=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
