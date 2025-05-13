# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.org import (
    ProjectListResponse,
    ProjectCreateResponse,
    ProjectDeleteResponse,
    ProjectRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProject:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Composio) -> None:
        project = client.org.project.create(
            name="name",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Composio) -> None:
        response = client.org.project.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Composio) -> None:
        with client.org.project.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        project = client.org.project.retrieve(
            "projectId",
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.org.project.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.org.project.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.org.project.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        project = client.org.project.list()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.org.project.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.org.project.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Composio) -> None:
        project = client.org.project.delete(
            "projectId",
        )
        assert_matches_type(ProjectDeleteResponse, project, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Composio) -> None:
        response = client.org.project.with_raw_response.delete(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectDeleteResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Composio) -> None:
        with client.org.project.with_streaming_response.delete(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectDeleteResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.org.project.with_raw_response.delete(
                "",
            )


class TestAsyncProject:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncComposio) -> None:
        project = await async_client.org.project.create(
            name="name",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        project = await async_client.org.project.retrieve(
            "projectId",
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.org.project.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        project = await async_client.org.project.list()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncComposio) -> None:
        project = await async_client.org.project.delete(
            "projectId",
        )
        assert_matches_type(ProjectDeleteResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.with_raw_response.delete(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectDeleteResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.with_streaming_response.delete(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectDeleteResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.org.project.with_raw_response.delete(
                "",
            )
