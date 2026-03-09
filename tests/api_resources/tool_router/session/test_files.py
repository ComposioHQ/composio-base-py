# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.tool_router.session import (
    FileListResponse,
    FileDeleteResponse,
    FileCreateUploadURLResponse,
    FileCreateDownloadURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        file = client.tool_router.session.files.list(
            mount_id="files",
            session_id="trs_123456789",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        file = client.tool_router.session.files.list(
            mount_id="files",
            session_id="trs_123456789",
            cursor="cursor",
            limit=1,
            mount_relative_prefix="data/",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.tool_router.session.files.with_raw_response.list(
            mount_id="files",
            session_id="trs_123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.tool_router.session.files.with_streaming_response.list(
            mount_id="files",
            session_id="trs_123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.tool_router.session.files.with_raw_response.list(
                mount_id="files",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mount_id` but received ''"):
            client.tool_router.session.files.with_raw_response.list(
                mount_id="",
                session_id="trs_123456789",
            )

    @parametrize
    def test_method_delete(self, client: Composio) -> None:
        file = client.tool_router.session.files.delete(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Composio) -> None:
        response = client.tool_router.session.files.with_raw_response.delete(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Composio) -> None:
        with client.tool_router.session.files.with_streaming_response.delete(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.tool_router.session.files.with_raw_response.delete(
                mount_id="files",
                session_id="",
                mount_relative_path="report.pdf",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mount_id` but received ''"):
            client.tool_router.session.files.with_raw_response.delete(
                mount_id="",
                session_id="trs_123456789",
                mount_relative_path="report.pdf",
            )

    @parametrize
    def test_method_create_download_url(self, client: Composio) -> None:
        file = client.tool_router.session.files.create_download_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )
        assert_matches_type(FileCreateDownloadURLResponse, file, path=["response"])

    @parametrize
    def test_raw_response_create_download_url(self, client: Composio) -> None:
        response = client.tool_router.session.files.with_raw_response.create_download_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileCreateDownloadURLResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_create_download_url(self, client: Composio) -> None:
        with client.tool_router.session.files.with_streaming_response.create_download_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileCreateDownloadURLResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_download_url(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.tool_router.session.files.with_raw_response.create_download_url(
                mount_id="files",
                session_id="",
                mount_relative_path="report.pdf",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mount_id` but received ''"):
            client.tool_router.session.files.with_raw_response.create_download_url(
                mount_id="",
                session_id="trs_123456789",
                mount_relative_path="report.pdf",
            )

    @parametrize
    def test_method_create_upload_url(self, client: Composio) -> None:
        file = client.tool_router.session.files.create_upload_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )
        assert_matches_type(FileCreateUploadURLResponse, file, path=["response"])

    @parametrize
    def test_method_create_upload_url_with_all_params(self, client: Composio) -> None:
        file = client.tool_router.session.files.create_upload_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
            mimetype="application/pdf",
        )
        assert_matches_type(FileCreateUploadURLResponse, file, path=["response"])

    @parametrize
    def test_raw_response_create_upload_url(self, client: Composio) -> None:
        response = client.tool_router.session.files.with_raw_response.create_upload_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileCreateUploadURLResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_create_upload_url(self, client: Composio) -> None:
        with client.tool_router.session.files.with_streaming_response.create_upload_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileCreateUploadURLResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_upload_url(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.tool_router.session.files.with_raw_response.create_upload_url(
                mount_id="files",
                session_id="",
                mount_relative_path="report.pdf",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mount_id` but received ''"):
            client.tool_router.session.files.with_raw_response.create_upload_url(
                mount_id="",
                session_id="trs_123456789",
                mount_relative_path="report.pdf",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        file = await async_client.tool_router.session.files.list(
            mount_id="files",
            session_id="trs_123456789",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        file = await async_client.tool_router.session.files.list(
            mount_id="files",
            session_id="trs_123456789",
            cursor="cursor",
            limit=1,
            mount_relative_prefix="data/",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.tool_router.session.files.with_raw_response.list(
            mount_id="files",
            session_id="trs_123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.tool_router.session.files.with_streaming_response.list(
            mount_id="files",
            session_id="trs_123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.tool_router.session.files.with_raw_response.list(
                mount_id="files",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mount_id` but received ''"):
            await async_client.tool_router.session.files.with_raw_response.list(
                mount_id="",
                session_id="trs_123456789",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncComposio) -> None:
        file = await async_client.tool_router.session.files.delete(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncComposio) -> None:
        response = await async_client.tool_router.session.files.with_raw_response.delete(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncComposio) -> None:
        async with async_client.tool_router.session.files.with_streaming_response.delete(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.tool_router.session.files.with_raw_response.delete(
                mount_id="files",
                session_id="",
                mount_relative_path="report.pdf",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mount_id` but received ''"):
            await async_client.tool_router.session.files.with_raw_response.delete(
                mount_id="",
                session_id="trs_123456789",
                mount_relative_path="report.pdf",
            )

    @parametrize
    async def test_method_create_download_url(self, async_client: AsyncComposio) -> None:
        file = await async_client.tool_router.session.files.create_download_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )
        assert_matches_type(FileCreateDownloadURLResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_create_download_url(self, async_client: AsyncComposio) -> None:
        response = await async_client.tool_router.session.files.with_raw_response.create_download_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileCreateDownloadURLResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_create_download_url(self, async_client: AsyncComposio) -> None:
        async with async_client.tool_router.session.files.with_streaming_response.create_download_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileCreateDownloadURLResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_download_url(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.tool_router.session.files.with_raw_response.create_download_url(
                mount_id="files",
                session_id="",
                mount_relative_path="report.pdf",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mount_id` but received ''"):
            await async_client.tool_router.session.files.with_raw_response.create_download_url(
                mount_id="",
                session_id="trs_123456789",
                mount_relative_path="report.pdf",
            )

    @parametrize
    async def test_method_create_upload_url(self, async_client: AsyncComposio) -> None:
        file = await async_client.tool_router.session.files.create_upload_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )
        assert_matches_type(FileCreateUploadURLResponse, file, path=["response"])

    @parametrize
    async def test_method_create_upload_url_with_all_params(self, async_client: AsyncComposio) -> None:
        file = await async_client.tool_router.session.files.create_upload_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
            mimetype="application/pdf",
        )
        assert_matches_type(FileCreateUploadURLResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_create_upload_url(self, async_client: AsyncComposio) -> None:
        response = await async_client.tool_router.session.files.with_raw_response.create_upload_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileCreateUploadURLResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_create_upload_url(self, async_client: AsyncComposio) -> None:
        async with async_client.tool_router.session.files.with_streaming_response.create_upload_url(
            mount_id="files",
            session_id="trs_123456789",
            mount_relative_path="report.pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileCreateUploadURLResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_upload_url(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.tool_router.session.files.with_raw_response.create_upload_url(
                mount_id="files",
                session_id="",
                mount_relative_path="report.pdf",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mount_id` but received ''"):
            await async_client.tool_router.session.files.with_raw_response.create_upload_url(
                mount_id="",
                session_id="trs_123456789",
                mount_relative_path="report.pdf",
            )
