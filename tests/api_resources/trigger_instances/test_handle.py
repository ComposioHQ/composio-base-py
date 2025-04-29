# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHandle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        handle = client.trigger_instances.handle.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )
        assert_matches_type(str, handle, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.trigger_instances.handle.with_raw_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        handle = response.parse()
        assert_matches_type(str, handle, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.trigger_instances.handle.with_streaming_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            handle = response.parse()
            assert_matches_type(str, handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.trigger_instances.handle.with_raw_response.retrieve(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                slug="",
            )

    @parametrize
    def test_method_execute(self, client: Composio) -> None:
        handle = client.trigger_instances.handle.execute(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )
        assert_matches_type(str, handle, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Composio) -> None:
        response = client.trigger_instances.handle.with_raw_response.execute(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        handle = response.parse()
        assert_matches_type(str, handle, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Composio) -> None:
        with client.trigger_instances.handle.with_streaming_response.execute(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            handle = response.parse()
            assert_matches_type(str, handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_execute(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.trigger_instances.handle.with_raw_response.execute(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                slug="",
            )


class TestAsyncHandle:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        handle = await async_client.trigger_instances.handle.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )
        assert_matches_type(str, handle, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.trigger_instances.handle.with_raw_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        handle = await response.parse()
        assert_matches_type(str, handle, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.trigger_instances.handle.with_streaming_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            handle = await response.parse()
            assert_matches_type(str, handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.trigger_instances.handle.with_raw_response.retrieve(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                slug="",
            )

    @parametrize
    async def test_method_execute(self, async_client: AsyncComposio) -> None:
        handle = await async_client.trigger_instances.handle.execute(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )
        assert_matches_type(str, handle, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncComposio) -> None:
        response = await async_client.trigger_instances.handle.with_raw_response.execute(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        handle = await response.parse()
        assert_matches_type(str, handle, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncComposio) -> None:
        async with async_client.trigger_instances.handle.with_streaming_response.execute(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            handle = await response.parse()
            assert_matches_type(str, handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_execute(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.trigger_instances.handle.with_raw_response.execute(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                slug="",
            )
