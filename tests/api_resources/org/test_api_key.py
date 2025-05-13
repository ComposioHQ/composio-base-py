# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.org import APIKeyRetrieveResponse, APIKeyRegenerateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        api_key = client.org.api_key.retrieve()
        assert_matches_type(APIKeyRetrieveResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.org.api_key.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyRetrieveResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.org.api_key.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyRetrieveResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_regenerate(self, client: Composio) -> None:
        api_key = client.org.api_key.regenerate()
        assert_matches_type(APIKeyRegenerateResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_regenerate(self, client: Composio) -> None:
        response = client.org.api_key.with_raw_response.regenerate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyRegenerateResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_regenerate(self, client: Composio) -> None:
        with client.org.api_key.with_streaming_response.regenerate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyRegenerateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIKey:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        api_key = await async_client.org.api_key.retrieve()
        assert_matches_type(APIKeyRetrieveResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.api_key.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyRetrieveResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.org.api_key.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyRetrieveResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_regenerate(self, async_client: AsyncComposio) -> None:
        api_key = await async_client.org.api_key.regenerate()
        assert_matches_type(APIKeyRegenerateResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_regenerate(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.api_key.with_raw_response.regenerate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyRegenerateResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_regenerate(self, async_client: AsyncComposio) -> None:
        async with async_client.org.api_key.with_streaming_response.regenerate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyRegenerateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True
