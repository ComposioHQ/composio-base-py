# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import TriggerLogResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrigger:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_log(self, client: Composio) -> None:
        trigger = client.trigger.log(
            cursor="cursor",
        )
        assert_matches_type(TriggerLogResponse, trigger, path=["response"])

    @parametrize
    def test_method_log_with_all_params(self, client: Composio) -> None:
        trigger = client.trigger.log(
            cursor="cursor",
            entity_id="entityId",
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            search="search",
            status="success",
            time="5m",
        )
        assert_matches_type(TriggerLogResponse, trigger, path=["response"])

    @parametrize
    def test_raw_response_log(self, client: Composio) -> None:
        response = client.trigger.with_raw_response.log(
            cursor="cursor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert_matches_type(TriggerLogResponse, trigger, path=["response"])

    @parametrize
    def test_streaming_response_log(self, client: Composio) -> None:
        with client.trigger.with_streaming_response.log(
            cursor="cursor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert_matches_type(TriggerLogResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrigger:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_log(self, async_client: AsyncComposio) -> None:
        trigger = await async_client.trigger.log(
            cursor="cursor",
        )
        assert_matches_type(TriggerLogResponse, trigger, path=["response"])

    @parametrize
    async def test_method_log_with_all_params(self, async_client: AsyncComposio) -> None:
        trigger = await async_client.trigger.log(
            cursor="cursor",
            entity_id="entityId",
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            search="search",
            status="success",
            time="5m",
        )
        assert_matches_type(TriggerLogResponse, trigger, path=["response"])

    @parametrize
    async def test_raw_response_log(self, async_client: AsyncComposio) -> None:
        response = await async_client.trigger.with_raw_response.log(
            cursor="cursor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert_matches_type(TriggerLogResponse, trigger, path=["response"])

    @parametrize
    async def test_streaming_response_log(self, async_client: AsyncComposio) -> None:
        async with async_client.trigger.with_streaming_response.log(
            cursor="cursor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert_matches_type(TriggerLogResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True
