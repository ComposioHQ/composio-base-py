# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    LinkCreateResponse,
    LinkSubmitResponse,
    LinkRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLink:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Composio) -> None:
        link = client.link.create(
            auth_config_id="auth_config_id",
            user_id="x",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Composio) -> None:
        link = client.link.create(
            auth_config_id="auth_config_id",
            user_id="x",
            callback_url="callback_url",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Composio) -> None:
        response = client.link.with_raw_response.create(
            auth_config_id="auth_config_id",
            user_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Composio) -> None:
        with client.link.with_streaming_response.create(
            auth_config_id="auth_config_id",
            user_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkCreateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        link = client.link.retrieve(
            "token",
        )
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.link.with_raw_response.retrieve(
            "token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.link.with_streaming_response.retrieve(
            "token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkRetrieveResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.link.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_submit(self, client: Composio) -> None:
        link = client.link.submit(
            token="token",
            input={"foo": "bar"},
        )
        assert_matches_type(LinkSubmitResponse, link, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: Composio) -> None:
        response = client.link.with_raw_response.submit(
            token="token",
            input={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkSubmitResponse, link, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: Composio) -> None:
        with client.link.with_streaming_response.submit(
            token="token",
            input={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkSubmitResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.link.with_raw_response.submit(
                token="",
                input={"foo": "bar"},
            )


class TestAsyncLink:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncComposio) -> None:
        link = await async_client.link.create(
            auth_config_id="auth_config_id",
            user_id="x",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncComposio) -> None:
        link = await async_client.link.create(
            auth_config_id="auth_config_id",
            user_id="x",
            callback_url="callback_url",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncComposio) -> None:
        response = await async_client.link.with_raw_response.create(
            auth_config_id="auth_config_id",
            user_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncComposio) -> None:
        async with async_client.link.with_streaming_response.create(
            auth_config_id="auth_config_id",
            user_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkCreateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        link = await async_client.link.retrieve(
            "token",
        )
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.link.with_raw_response.retrieve(
            "token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.link.with_streaming_response.retrieve(
            "token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkRetrieveResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.link.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_submit(self, async_client: AsyncComposio) -> None:
        link = await async_client.link.submit(
            token="token",
            input={"foo": "bar"},
        )
        assert_matches_type(LinkSubmitResponse, link, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncComposio) -> None:
        response = await async_client.link.with_raw_response.submit(
            token="token",
            input={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkSubmitResponse, link, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncComposio) -> None:
        async with async_client.link.with_streaming_response.submit(
            token="token",
            input={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkSubmitResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.link.with_raw_response.submit(
                token="",
                input={"foo": "bar"},
            )
