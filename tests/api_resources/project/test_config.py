# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.project import ConfigUpdateResponse, ConfigRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        config = client.project.config.retrieve()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.project.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.project.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Composio) -> None:
        config = client.project.config.update()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Composio) -> None:
        config = client.project.config.update(
            display_name="display_name",
            is_2_fa_enabled=True,
            is_composio_link_enabled_for_managed_auth=True,
            log_visibility_setting="show_all",
            logo_url="logo_url",
            mask_secret_keys_in_connected_account=True,
            require_mcp_api_key=True,
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Composio) -> None:
        response = client.project.config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Composio) -> None:
        with client.project.config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        config = await async_client.project.config.retrieve()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.project.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.project.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncComposio) -> None:
        config = await async_client.project.config.update()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncComposio) -> None:
        config = await async_client.project.config.update(
            display_name="display_name",
            is_2_fa_enabled=True,
            is_composio_link_enabled_for_managed_auth=True,
            log_visibility_setting="show_all",
            logo_url="logo_url",
            mask_secret_keys_in_connected_account=True,
            require_mcp_api_key=True,
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncComposio) -> None:
        response = await async_client.project.config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncComposio) -> None:
        async with async_client.project.config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True
