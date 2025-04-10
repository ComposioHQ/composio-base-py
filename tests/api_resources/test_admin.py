# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_sdk import ComposioSDK, AsyncComposioSDK
from composio_sdk.types import AdminIdentifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_identify(self, client: ComposioSDK) -> None:
        admin = client.admin.identify(
            hash="hash",
        )
        assert_matches_type(AdminIdentifyResponse, admin, path=["response"])

    @parametrize
    def test_method_identify_with_all_params(self, client: ComposioSDK) -> None:
        admin = client.admin.identify(
            hash="hash",
            admin_token="adminToken",
        )
        assert_matches_type(AdminIdentifyResponse, admin, path=["response"])

    @parametrize
    def test_raw_response_identify(self, client: ComposioSDK) -> None:
        response = client.admin.with_raw_response.identify(
            hash="hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminIdentifyResponse, admin, path=["response"])

    @parametrize
    def test_streaming_response_identify(self, client: ComposioSDK) -> None:
        with client.admin.with_streaming_response.identify(
            hash="hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminIdentifyResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_identify(self, async_client: AsyncComposioSDK) -> None:
        admin = await async_client.admin.identify(
            hash="hash",
        )
        assert_matches_type(AdminIdentifyResponse, admin, path=["response"])

    @parametrize
    async def test_method_identify_with_all_params(self, async_client: AsyncComposioSDK) -> None:
        admin = await async_client.admin.identify(
            hash="hash",
            admin_token="adminToken",
        )
        assert_matches_type(AdminIdentifyResponse, admin, path=["response"])

    @parametrize
    async def test_raw_response_identify(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.admin.with_raw_response.identify(
            hash="hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminIdentifyResponse, admin, path=["response"])

    @parametrize
    async def test_streaming_response_identify(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.admin.with_streaming_response.identify(
            hash="hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminIdentifyResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True
