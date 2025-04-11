# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    TriggerInstanceUpsertResponse,
    TriggerInstanceListActiveResponse,
    TriggerInstanceRemoveUpsertResponse,
    TriggerInstanceUpdateStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTriggerInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_active(self, client: Composio) -> None:
        trigger_instance = client.trigger_instances.list_active()
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @parametrize
    def test_method_list_active_with_all_params(self, client: Composio) -> None:
        trigger_instance = client.trigger_instances.list_active(
            auth_config_ids="authConfigIds",
            connected_account_ids="connectedAccountIds",
            limit=1,
            page=1,
            show_disabled=True,
            trigger_ids="triggerIds",
            trigger_names="triggerNames",
        )
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @parametrize
    def test_raw_response_list_active(self, client: Composio) -> None:
        response = client.trigger_instances.with_raw_response.list_active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = response.parse()
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @parametrize
    def test_streaming_response_list_active(self, client: Composio) -> None:
        with client.trigger_instances.with_streaming_response.list_active() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = response.parse()
            assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove_upsert(self, client: Composio) -> None:
        trigger_instance = client.trigger_instances.remove_upsert(
            "slug",
        )
        assert_matches_type(TriggerInstanceRemoveUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    def test_raw_response_remove_upsert(self, client: Composio) -> None:
        response = client.trigger_instances.with_raw_response.remove_upsert(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = response.parse()
        assert_matches_type(TriggerInstanceRemoveUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    def test_streaming_response_remove_upsert(self, client: Composio) -> None:
        with client.trigger_instances.with_streaming_response.remove_upsert(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = response.parse()
            assert_matches_type(TriggerInstanceRemoveUpsertResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_upsert(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.trigger_instances.with_raw_response.remove_upsert(
                "",
            )

    @parametrize
    def test_method_update_status(self, client: Composio) -> None:
        trigger_instance = client.trigger_instances.update_status(
            status="enable",
            slug="slug",
        )
        assert_matches_type(TriggerInstanceUpdateStatusResponse, trigger_instance, path=["response"])

    @parametrize
    def test_raw_response_update_status(self, client: Composio) -> None:
        response = client.trigger_instances.with_raw_response.update_status(
            status="enable",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = response.parse()
        assert_matches_type(TriggerInstanceUpdateStatusResponse, trigger_instance, path=["response"])

    @parametrize
    def test_streaming_response_update_status(self, client: Composio) -> None:
        with client.trigger_instances.with_streaming_response.update_status(
            status="enable",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = response.parse()
            assert_matches_type(TriggerInstanceUpdateStatusResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_status(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.trigger_instances.with_raw_response.update_status(
                status="enable",
                slug="",
            )

    @parametrize
    def test_method_upsert(self, client: Composio) -> None:
        trigger_instance = client.trigger_instances.upsert(
            slug="slug",
            connected_auth_id="connectedAuthId",
            trigger_config={"foo": "bar"},
        )
        assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    def test_raw_response_upsert(self, client: Composio) -> None:
        response = client.trigger_instances.with_raw_response.upsert(
            slug="slug",
            connected_auth_id="connectedAuthId",
            trigger_config={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = response.parse()
        assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    def test_streaming_response_upsert(self, client: Composio) -> None:
        with client.trigger_instances.with_streaming_response.upsert(
            slug="slug",
            connected_auth_id="connectedAuthId",
            trigger_config={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = response.parse()
            assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upsert(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.trigger_instances.with_raw_response.upsert(
                slug="",
                connected_auth_id="connectedAuthId",
                trigger_config={"foo": "bar"},
            )


class TestAsyncTriggerInstances:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list_active(self, async_client: AsyncComposio) -> None:
        trigger_instance = await async_client.trigger_instances.list_active()
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_method_list_active_with_all_params(self, async_client: AsyncComposio) -> None:
        trigger_instance = await async_client.trigger_instances.list_active(
            auth_config_ids="authConfigIds",
            connected_account_ids="connectedAccountIds",
            limit=1,
            page=1,
            show_disabled=True,
            trigger_ids="triggerIds",
            trigger_names="triggerNames",
        )
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_raw_response_list_active(self, async_client: AsyncComposio) -> None:
        response = await async_client.trigger_instances.with_raw_response.list_active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = await response.parse()
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_streaming_response_list_active(self, async_client: AsyncComposio) -> None:
        async with async_client.trigger_instances.with_streaming_response.list_active() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = await response.parse()
            assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove_upsert(self, async_client: AsyncComposio) -> None:
        trigger_instance = await async_client.trigger_instances.remove_upsert(
            "slug",
        )
        assert_matches_type(TriggerInstanceRemoveUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_raw_response_remove_upsert(self, async_client: AsyncComposio) -> None:
        response = await async_client.trigger_instances.with_raw_response.remove_upsert(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = await response.parse()
        assert_matches_type(TriggerInstanceRemoveUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_streaming_response_remove_upsert(self, async_client: AsyncComposio) -> None:
        async with async_client.trigger_instances.with_streaming_response.remove_upsert(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = await response.parse()
            assert_matches_type(TriggerInstanceRemoveUpsertResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_upsert(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.trigger_instances.with_raw_response.remove_upsert(
                "",
            )

    @parametrize
    async def test_method_update_status(self, async_client: AsyncComposio) -> None:
        trigger_instance = await async_client.trigger_instances.update_status(
            status="enable",
            slug="slug",
        )
        assert_matches_type(TriggerInstanceUpdateStatusResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncComposio) -> None:
        response = await async_client.trigger_instances.with_raw_response.update_status(
            status="enable",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = await response.parse()
        assert_matches_type(TriggerInstanceUpdateStatusResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncComposio) -> None:
        async with async_client.trigger_instances.with_streaming_response.update_status(
            status="enable",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = await response.parse()
            assert_matches_type(TriggerInstanceUpdateStatusResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.trigger_instances.with_raw_response.update_status(
                status="enable",
                slug="",
            )

    @parametrize
    async def test_method_upsert(self, async_client: AsyncComposio) -> None:
        trigger_instance = await async_client.trigger_instances.upsert(
            slug="slug",
            connected_auth_id="connectedAuthId",
            trigger_config={"foo": "bar"},
        )
        assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncComposio) -> None:
        response = await async_client.trigger_instances.with_raw_response.upsert(
            slug="slug",
            connected_auth_id="connectedAuthId",
            trigger_config={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = await response.parse()
        assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncComposio) -> None:
        async with async_client.trigger_instances.with_streaming_response.upsert(
            slug="slug",
            connected_auth_id="connectedAuthId",
            trigger_config={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = await response.parse()
            assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.trigger_instances.with_raw_response.upsert(
                slug="",
                connected_auth_id="connectedAuthId",
                trigger_config={"foo": "bar"},
            )
