# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.org.project import (
    APIKeyListResponse,
    APIKeyCreateResponse,
    APIKeyDeleteResponse,
    APIKeyCreateAPIKeyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Composio) -> None:
        api_key = client.org.project.api_keys.create(
            project_id="proj_abc123xyz456",
            name="Production API Key",
        )
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Composio) -> None:
        response = client.org.project.api_keys.with_raw_response.create(
            project_id="proj_abc123xyz456",
            name="Production API Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Composio) -> None:
        with client.org.project.api_keys.with_streaming_response.create(
            project_id="proj_abc123xyz456",
            name="Production API Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.org.project.api_keys.with_raw_response.create(
                project_id="",
                name="Production API Key",
            )

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        api_key = client.org.project.api_keys.list(
            "proj_abc123xyz456",
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.org.project.api_keys.with_raw_response.list(
            "proj_abc123xyz456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.org.project.api_keys.with_streaming_response.list(
            "proj_abc123xyz456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.org.project.api_keys.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Composio) -> None:
        api_key = client.org.project.api_keys.delete(
            id="01H4DKRF5SMP7NQCA3BWT0JYB6",
            project_id="proj_abc123xyz456",
        )
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Composio) -> None:
        response = client.org.project.api_keys.with_raw_response.delete(
            id="01H4DKRF5SMP7NQCA3BWT0JYB6",
            project_id="proj_abc123xyz456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Composio) -> None:
        with client.org.project.api_keys.with_streaming_response.delete(
            id="01H4DKRF5SMP7NQCA3BWT0JYB6",
            project_id="proj_abc123xyz456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.org.project.api_keys.with_raw_response.delete(
                id="01H4DKRF5SMP7NQCA3BWT0JYB6",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.project.api_keys.with_raw_response.delete(
                id="",
                project_id="proj_abc123xyz456",
            )

    @parametrize
    def test_method_create_api_key(self, client: Composio) -> None:
        api_key = client.org.project.api_keys.create_api_key(
            "proj_abc123xyz456",
        )
        assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_create_api_key(self, client: Composio) -> None:
        response = client.org.project.api_keys.with_raw_response.create_api_key(
            "proj_abc123xyz456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_create_api_key(self, client: Composio) -> None:
        with client.org.project.api_keys.with_streaming_response.create_api_key(
            "proj_abc123xyz456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_api_key(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.org.project.api_keys.with_raw_response.create_api_key(
                "",
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncComposio) -> None:
        api_key = await async_client.org.project.api_keys.create(
            project_id="proj_abc123xyz456",
            name="Production API Key",
        )
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.api_keys.with_raw_response.create(
            project_id="proj_abc123xyz456",
            name="Production API Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.api_keys.with_streaming_response.create(
            project_id="proj_abc123xyz456",
            name="Production API Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.org.project.api_keys.with_raw_response.create(
                project_id="",
                name="Production API Key",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        api_key = await async_client.org.project.api_keys.list(
            "proj_abc123xyz456",
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.api_keys.with_raw_response.list(
            "proj_abc123xyz456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.api_keys.with_streaming_response.list(
            "proj_abc123xyz456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.org.project.api_keys.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncComposio) -> None:
        api_key = await async_client.org.project.api_keys.delete(
            id="01H4DKRF5SMP7NQCA3BWT0JYB6",
            project_id="proj_abc123xyz456",
        )
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.api_keys.with_raw_response.delete(
            id="01H4DKRF5SMP7NQCA3BWT0JYB6",
            project_id="proj_abc123xyz456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.api_keys.with_streaming_response.delete(
            id="01H4DKRF5SMP7NQCA3BWT0JYB6",
            project_id="proj_abc123xyz456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.org.project.api_keys.with_raw_response.delete(
                id="01H4DKRF5SMP7NQCA3BWT0JYB6",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.project.api_keys.with_raw_response.delete(
                id="",
                project_id="proj_abc123xyz456",
            )

    @parametrize
    async def test_method_create_api_key(self, async_client: AsyncComposio) -> None:
        api_key = await async_client.org.project.api_keys.create_api_key(
            "proj_abc123xyz456",
        )
        assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_create_api_key(self, async_client: AsyncComposio) -> None:
        response = await async_client.org.project.api_keys.with_raw_response.create_api_key(
            "proj_abc123xyz456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_create_api_key(self, async_client: AsyncComposio) -> None:
        async with async_client.org.project.api_keys.with_streaming_response.create_api_key(
            "proj_abc123xyz456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_api_key(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.org.project.api_keys.with_raw_response.create_api_key(
                "",
            )
