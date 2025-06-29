# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.trigger_instances import ManageDeleteResponse, ManageUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Composio) -> None:
        manage = client.trigger_instances.manage.update(
            trigger_id="triggerId",
            status="enable",
        )
        assert_matches_type(ManageUpdateResponse, manage, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Composio) -> None:
        response = client.trigger_instances.manage.with_raw_response.update(
            trigger_id="triggerId",
            status="enable",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manage = response.parse()
        assert_matches_type(ManageUpdateResponse, manage, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Composio) -> None:
        with client.trigger_instances.manage.with_streaming_response.update(
            trigger_id="triggerId",
            status="enable",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manage = response.parse()
            assert_matches_type(ManageUpdateResponse, manage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            client.trigger_instances.manage.with_raw_response.update(
                trigger_id="",
                status="enable",
            )

    @parametrize
    def test_method_delete(self, client: Composio) -> None:
        manage = client.trigger_instances.manage.delete(
            "triggerId",
        )
        assert_matches_type(ManageDeleteResponse, manage, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Composio) -> None:
        response = client.trigger_instances.manage.with_raw_response.delete(
            "triggerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manage = response.parse()
        assert_matches_type(ManageDeleteResponse, manage, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Composio) -> None:
        with client.trigger_instances.manage.with_streaming_response.delete(
            "triggerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manage = response.parse()
            assert_matches_type(ManageDeleteResponse, manage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            client.trigger_instances.manage.with_raw_response.delete(
                "",
            )


class TestAsyncManage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncComposio) -> None:
        manage = await async_client.trigger_instances.manage.update(
            trigger_id="triggerId",
            status="enable",
        )
        assert_matches_type(ManageUpdateResponse, manage, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncComposio) -> None:
        response = await async_client.trigger_instances.manage.with_raw_response.update(
            trigger_id="triggerId",
            status="enable",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manage = await response.parse()
        assert_matches_type(ManageUpdateResponse, manage, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncComposio) -> None:
        async with async_client.trigger_instances.manage.with_streaming_response.update(
            trigger_id="triggerId",
            status="enable",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manage = await response.parse()
            assert_matches_type(ManageUpdateResponse, manage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            await async_client.trigger_instances.manage.with_raw_response.update(
                trigger_id="",
                status="enable",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncComposio) -> None:
        manage = await async_client.trigger_instances.manage.delete(
            "triggerId",
        )
        assert_matches_type(ManageDeleteResponse, manage, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncComposio) -> None:
        response = await async_client.trigger_instances.manage.with_raw_response.delete(
            "triggerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manage = await response.parse()
        assert_matches_type(ManageDeleteResponse, manage, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncComposio) -> None:
        async with async_client.trigger_instances.manage.with_streaming_response.delete(
            "triggerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manage = await response.parse()
            assert_matches_type(ManageDeleteResponse, manage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            await async_client.trigger_instances.manage.with_raw_response.delete(
                "",
            )
