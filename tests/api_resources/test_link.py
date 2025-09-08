# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import LinkRetrieveResponse, LinkSubmitInputResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLink:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
    def test_method_submit_input(self, client: Composio) -> None:
        link = client.link.submit_input(
            token="token",
            input={"foo": "bar"},
        )
        assert_matches_type(LinkSubmitInputResponse, link, path=["response"])

    @parametrize
    def test_raw_response_submit_input(self, client: Composio) -> None:
        response = client.link.with_raw_response.submit_input(
            token="token",
            input={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkSubmitInputResponse, link, path=["response"])

    @parametrize
    def test_streaming_response_submit_input(self, client: Composio) -> None:
        with client.link.with_streaming_response.submit_input(
            token="token",
            input={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkSubmitInputResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit_input(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.link.with_raw_response.submit_input(
                token="",
                input={"foo": "bar"},
            )


class TestAsyncLink:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

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
    async def test_method_submit_input(self, async_client: AsyncComposio) -> None:
        link = await async_client.link.submit_input(
            token="token",
            input={"foo": "bar"},
        )
        assert_matches_type(LinkSubmitInputResponse, link, path=["response"])

    @parametrize
    async def test_raw_response_submit_input(self, async_client: AsyncComposio) -> None:
        response = await async_client.link.with_raw_response.submit_input(
            token="token",
            input={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkSubmitInputResponse, link, path=["response"])

    @parametrize
    async def test_streaming_response_submit_input(self, async_client: AsyncComposio) -> None:
        async with async_client.link.with_streaming_response.submit_input(
            token="token",
            input={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkSubmitInputResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit_input(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.link.with_raw_response.submit_input(
                token="",
                input={"foo": "bar"},
            )
