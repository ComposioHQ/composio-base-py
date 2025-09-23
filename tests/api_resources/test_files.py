# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import FileListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        file = client.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        file = client.files.list(
            cursor="cursor",
            limit=0,
            tool_slug="tool_slug",
            toolkit_slug="toolkit_slug",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        file = await async_client.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        file = await async_client.files.list(
            cursor="cursor",
            limit=0,
            tool_slug="tool_slug",
            toolkit_slug="toolkit_slug",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
