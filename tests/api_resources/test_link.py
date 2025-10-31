# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import LinkCreateResponse

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
            connection_data={
                "account_id": "account_id",
                "account_url": "account_url",
                "api_url": "api_url",
                "base_url": "base_url",
                "borneo_dashboard_url": "borneo_dashboard_url",
                "companydomain": "COMPANYDOMAIN",
                "dc": "dc",
                "domain": "domain",
                "extension": "extension",
                "form_api_base_url": "form_api_base_url",
                "instance_endpoint": "instanceEndpoint",
                "instance_name": "instanceName",
                "proxy_password": "proxy_password",
                "proxy_username": "proxy_username",
                "region": "region",
                "server_location": "server_location",
                "shop": "shop",
                "site_name": "site_name",
                "subdomain": "subdomain",
                "version": "version",
                "your_server": "your_server",
                "your_domain": "your-domain",
            },
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
            connection_data={
                "account_id": "account_id",
                "account_url": "account_url",
                "api_url": "api_url",
                "base_url": "base_url",
                "borneo_dashboard_url": "borneo_dashboard_url",
                "companydomain": "COMPANYDOMAIN",
                "dc": "dc",
                "domain": "domain",
                "extension": "extension",
                "form_api_base_url": "form_api_base_url",
                "instance_endpoint": "instanceEndpoint",
                "instance_name": "instanceName",
                "proxy_password": "proxy_password",
                "proxy_username": "proxy_username",
                "region": "region",
                "server_location": "server_location",
                "shop": "shop",
                "site_name": "site_name",
                "subdomain": "subdomain",
                "version": "version",
                "your_server": "your_server",
                "your_domain": "your-domain",
            },
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
