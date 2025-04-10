# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_sdk import ComposioSDK, AsyncComposioSDK
from composio_sdk.types import ToolListResponse, ToolRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: ComposioSDK) -> None:
        tool = client.tools.retrieve(
            "tool_slug",
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ComposioSDK) -> None:
        response = client.tools.with_raw_response.retrieve(
            "tool_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ComposioSDK) -> None:
        with client.tools.with_streaming_response.retrieve(
            "tool_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ComposioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_slug` but received ''"):
            client.tools.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: ComposioSDK) -> None:
        tool = client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ComposioSDK) -> None:
        tool = client.tools.list(
            cursor="1",
            important="true",
            limit="20",
            search="github actions",
            toolkit_slug="github",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ComposioSDK) -> None:
        response = client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ComposioSDK) -> None:
        with client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_enum(self, client: ComposioSDK) -> None:
        tool = client.tools.retrieve_enum()
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    def test_raw_response_retrieve_enum(self, client: ComposioSDK) -> None:
        response = client.tools.with_raw_response.retrieve_enum()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_enum(self, client: ComposioSDK) -> None:
        with client.tools.with_streaming_response.retrieve_enum() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(str, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposioSDK) -> None:
        tool = await async_client.tools.retrieve(
            "tool_slug",
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.tools.with_raw_response.retrieve(
            "tool_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.tools.with_streaming_response.retrieve(
            "tool_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_slug` but received ''"):
            await async_client.tools.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposioSDK) -> None:
        tool = await async_client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposioSDK) -> None:
        tool = await async_client.tools.list(
            cursor="1",
            important="true",
            limit="20",
            search="github actions",
            toolkit_slug="github",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_enum(self, async_client: AsyncComposioSDK) -> None:
        tool = await async_client.tools.retrieve_enum()
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_enum(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.tools.with_raw_response.retrieve_enum()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_enum(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.tools.with_streaming_response.retrieve_enum() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(str, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
