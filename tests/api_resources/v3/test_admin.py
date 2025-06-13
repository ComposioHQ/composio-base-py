# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.v3 import AdminRefreshAuthTokensResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_refresh_auth_tokens(self, client: Composio) -> None:
        admin = client.v3.admin.refresh_auth_tokens(
            connection_ids=["conn_123abc", "conn_456def"],
            x_composio_admin_token="adm_123456789abcdef",
        )
        assert_matches_type(AdminRefreshAuthTokensResponse, admin, path=["response"])

    @parametrize
    def test_method_refresh_auth_tokens_with_all_params(self, client: Composio) -> None:
        admin = client.v3.admin.refresh_auth_tokens(
            connection_ids=["conn_123abc", "conn_456def"],
            x_composio_admin_token="adm_123456789abcdef",
            parallelism=5,
        )
        assert_matches_type(AdminRefreshAuthTokensResponse, admin, path=["response"])

    @parametrize
    def test_raw_response_refresh_auth_tokens(self, client: Composio) -> None:
        response = client.v3.admin.with_raw_response.refresh_auth_tokens(
            connection_ids=["conn_123abc", "conn_456def"],
            x_composio_admin_token="adm_123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminRefreshAuthTokensResponse, admin, path=["response"])

    @parametrize
    def test_streaming_response_refresh_auth_tokens(self, client: Composio) -> None:
        with client.v3.admin.with_streaming_response.refresh_auth_tokens(
            connection_ids=["conn_123abc", "conn_456def"],
            x_composio_admin_token="adm_123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminRefreshAuthTokensResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_refresh_auth_tokens(self, async_client: AsyncComposio) -> None:
        admin = await async_client.v3.admin.refresh_auth_tokens(
            connection_ids=["conn_123abc", "conn_456def"],
            x_composio_admin_token="adm_123456789abcdef",
        )
        assert_matches_type(AdminRefreshAuthTokensResponse, admin, path=["response"])

    @parametrize
    async def test_method_refresh_auth_tokens_with_all_params(self, async_client: AsyncComposio) -> None:
        admin = await async_client.v3.admin.refresh_auth_tokens(
            connection_ids=["conn_123abc", "conn_456def"],
            x_composio_admin_token="adm_123456789abcdef",
            parallelism=5,
        )
        assert_matches_type(AdminRefreshAuthTokensResponse, admin, path=["response"])

    @parametrize
    async def test_raw_response_refresh_auth_tokens(self, async_client: AsyncComposio) -> None:
        response = await async_client.v3.admin.with_raw_response.refresh_auth_tokens(
            connection_ids=["conn_123abc", "conn_456def"],
            x_composio_admin_token="adm_123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminRefreshAuthTokensResponse, admin, path=["response"])

    @parametrize
    async def test_streaming_response_refresh_auth_tokens(self, async_client: AsyncComposio) -> None:
        async with async_client.v3.admin.with_streaming_response.refresh_auth_tokens(
            connection_ids=["conn_123abc", "conn_456def"],
            x_composio_admin_token="adm_123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminRefreshAuthTokensResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True
