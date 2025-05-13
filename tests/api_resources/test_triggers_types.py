# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    TriggersTypeListResponse,
    TriggersTypeRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTriggersTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        triggers_type = client.triggers_types.retrieve(
            "slug",
        )
        assert_matches_type(TriggersTypeRetrieveResponse, triggers_type, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.triggers_types.with_raw_response.retrieve(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggers_type = response.parse()
        assert_matches_type(TriggersTypeRetrieveResponse, triggers_type, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.triggers_types.with_streaming_response.retrieve(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggers_type = response.parse()
            assert_matches_type(TriggersTypeRetrieveResponse, triggers_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.triggers_types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        triggers_type = client.triggers_types.list()
        assert_matches_type(TriggersTypeListResponse, triggers_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        triggers_type = client.triggers_types.list(
            cursor="cursor",
            limit=0,
            toolkit_slugs="toolkit_slugs",
        )
        assert_matches_type(TriggersTypeListResponse, triggers_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.triggers_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggers_type = response.parse()
        assert_matches_type(TriggersTypeListResponse, triggers_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.triggers_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggers_type = response.parse()
            assert_matches_type(TriggersTypeListResponse, triggers_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_enum(self, client: Composio) -> None:
        triggers_type = client.triggers_types.retrieve_enum()
        assert_matches_type(str, triggers_type, path=["response"])

    @parametrize
    def test_raw_response_retrieve_enum(self, client: Composio) -> None:
        response = client.triggers_types.with_raw_response.retrieve_enum()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggers_type = response.parse()
        assert_matches_type(str, triggers_type, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_enum(self, client: Composio) -> None:
        with client.triggers_types.with_streaming_response.retrieve_enum() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggers_type = response.parse()
            assert_matches_type(str, triggers_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTriggersTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        triggers_type = await async_client.triggers_types.retrieve(
            "slug",
        )
        assert_matches_type(TriggersTypeRetrieveResponse, triggers_type, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.triggers_types.with_raw_response.retrieve(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggers_type = await response.parse()
        assert_matches_type(TriggersTypeRetrieveResponse, triggers_type, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.triggers_types.with_streaming_response.retrieve(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggers_type = await response.parse()
            assert_matches_type(TriggersTypeRetrieveResponse, triggers_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.triggers_types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        triggers_type = await async_client.triggers_types.list()
        assert_matches_type(TriggersTypeListResponse, triggers_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        triggers_type = await async_client.triggers_types.list(
            cursor="cursor",
            limit=0,
            toolkit_slugs="toolkit_slugs",
        )
        assert_matches_type(TriggersTypeListResponse, triggers_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.triggers_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggers_type = await response.parse()
        assert_matches_type(TriggersTypeListResponse, triggers_type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.triggers_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggers_type = await response.parse()
            assert_matches_type(TriggersTypeListResponse, triggers_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_enum(self, async_client: AsyncComposio) -> None:
        triggers_type = await async_client.triggers_types.retrieve_enum()
        assert_matches_type(str, triggers_type, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_enum(self, async_client: AsyncComposio) -> None:
        response = await async_client.triggers_types.with_raw_response.retrieve_enum()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggers_type = await response.parse()
        assert_matches_type(str, triggers_type, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_enum(self, async_client: AsyncComposio) -> None:
        async with async_client.triggers_types.with_streaming_response.retrieve_enum() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggers_type = await response.parse()
            assert_matches_type(str, triggers_type, path=["response"])

        assert cast(Any, response.is_closed) is True
