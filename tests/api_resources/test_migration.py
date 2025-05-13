# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import MigrationRetrieveNanoidResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMigration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_nanoid(self, client: Composio) -> None:
        migration = client.migration.retrieve_nanoid(
            type="CONNECTED_ACCOUNT",
            uuid="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MigrationRetrieveNanoidResponse, migration, path=["response"])

    @parametrize
    def test_raw_response_retrieve_nanoid(self, client: Composio) -> None:
        response = client.migration.with_raw_response.retrieve_nanoid(
            type="CONNECTED_ACCOUNT",
            uuid="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationRetrieveNanoidResponse, migration, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_nanoid(self, client: Composio) -> None:
        with client.migration.with_streaming_response.retrieve_nanoid(
            type="CONNECTED_ACCOUNT",
            uuid="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = response.parse()
            assert_matches_type(MigrationRetrieveNanoidResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMigration:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve_nanoid(self, async_client: AsyncComposio) -> None:
        migration = await async_client.migration.retrieve_nanoid(
            type="CONNECTED_ACCOUNT",
            uuid="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MigrationRetrieveNanoidResponse, migration, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_nanoid(self, async_client: AsyncComposio) -> None:
        response = await async_client.migration.with_raw_response.retrieve_nanoid(
            type="CONNECTED_ACCOUNT",
            uuid="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = await response.parse()
        assert_matches_type(MigrationRetrieveNanoidResponse, migration, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_nanoid(self, async_client: AsyncComposio) -> None:
        async with async_client.migration.with_streaming_response.retrieve_nanoid(
            type="CONNECTED_ACCOUNT",
            uuid="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = await response.parse()
            assert_matches_type(MigrationRetrieveNanoidResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True
