# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    McpListResponse,
    McpCreateResponse,
    McpDeleteResponse,
    McpUpdateResponse,
    McpRetrieveResponse,
    McpValidateResponse,
    McpRetrieveAppResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Composio) -> None:
        mcp = client.mcp.create(
            name="name",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Composio) -> None:
        mcp = client.mcp.create(
            name="name",
            actions=["string"],
            apps=["string"],
            auth_configs={"foo": "bar"},
            connected_account_ids=["string"],
            custom_auth_headers=True,
            entity_ids=["string"],
            ttl="1d",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpCreateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        mcp = client.mcp.retrieve(
            "id",
        )
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mcp.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Composio) -> None:
        mcp = client.mcp.update(
            id="id",
        )
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Composio) -> None:
        mcp = client.mcp.update(
            id="id",
            actions=["string"],
            apps=["string"],
            name="name",
        )
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpUpdateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mcp.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        mcp = client.mcp.list()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        mcp = client.mcp.list(
            app_id=["string"],
            connected_account_id=["string"],
            cursor=0,
            entity_id=["string"],
            integration_id="integration_id",
            limit=0,
        )
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpListResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Composio) -> None:
        mcp = client.mcp.delete(
            "id",
        )
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpDeleteResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mcp.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_retrieve_app(self, client: Composio) -> None:
        mcp = client.mcp.retrieve_app(
            "appKey",
        )
        assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_retrieve_app(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.retrieve_app(
            "appKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_app(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.retrieve_app(
            "appKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_app(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_key` but received ''"):
            client.mcp.with_raw_response.retrieve_app(
                "",
            )

    @parametrize
    def test_method_validate(self, client: Composio) -> None:
        mcp = client.mcp.validate(
            uuid="uuid",
            x_composio_admin_token="x-composio-admin-token",
        )
        assert_matches_type(McpValidateResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: Composio) -> None:
        response = client.mcp.with_raw_response.validate(
            uuid="uuid",
            x_composio_admin_token="x-composio-admin-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpValidateResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: Composio) -> None:
        with client.mcp.with_streaming_response.validate(
            uuid="uuid",
            x_composio_admin_token="x-composio-admin-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpValidateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_validate(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.mcp.with_raw_response.validate(
                uuid="",
                x_composio_admin_token="x-composio-admin-token",
            )


class TestAsyncMcp:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.create(
            name="name",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.create(
            name="name",
            actions=["string"],
            apps=["string"],
            auth_configs={"foo": "bar"},
            connected_account_ids=["string"],
            custom_auth_headers=True,
            entity_ids=["string"],
            ttl="1d",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpCreateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.retrieve(
            "id",
        )
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mcp.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.update(
            id="id",
        )
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.update(
            id="id",
            actions=["string"],
            apps=["string"],
            name="name",
        )
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpUpdateResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpUpdateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mcp.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.list()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.list(
            app_id=["string"],
            connected_account_id=["string"],
            cursor=0,
            entity_id=["string"],
            integration_id="integration_id",
            limit=0,
        )
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpListResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.delete(
            "id",
        )
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpDeleteResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mcp.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_retrieve_app(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.retrieve_app(
            "appKey",
        )
        assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_app(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.retrieve_app(
            "appKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_app(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.retrieve_app(
            "appKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpRetrieveAppResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_app(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_key` but received ''"):
            await async_client.mcp.with_raw_response.retrieve_app(
                "",
            )

    @parametrize
    async def test_method_validate(self, async_client: AsyncComposio) -> None:
        mcp = await async_client.mcp.validate(
            uuid="uuid",
            x_composio_admin_token="x-composio-admin-token",
        )
        assert_matches_type(McpValidateResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncComposio) -> None:
        response = await async_client.mcp.with_raw_response.validate(
            uuid="uuid",
            x_composio_admin_token="x-composio-admin-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpValidateResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncComposio) -> None:
        async with async_client.mcp.with_streaming_response.validate(
            uuid="uuid",
            x_composio_admin_token="x-composio-admin-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpValidateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_validate(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.mcp.with_raw_response.validate(
                uuid="",
                x_composio_admin_token="x-composio-admin-token",
            )
