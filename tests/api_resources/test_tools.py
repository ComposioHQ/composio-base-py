# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    ToolListResponse,
    ToolProxyResponse,
    ToolExecuteResponse,
    ToolGetInputResponse,
    ToolRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        tool = client.tools.retrieve(
            "tool_slug",
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.tools.with_raw_response.retrieve(
            "tool_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.tools.with_streaming_response.retrieve(
            "tool_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_slug` but received ''"):
            client.tools.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        tool = client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        tool = client.tools.list(
            cursor="1",
            important="true",
            limit="20",
            search="github actions",
            tags=["string"],
            tool_slugs="github-actions,github-repos",
            toolkit_slug="github",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_execute(self, client: Composio) -> None:
        tool = client.tools.execute(
            action="action",
        )
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: Composio) -> None:
        tool = client.tools.execute(
            action="action",
            allow_tracing=True,
            arguments={"foo": "bar"},
            connected_account_id="connected_account_id",
            custom_auth_params={
                "parameters": [
                    {
                        "in": "query",
                        "name": "name",
                        "value": "string",
                    }
                ],
                "base_url": "base_url",
                "body": {"foo": "bar"},
            },
            entity_id="entity_id",
            text="text",
            version="version",
        )
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Composio) -> None:
        response = client.tools.with_raw_response.execute(
            action="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Composio) -> None:
        with client.tools.with_streaming_response.execute(
            action="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolExecuteResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_execute(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            client.tools.with_raw_response.execute(
                action="",
            )

    @parametrize
    def test_method_get_input(self, client: Composio) -> None:
        tool = client.tools.get_input(
            action_name="actionName",
            text="text",
        )
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    def test_method_get_input_with_all_params(self, client: Composio) -> None:
        tool = client.tools.get_input(
            action_name="actionName",
            text="text",
            custom_description="customDescription",
            system_prompt="systemPrompt",
            version="version",
        )
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_get_input(self, client: Composio) -> None:
        response = client.tools.with_raw_response.get_input(
            action_name="actionName",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_get_input(self, client: Composio) -> None:
        with client.tools.with_streaming_response.get_input(
            action_name="actionName",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolGetInputResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_input(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_name` but received ''"):
            client.tools.with_raw_response.get_input(
                action_name="",
                text="text",
            )

    @parametrize
    def test_method_proxy(self, client: Composio) -> None:
        tool = client.tools.proxy(
            endpoint="endpoint",
            method="GET",
        )
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    def test_method_proxy_with_all_params(self, client: Composio) -> None:
        tool = client.tools.proxy(
            endpoint="endpoint",
            method="GET",
            body={},
            connected_account_id="connected_account_id",
            parameters=[
                {
                    "name": "name",
                    "type": "header",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_proxy(self, client: Composio) -> None:
        response = client.tools.with_raw_response.proxy(
            endpoint="endpoint",
            method="GET",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_proxy(self, client: Composio) -> None:
        with client.tools.with_streaming_response.proxy(
            endpoint="endpoint",
            method="GET",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolProxyResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_enum(self, client: Composio) -> None:
        tool = client.tools.retrieve_enum()
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    def test_raw_response_retrieve_enum(self, client: Composio) -> None:
        response = client.tools.with_raw_response.retrieve_enum()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_enum(self, client: Composio) -> None:
        with client.tools.with_streaming_response.retrieve_enum() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(str, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.retrieve(
            "tool_slug",
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.retrieve(
            "tool_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.retrieve(
            "tool_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_slug` but received ''"):
            await async_client.tools.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.list(
            cursor="1",
            important="true",
            limit="20",
            search="github actions",
            tags=["string"],
            tool_slugs="github-actions,github-repos",
            toolkit_slug="github",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_execute(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.execute(
            action="action",
        )
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.execute(
            action="action",
            allow_tracing=True,
            arguments={"foo": "bar"},
            connected_account_id="connected_account_id",
            custom_auth_params={
                "parameters": [
                    {
                        "in": "query",
                        "name": "name",
                        "value": "string",
                    }
                ],
                "base_url": "base_url",
                "body": {"foo": "bar"},
            },
            entity_id="entity_id",
            text="text",
            version="version",
        )
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.execute(
            action="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.execute(
            action="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolExecuteResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_execute(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            await async_client.tools.with_raw_response.execute(
                action="",
            )

    @parametrize
    async def test_method_get_input(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.get_input(
            action_name="actionName",
            text="text",
        )
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    async def test_method_get_input_with_all_params(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.get_input(
            action_name="actionName",
            text="text",
            custom_description="customDescription",
            system_prompt="systemPrompt",
            version="version",
        )
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_get_input(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.get_input(
            action_name="actionName",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_get_input(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.get_input(
            action_name="actionName",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolGetInputResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_input(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_name` but received ''"):
            await async_client.tools.with_raw_response.get_input(
                action_name="",
                text="text",
            )

    @parametrize
    async def test_method_proxy(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.proxy(
            endpoint="endpoint",
            method="GET",
        )
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    async def test_method_proxy_with_all_params(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.proxy(
            endpoint="endpoint",
            method="GET",
            body={},
            connected_account_id="connected_account_id",
            parameters=[
                {
                    "name": "name",
                    "type": "header",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_proxy(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.proxy(
            endpoint="endpoint",
            method="GET",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_proxy(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.proxy(
            endpoint="endpoint",
            method="GET",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolProxyResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_enum(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.retrieve_enum()
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_enum(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.retrieve_enum()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_enum(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.retrieve_enum() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(str, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
