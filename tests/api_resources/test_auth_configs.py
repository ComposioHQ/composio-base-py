# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    AuthConfigListResponse,
    AuthConfigCreateResponse,
    AuthConfigRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Composio) -> None:
        auth_config = client.auth_configs.create(
            toolkit={"slug": "slug"},
        )
        assert_matches_type(AuthConfigCreateResponse, auth_config, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Composio) -> None:
        auth_config = client.auth_configs.create(
            toolkit={"slug": "slug"},
            auth_config={
                "type": "use_composio_managed_auth",
                "credentials": {
                    "scopes": "string",
                    "user_scopes": "string",
                },
                "name": "name",
                "tool_access_config": {"tools_for_connected_account_creation": ["string"]},
            },
        )
        assert_matches_type(AuthConfigCreateResponse, auth_config, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Composio) -> None:
        response = client.auth_configs.with_raw_response.create(
            toolkit={"slug": "slug"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = response.parse()
        assert_matches_type(AuthConfigCreateResponse, auth_config, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Composio) -> None:
        with client.auth_configs.with_streaming_response.create(
            toolkit={"slug": "slug"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = response.parse()
            assert_matches_type(AuthConfigCreateResponse, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        auth_config = client.auth_configs.retrieve(
            "nanoid",
        )
        assert_matches_type(AuthConfigRetrieveResponse, auth_config, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.auth_configs.with_raw_response.retrieve(
            "nanoid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = response.parse()
        assert_matches_type(AuthConfigRetrieveResponse, auth_config, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.auth_configs.with_streaming_response.retrieve(
            "nanoid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = response.parse()
            assert_matches_type(AuthConfigRetrieveResponse, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            client.auth_configs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update_overload_1(self, client: Composio) -> None:
        auth_config = client.auth_configs.update(
            nanoid="nanoid",
            credentials={},
            type="custom",
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Composio) -> None:
        auth_config = client.auth_configs.update(
            nanoid="nanoid",
            credentials={
                "scopes": "string",
                "user_scopes": "string",
            },
            type="custom",
            proxy_config={
                "proxy_url": "https://example.com",
                "proxy_auth_key": "proxy_auth_key",
            },
            tool_access_config={
                "tools_available_for_execution": ["string"],
                "tools_for_connected_account_creation": ["string"],
            },
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Composio) -> None:
        response = client.auth_configs.with_raw_response.update(
            nanoid="nanoid",
            credentials={},
            type="custom",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = response.parse()
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Composio) -> None:
        with client.auth_configs.with_streaming_response.update(
            nanoid="nanoid",
            credentials={},
            type="custom",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = response.parse()
            assert_matches_type(object, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            client.auth_configs.with_raw_response.update(
                nanoid="",
                credentials={},
                type="custom",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Composio) -> None:
        auth_config = client.auth_configs.update(
            nanoid="nanoid",
            type="default",
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Composio) -> None:
        auth_config = client.auth_configs.update(
            nanoid="nanoid",
            type="default",
            scopes="string",
            tool_access_config={
                "tools_available_for_execution": ["string"],
                "tools_for_connected_account_creation": ["string"],
            },
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Composio) -> None:
        response = client.auth_configs.with_raw_response.update(
            nanoid="nanoid",
            type="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = response.parse()
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Composio) -> None:
        with client.auth_configs.with_streaming_response.update(
            nanoid="nanoid",
            type="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = response.parse()
            assert_matches_type(object, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            client.auth_configs.with_raw_response.update(
                nanoid="",
                type="default",
            )

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        auth_config = client.auth_configs.list()
        assert_matches_type(AuthConfigListResponse, auth_config, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        auth_config = client.auth_configs.list(
            cursor="cursor",
            deprecated_app_id="deprecated_app_id",
            deprecated_status="deprecated_status",
            is_composio_managed="string",
            limit=0,
            search="search",
            show_disabled=True,
            toolkit_slug="toolkit_slug",
        )
        assert_matches_type(AuthConfigListResponse, auth_config, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.auth_configs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = response.parse()
        assert_matches_type(AuthConfigListResponse, auth_config, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.auth_configs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = response.parse()
            assert_matches_type(AuthConfigListResponse, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Composio) -> None:
        auth_config = client.auth_configs.delete(
            "nanoid",
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Composio) -> None:
        response = client.auth_configs.with_raw_response.delete(
            "nanoid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = response.parse()
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Composio) -> None:
        with client.auth_configs.with_streaming_response.delete(
            "nanoid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = response.parse()
            assert_matches_type(object, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            client.auth_configs.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_update_status(self, client: Composio) -> None:
        auth_config = client.auth_configs.update_status(
            status="ENABLED",
            nanoid="nanoid",
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    def test_raw_response_update_status(self, client: Composio) -> None:
        response = client.auth_configs.with_raw_response.update_status(
            status="ENABLED",
            nanoid="nanoid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = response.parse()
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    def test_streaming_response_update_status(self, client: Composio) -> None:
        with client.auth_configs.with_streaming_response.update_status(
            status="ENABLED",
            nanoid="nanoid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = response.parse()
            assert_matches_type(object, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_status(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            client.auth_configs.with_raw_response.update_status(
                status="ENABLED",
                nanoid="",
            )


class TestAsyncAuthConfigs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncComposio) -> None:
        auth_config = await async_client.auth_configs.create(
            toolkit={"slug": "slug"},
        )
        assert_matches_type(AuthConfigCreateResponse, auth_config, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncComposio) -> None:
        auth_config = await async_client.auth_configs.create(
            toolkit={"slug": "slug"},
            auth_config={
                "type": "use_composio_managed_auth",
                "credentials": {
                    "scopes": "string",
                    "user_scopes": "string",
                },
                "name": "name",
                "tool_access_config": {"tools_for_connected_account_creation": ["string"]},
            },
        )
        assert_matches_type(AuthConfigCreateResponse, auth_config, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncComposio) -> None:
        response = await async_client.auth_configs.with_raw_response.create(
            toolkit={"slug": "slug"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = await response.parse()
        assert_matches_type(AuthConfigCreateResponse, auth_config, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncComposio) -> None:
        async with async_client.auth_configs.with_streaming_response.create(
            toolkit={"slug": "slug"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = await response.parse()
            assert_matches_type(AuthConfigCreateResponse, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        auth_config = await async_client.auth_configs.retrieve(
            "nanoid",
        )
        assert_matches_type(AuthConfigRetrieveResponse, auth_config, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.auth_configs.with_raw_response.retrieve(
            "nanoid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = await response.parse()
        assert_matches_type(AuthConfigRetrieveResponse, auth_config, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.auth_configs.with_streaming_response.retrieve(
            "nanoid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = await response.parse()
            assert_matches_type(AuthConfigRetrieveResponse, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            await async_client.auth_configs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncComposio) -> None:
        auth_config = await async_client.auth_configs.update(
            nanoid="nanoid",
            credentials={},
            type="custom",
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncComposio) -> None:
        auth_config = await async_client.auth_configs.update(
            nanoid="nanoid",
            credentials={
                "scopes": "string",
                "user_scopes": "string",
            },
            type="custom",
            proxy_config={
                "proxy_url": "https://example.com",
                "proxy_auth_key": "proxy_auth_key",
            },
            tool_access_config={
                "tools_available_for_execution": ["string"],
                "tools_for_connected_account_creation": ["string"],
            },
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncComposio) -> None:
        response = await async_client.auth_configs.with_raw_response.update(
            nanoid="nanoid",
            credentials={},
            type="custom",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = await response.parse()
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncComposio) -> None:
        async with async_client.auth_configs.with_streaming_response.update(
            nanoid="nanoid",
            credentials={},
            type="custom",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = await response.parse()
            assert_matches_type(object, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            await async_client.auth_configs.with_raw_response.update(
                nanoid="",
                credentials={},
                type="custom",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncComposio) -> None:
        auth_config = await async_client.auth_configs.update(
            nanoid="nanoid",
            type="default",
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncComposio) -> None:
        auth_config = await async_client.auth_configs.update(
            nanoid="nanoid",
            type="default",
            scopes="string",
            tool_access_config={
                "tools_available_for_execution": ["string"],
                "tools_for_connected_account_creation": ["string"],
            },
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncComposio) -> None:
        response = await async_client.auth_configs.with_raw_response.update(
            nanoid="nanoid",
            type="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = await response.parse()
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncComposio) -> None:
        async with async_client.auth_configs.with_streaming_response.update(
            nanoid="nanoid",
            type="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = await response.parse()
            assert_matches_type(object, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            await async_client.auth_configs.with_raw_response.update(
                nanoid="",
                type="default",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        auth_config = await async_client.auth_configs.list()
        assert_matches_type(AuthConfigListResponse, auth_config, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        auth_config = await async_client.auth_configs.list(
            cursor="cursor",
            deprecated_app_id="deprecated_app_id",
            deprecated_status="deprecated_status",
            is_composio_managed="string",
            limit=0,
            search="search",
            show_disabled=True,
            toolkit_slug="toolkit_slug",
        )
        assert_matches_type(AuthConfigListResponse, auth_config, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.auth_configs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = await response.parse()
        assert_matches_type(AuthConfigListResponse, auth_config, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.auth_configs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = await response.parse()
            assert_matches_type(AuthConfigListResponse, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncComposio) -> None:
        auth_config = await async_client.auth_configs.delete(
            "nanoid",
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncComposio) -> None:
        response = await async_client.auth_configs.with_raw_response.delete(
            "nanoid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = await response.parse()
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncComposio) -> None:
        async with async_client.auth_configs.with_streaming_response.delete(
            "nanoid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = await response.parse()
            assert_matches_type(object, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            await async_client.auth_configs.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_update_status(self, async_client: AsyncComposio) -> None:
        auth_config = await async_client.auth_configs.update_status(
            status="ENABLED",
            nanoid="nanoid",
        )
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncComposio) -> None:
        response = await async_client.auth_configs.with_raw_response.update_status(
            status="ENABLED",
            nanoid="nanoid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_config = await response.parse()
        assert_matches_type(object, auth_config, path=["response"])

    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncComposio) -> None:
        async with async_client.auth_configs.with_streaming_response.update_status(
            status="ENABLED",
            nanoid="nanoid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_config = await response.parse()
            assert_matches_type(object, auth_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            await async_client.auth_configs.with_raw_response.update_status(
                status="ENABLED",
                nanoid="",
            )
