# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    McpListResponse,
    McpCreateResponse,
    McpDeleteResponse,
    McpUpdateResponse,
    McpRetrieveResponse,
    McpRetrieveAppResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Composio) -> None:
        mcp = client.mcp.create(
            name="GitHub Integration Server",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Composio) -> None:
        mcp = client.mcp.create(
            name="GitHub Integration Server",
            allowed_tools=["github-issues", "github-repos", "github-pull-requests"],
            auth_config_id="auth_cfg_abc123def456",
            ttl="1d",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.create(
            name="GitHub Integration Server",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.create(
            name="GitHub Integration Server",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpCreateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        mcp = client.mcp.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mcp.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Composio) -> None:
        mcp = client.mcp.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Composio) -> None:
        mcp = client.mcp.update(
            id="550e8400-e29b-41d4-a716-446655440000",
            actions=["GMAIL_ADD_LABEL_TO_EMAIL"],
            apps=["gmail"],
            name="Updated GitHub Integration Server",
        )
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpUpdateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mcp.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_method_list(self, client: Composio) -> None:
        mcp = client.mcp.list()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        mcp = client.mcp.list(
            auth_config_id="auth_cfg_abc123def456",
            limit=10,
            name="github",
            page_no=1,
            toolkit="github",
        )
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpListResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Composio) -> None:
        mcp = client.mcp.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpDeleteResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mcp.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_retrieve_app(self, client: Composio) -> None:
        mcp = client.mcp.retrieve_app(
            app_key="github",
        )
        assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

    @parametrize
    def test_method_retrieve_app_with_all_params(self, client: Composio) -> None:
        mcp = client.mcp.retrieve_app(
            app_key="github",
            auth_config_id="auth_cfg_abc123def456",
            limit=10,
            name="github",
            page_no=1,
            toolkit="github",
        )
        assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_retrieve_app(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.retrieve_app(
            app_key="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_app(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.retrieve_app(
            app_key="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_app(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_key` but received ''"):
            client.mcp.with_raw_response.retrieve_app(
                app_key="",
            )


class TestAsyncMcp:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.create(
            name="GitHub Integration Server",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.create(
            name="GitHub Integration Server",
            allowed_tools=["github-issues", "github-repos", "github-pull-requests"],
            auth_config_id="auth_cfg_abc123def456",
            ttl="1d",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.create(
            name="GitHub Integration Server",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.create(
            name="GitHub Integration Server",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpCreateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mcp.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.update(
            id="550e8400-e29b-41d4-a716-446655440000",
            actions=["GMAIL_ADD_LABEL_TO_EMAIL"],
            apps=["gmail"],
            name="Updated GitHub Integration Server",
        )
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpUpdateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mcp.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.list()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.list(
            auth_config_id="auth_cfg_abc123def456",
            limit=10,
            name="github",
            page_no=1,
            toolkit="github",
        )
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpListResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpDeleteResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mcp.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_retrieve_app(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.retrieve_app(
            app_key="github",
        )
        assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

    @parametrize
    async def test_method_retrieve_app_with_all_params(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.retrieve_app(
            app_key="github",
            auth_config_id="auth_cfg_abc123def456",
            limit=10,
            name="github",
            page_no=1,
            toolkit="github",
        )
        assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_app(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.retrieve_app(
            app_key="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_app(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.retrieve_app(
            app_key="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_app(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_key` but received ''"):
            await async_client.mcp.with_raw_response.retrieve_app(
                app_key="",
            )
