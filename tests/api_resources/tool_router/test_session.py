# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types.tool_router import (
    SessionLinkResponse,
    SessionCreateResponse,
    SessionExecuteResponse,
    SessionRetrieveResponse,
    SessionToolkitsResponse,
    SessionExecuteMetaResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Composio) -> None:
        session = client.tool_router.session.create(
            user_id="user_123456789",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Composio) -> None:
        session = client.tool_router.session.create(
            user_id="user_123456789",
            auth_configs={
                "gmail": "ac_1223434343",
                "slack": "ac_23343434343434",
            },
            connected_accounts={"github": "ca_34454545454545"},
            manage_connections={
                "callback_url": "https://your-app.com/auth/callback",
                "enable": True,
            },
            tags=["readOnlyHint", "destructiveHint"],
            toolkits={"enable": ["gmail", "slack", "github"]},
            tools={
                "gmail": {"enable": ["GMAIL_SEND_EMAIL", "GMAIL_FETCH_EMAILS"]},
                "slack": {"disable": ["SLACK_ADD_EMOJI"]},
                "slack_bot": {"tags": ["destructiveHint"]},
            },
            workbench={
                "auto_offload_threshold": 20000,
                "enable_proxy_execution": True,
            },
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Composio) -> None:
        response = client.tool_router.session.with_raw_response.create(
            user_id="user_123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Composio) -> None:
        with client.tool_router.session.with_streaming_response.create(
            user_id="user_123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        session = client.tool_router.session.retrieve(
            "trs_123456789",
        )
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.tool_router.session.with_raw_response.retrieve(
            "trs_123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.tool_router.session.with_streaming_response.retrieve(
            "trs_123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionRetrieveResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.tool_router.session.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_execute(self, client: Composio) -> None:
        session = client.tool_router.session.execute(
            session_id="trs_LX9uJKBinWWr",
            tool_slug="GITHUB_CREATE_ISSUE",
        )
        assert_matches_type(SessionExecuteResponse, session, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: Composio) -> None:
        session = client.tool_router.session.execute(
            session_id="trs_LX9uJKBinWWr",
            tool_slug="GITHUB_CREATE_ISSUE",
            arguments={
                "repository": "bar",
                "workflow_id": "bar",
                "ref": "bar",
                "inputs": "bar",
            },
        )
        assert_matches_type(SessionExecuteResponse, session, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Composio) -> None:
        response = client.tool_router.session.with_raw_response.execute(
            session_id="trs_LX9uJKBinWWr",
            tool_slug="GITHUB_CREATE_ISSUE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionExecuteResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Composio) -> None:
        with client.tool_router.session.with_streaming_response.execute(
            session_id="trs_LX9uJKBinWWr",
            tool_slug="GITHUB_CREATE_ISSUE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionExecuteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_execute(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.tool_router.session.with_raw_response.execute(
                session_id="",
                tool_slug="GITHUB_CREATE_ISSUE",
            )

    @parametrize
    def test_method_execute_meta(self, client: Composio) -> None:
        session = client.tool_router.session.execute_meta(
            session_id="trs_LX9uJKBinWWr",
            slug="COMPOSIO_MANAGE_CONNECTIONS",
        )
        assert_matches_type(SessionExecuteMetaResponse, session, path=["response"])

    @parametrize
    def test_method_execute_meta_with_all_params(self, client: Composio) -> None:
        session = client.tool_router.session.execute_meta(
            session_id="trs_LX9uJKBinWWr",
            slug="COMPOSIO_MANAGE_CONNECTIONS",
            arguments={
                "toolkits": "bar",
                "reinitiate_all": "bar",
            },
        )
        assert_matches_type(SessionExecuteMetaResponse, session, path=["response"])

    @parametrize
    def test_raw_response_execute_meta(self, client: Composio) -> None:
        response = client.tool_router.session.with_raw_response.execute_meta(
            session_id="trs_LX9uJKBinWWr",
            slug="COMPOSIO_MANAGE_CONNECTIONS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionExecuteMetaResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_execute_meta(self, client: Composio) -> None:
        with client.tool_router.session.with_streaming_response.execute_meta(
            session_id="trs_LX9uJKBinWWr",
            slug="COMPOSIO_MANAGE_CONNECTIONS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionExecuteMetaResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_execute_meta(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.tool_router.session.with_raw_response.execute_meta(
                session_id="",
                slug="COMPOSIO_MANAGE_CONNECTIONS",
            )

    @parametrize
    def test_method_link(self, client: Composio) -> None:
        session = client.tool_router.session.link(
            session_id="trs_LX9uJKBinWWr",
            toolkit="github",
        )
        assert_matches_type(SessionLinkResponse, session, path=["response"])

    @parametrize
    def test_method_link_with_all_params(self, client: Composio) -> None:
        session = client.tool_router.session.link(
            session_id="trs_LX9uJKBinWWr",
            toolkit="github",
            callback_url="https://myapp.com/callback",
        )
        assert_matches_type(SessionLinkResponse, session, path=["response"])

    @parametrize
    def test_raw_response_link(self, client: Composio) -> None:
        response = client.tool_router.session.with_raw_response.link(
            session_id="trs_LX9uJKBinWWr",
            toolkit="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionLinkResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_link(self, client: Composio) -> None:
        with client.tool_router.session.with_streaming_response.link(
            session_id="trs_LX9uJKBinWWr",
            toolkit="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionLinkResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_link(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.tool_router.session.with_raw_response.link(
                session_id="",
                toolkit="github",
            )

    @parametrize
    def test_method_toolkits(self, client: Composio) -> None:
        session = client.tool_router.session.toolkits(
            session_id="trs_123456789",
        )
        assert_matches_type(SessionToolkitsResponse, session, path=["response"])

    @parametrize
    def test_method_toolkits_with_all_params(self, client: Composio) -> None:
        session = client.tool_router.session.toolkits(
            session_id="trs_123456789",
            cursor="cursor",
            is_connected=True,
            limit=0,
            toolkits=["string"],
        )
        assert_matches_type(SessionToolkitsResponse, session, path=["response"])

    @parametrize
    def test_raw_response_toolkits(self, client: Composio) -> None:
        response = client.tool_router.session.with_raw_response.toolkits(
            session_id="trs_123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionToolkitsResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_toolkits(self, client: Composio) -> None:
        with client.tool_router.session.with_streaming_response.toolkits(
            session_id="trs_123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionToolkitsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_toolkits(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.tool_router.session.with_raw_response.toolkits(
                session_id="",
            )


class TestAsyncSession:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncComposio) -> None:
        session = await async_client.tool_router.session.create(
            user_id="user_123456789",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncComposio) -> None:
        session = await async_client.tool_router.session.create(
            user_id="user_123456789",
            auth_configs={
                "gmail": "ac_1223434343",
                "slack": "ac_23343434343434",
            },
            connected_accounts={"github": "ca_34454545454545"},
            manage_connections={
                "callback_url": "https://your-app.com/auth/callback",
                "enable": True,
            },
            tags=["readOnlyHint", "destructiveHint"],
            toolkits={"enable": ["gmail", "slack", "github"]},
            tools={
                "gmail": {"enable": ["GMAIL_SEND_EMAIL", "GMAIL_FETCH_EMAILS"]},
                "slack": {"disable": ["SLACK_ADD_EMOJI"]},
                "slack_bot": {"tags": ["destructiveHint"]},
            },
            workbench={
                "auto_offload_threshold": 20000,
                "enable_proxy_execution": True,
            },
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncComposio) -> None:
        response = await async_client.tool_router.session.with_raw_response.create(
            user_id="user_123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncComposio) -> None:
        async with async_client.tool_router.session.with_streaming_response.create(
            user_id="user_123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        session = await async_client.tool_router.session.retrieve(
            "trs_123456789",
        )
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.tool_router.session.with_raw_response.retrieve(
            "trs_123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.tool_router.session.with_streaming_response.retrieve(
            "trs_123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionRetrieveResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.tool_router.session.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_execute(self, async_client: AsyncComposio) -> None:
        session = await async_client.tool_router.session.execute(
            session_id="trs_LX9uJKBinWWr",
            tool_slug="GITHUB_CREATE_ISSUE",
        )
        assert_matches_type(SessionExecuteResponse, session, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncComposio) -> None:
        session = await async_client.tool_router.session.execute(
            session_id="trs_LX9uJKBinWWr",
            tool_slug="GITHUB_CREATE_ISSUE",
            arguments={
                "repository": "bar",
                "workflow_id": "bar",
                "ref": "bar",
                "inputs": "bar",
            },
        )
        assert_matches_type(SessionExecuteResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncComposio) -> None:
        response = await async_client.tool_router.session.with_raw_response.execute(
            session_id="trs_LX9uJKBinWWr",
            tool_slug="GITHUB_CREATE_ISSUE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionExecuteResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncComposio) -> None:
        async with async_client.tool_router.session.with_streaming_response.execute(
            session_id="trs_LX9uJKBinWWr",
            tool_slug="GITHUB_CREATE_ISSUE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionExecuteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_execute(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.tool_router.session.with_raw_response.execute(
                session_id="",
                tool_slug="GITHUB_CREATE_ISSUE",
            )

    @parametrize
    async def test_method_execute_meta(self, async_client: AsyncComposio) -> None:
        session = await async_client.tool_router.session.execute_meta(
            session_id="trs_LX9uJKBinWWr",
            slug="COMPOSIO_MANAGE_CONNECTIONS",
        )
        assert_matches_type(SessionExecuteMetaResponse, session, path=["response"])

    @parametrize
    async def test_method_execute_meta_with_all_params(self, async_client: AsyncComposio) -> None:
        session = await async_client.tool_router.session.execute_meta(
            session_id="trs_LX9uJKBinWWr",
            slug="COMPOSIO_MANAGE_CONNECTIONS",
            arguments={
                "toolkits": "bar",
                "reinitiate_all": "bar",
            },
        )
        assert_matches_type(SessionExecuteMetaResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_execute_meta(self, async_client: AsyncComposio) -> None:
        response = await async_client.tool_router.session.with_raw_response.execute_meta(
            session_id="trs_LX9uJKBinWWr",
            slug="COMPOSIO_MANAGE_CONNECTIONS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionExecuteMetaResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_execute_meta(self, async_client: AsyncComposio) -> None:
        async with async_client.tool_router.session.with_streaming_response.execute_meta(
            session_id="trs_LX9uJKBinWWr",
            slug="COMPOSIO_MANAGE_CONNECTIONS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionExecuteMetaResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_execute_meta(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.tool_router.session.with_raw_response.execute_meta(
                session_id="",
                slug="COMPOSIO_MANAGE_CONNECTIONS",
            )

    @parametrize
    async def test_method_link(self, async_client: AsyncComposio) -> None:
        session = await async_client.tool_router.session.link(
            session_id="trs_LX9uJKBinWWr",
            toolkit="github",
        )
        assert_matches_type(SessionLinkResponse, session, path=["response"])

    @parametrize
    async def test_method_link_with_all_params(self, async_client: AsyncComposio) -> None:
        session = await async_client.tool_router.session.link(
            session_id="trs_LX9uJKBinWWr",
            toolkit="github",
            callback_url="https://myapp.com/callback",
        )
        assert_matches_type(SessionLinkResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_link(self, async_client: AsyncComposio) -> None:
        response = await async_client.tool_router.session.with_raw_response.link(
            session_id="trs_LX9uJKBinWWr",
            toolkit="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionLinkResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_link(self, async_client: AsyncComposio) -> None:
        async with async_client.tool_router.session.with_streaming_response.link(
            session_id="trs_LX9uJKBinWWr",
            toolkit="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionLinkResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_link(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.tool_router.session.with_raw_response.link(
                session_id="",
                toolkit="github",
            )

    @parametrize
    async def test_method_toolkits(self, async_client: AsyncComposio) -> None:
        session = await async_client.tool_router.session.toolkits(
            session_id="trs_123456789",
        )
        assert_matches_type(SessionToolkitsResponse, session, path=["response"])

    @parametrize
    async def test_method_toolkits_with_all_params(self, async_client: AsyncComposio) -> None:
        session = await async_client.tool_router.session.toolkits(
            session_id="trs_123456789",
            cursor="cursor",
            is_connected=True,
            limit=0,
            toolkits=["string"],
        )
        assert_matches_type(SessionToolkitsResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_toolkits(self, async_client: AsyncComposio) -> None:
        response = await async_client.tool_router.session.with_raw_response.toolkits(
            session_id="trs_123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionToolkitsResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_toolkits(self, async_client: AsyncComposio) -> None:
        async with async_client.tool_router.session.with_streaming_response.toolkits(
            session_id="trs_123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionToolkitsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_toolkits(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.tool_router.session.with_raw_response.toolkits(
                session_id="",
            )
