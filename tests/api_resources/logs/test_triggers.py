# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.logs import TriggerListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTriggers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        trigger = client.logs.triggers.list()
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        trigger = client.logs.triggers.list(
            cursor="cursor",
            entity_id="entityId",
            from_=0,
            include_payload=True,
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            search="search",
            search_params=[
                {
                    "field": "field",
                    "operation": "operation",
                    "value": "value",
                }
            ],
            status="success",
            time="5m",
            to=0,
            user_id="userId",
        )
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.logs.triggers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.logs.triggers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert_matches_type(TriggerListResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTriggers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        trigger = await async_client.logs.triggers.list()
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        trigger = await async_client.logs.triggers.list(
            cursor="cursor",
            entity_id="entityId",
            from_=0,
            include_payload=True,
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            search="search",
            search_params=[
                {
                    "field": "field",
                    "operation": "operation",
                    "value": "value",
                }
            ],
            status="success",
            time="5m",
            to=0,
            user_id="userId",
        )
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.logs.triggers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.logs.triggers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert_matches_type(TriggerListResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True
