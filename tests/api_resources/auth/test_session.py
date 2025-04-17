# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.auth import SessionGetInfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_info(self, client: Composio) -> None:
        session = client.auth.session.get_info()
        assert_matches_type(SessionGetInfoResponse, session, path=["response"])

    @parametrize
    def test_raw_response_get_info(self, client: Composio) -> None:
        response = client.auth.session.with_raw_response.get_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetInfoResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_get_info(self, client: Composio) -> None:
        with client.auth.session.with_streaming_response.get_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetInfoResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSession:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_info(self, async_client: AsyncComposio) -> None:
        session = await async_client.auth.session.get_info()
        assert_matches_type(SessionGetInfoResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_get_info(self, async_client: AsyncComposio) -> None:
        response = await async_client.auth.session.with_raw_response.get_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetInfoResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_get_info(self, async_client: AsyncComposio) -> None:
        async with async_client.auth.session.with_streaming_response.get_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetInfoResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True
