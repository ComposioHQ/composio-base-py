# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.org.project import (
    WebhookDeleteResponse,
    WebhookUpdateResponse,
    WebhookRefreshResponse,
    WebhookRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhook:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        webhook = client.org.project.webhook.retrieve(
            type="trigger",
        )
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.org.project.webhook.with_raw_response.retrieve(
            type="trigger",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.org.project.webhook.with_streaming_response.retrieve(
            type="trigger",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Composio) -> None:
        webhook = client.org.project.webhook.update(
            type="trigger",
            webhook_url="https://example.com",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Composio) -> None:
        response = client.org.project.webhook.with_raw_response.update(
            type="trigger",
            webhook_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Composio) -> None:
        with client.org.project.webhook.with_streaming_response.update(
            type="trigger",
            webhook_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Composio) -> None:
        webhook = client.org.project.webhook.delete(
            type="trigger",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Composio) -> None:
        response = client.org.project.webhook.with_raw_response.delete(
            type="trigger",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Composio) -> None:
        with client.org.project.webhook.with_streaming_response.delete(
            type="trigger",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_refresh(self, client: Composio) -> None:
        webhook = client.org.project.webhook.refresh()
        assert_matches_type(WebhookRefreshResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_refresh(self, client: Composio) -> None:
        response = client.org.project.webhook.with_raw_response.refresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookRefreshResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_refresh(self, client: Composio) -> None:
        with client.org.project.webhook.with_streaming_response.refresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookRefreshResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhook:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        webhook = await async_client.org.project.webhook.retrieve(
            type="trigger",
        )
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.webhook.with_raw_response.retrieve(
            type="trigger",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.webhook.with_streaming_response.retrieve(
            type="trigger",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncComposio) -> None:
        webhook = await async_client.org.project.webhook.update(
            type="trigger",
            webhook_url="https://example.com",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.webhook.with_raw_response.update(
            type="trigger",
            webhook_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.webhook.with_streaming_response.update(
            type="trigger",
            webhook_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncComposio) -> None:
        webhook = await async_client.org.project.webhook.delete(
            type="trigger",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.webhook.with_raw_response.delete(
            type="trigger",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.webhook.with_streaming_response.delete(
            type="trigger",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_refresh(self, async_client: AsyncComposio) -> None:
        webhook = await async_client.org.project.webhook.refresh()
        assert_matches_type(WebhookRefreshResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.webhook.with_raw_response.refresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookRefreshResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.webhook.with_streaming_response.refresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookRefreshResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
