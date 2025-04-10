# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_sdk import ComposioSDK, AsyncComposioSDK
from composio_sdk.types.tools import (
    ExecuteInputResponse,
    ExecuteProxyResponse,
    ExecuteExecuteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecute:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_execute(self, client: ComposioSDK) -> None:
        execute = client.tools.execute.execute(
            action="action",
        )
        assert_matches_type(ExecuteExecuteResponse, execute, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: ComposioSDK) -> None:
        execute = client.tools.execute.execute(
            action="action",
            allow_tracing=True,
            arguments={"foo": "bar"},
            connected_account_id="connected_account_id",
            entity_id="entity_id",
            text="text",
            version="version",
        )
        assert_matches_type(ExecuteExecuteResponse, execute, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: ComposioSDK) -> None:
        response = client.tools.execute.with_raw_response.execute(
            action="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = response.parse()
        assert_matches_type(ExecuteExecuteResponse, execute, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: ComposioSDK) -> None:
        with client.tools.execute.with_streaming_response.execute(
            action="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = response.parse()
            assert_matches_type(ExecuteExecuteResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_execute(self, client: ComposioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            client.tools.execute.with_raw_response.execute(
                action="",
            )

    @parametrize
    def test_method_input(self, client: ComposioSDK) -> None:
        execute = client.tools.execute.input(
            action_name="actionName",
            text="text",
        )
        assert_matches_type(ExecuteInputResponse, execute, path=["response"])

    @parametrize
    def test_method_input_with_all_params(self, client: ComposioSDK) -> None:
        execute = client.tools.execute.input(
            action_name="actionName",
            text="text",
            custom_description="customDescription",
            system_prompt="systemPrompt",
            version="version",
        )
        assert_matches_type(ExecuteInputResponse, execute, path=["response"])

    @parametrize
    def test_raw_response_input(self, client: ComposioSDK) -> None:
        response = client.tools.execute.with_raw_response.input(
            action_name="actionName",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = response.parse()
        assert_matches_type(ExecuteInputResponse, execute, path=["response"])

    @parametrize
    def test_streaming_response_input(self, client: ComposioSDK) -> None:
        with client.tools.execute.with_streaming_response.input(
            action_name="actionName",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = response.parse()
            assert_matches_type(ExecuteInputResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_input(self, client: ComposioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_name` but received ''"):
            client.tools.execute.with_raw_response.input(
                action_name="",
                text="text",
            )

    @parametrize
    def test_method_proxy(self, client: ComposioSDK) -> None:
        execute = client.tools.execute.proxy(
            endpoint="endpoint",
            method="GET",
        )
        assert_matches_type(ExecuteProxyResponse, execute, path=["response"])

    @parametrize
    def test_method_proxy_with_all_params(self, client: ComposioSDK) -> None:
        execute = client.tools.execute.proxy(
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
        assert_matches_type(ExecuteProxyResponse, execute, path=["response"])

    @parametrize
    def test_raw_response_proxy(self, client: ComposioSDK) -> None:
        response = client.tools.execute.with_raw_response.proxy(
            endpoint="endpoint",
            method="GET",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = response.parse()
        assert_matches_type(ExecuteProxyResponse, execute, path=["response"])

    @parametrize
    def test_streaming_response_proxy(self, client: ComposioSDK) -> None:
        with client.tools.execute.with_streaming_response.proxy(
            endpoint="endpoint",
            method="GET",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = response.parse()
            assert_matches_type(ExecuteProxyResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExecute:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_execute(self, async_client: AsyncComposioSDK) -> None:
        execute = await async_client.tools.execute.execute(
            action="action",
        )
        assert_matches_type(ExecuteExecuteResponse, execute, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncComposioSDK) -> None:
        execute = await async_client.tools.execute.execute(
            action="action",
            allow_tracing=True,
            arguments={"foo": "bar"},
            connected_account_id="connected_account_id",
            entity_id="entity_id",
            text="text",
            version="version",
        )
        assert_matches_type(ExecuteExecuteResponse, execute, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.tools.execute.with_raw_response.execute(
            action="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = await response.parse()
        assert_matches_type(ExecuteExecuteResponse, execute, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.tools.execute.with_streaming_response.execute(
            action="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = await response.parse()
            assert_matches_type(ExecuteExecuteResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_execute(self, async_client: AsyncComposioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            await async_client.tools.execute.with_raw_response.execute(
                action="",
            )

    @parametrize
    async def test_method_input(self, async_client: AsyncComposioSDK) -> None:
        execute = await async_client.tools.execute.input(
            action_name="actionName",
            text="text",
        )
        assert_matches_type(ExecuteInputResponse, execute, path=["response"])

    @parametrize
    async def test_method_input_with_all_params(self, async_client: AsyncComposioSDK) -> None:
        execute = await async_client.tools.execute.input(
            action_name="actionName",
            text="text",
            custom_description="customDescription",
            system_prompt="systemPrompt",
            version="version",
        )
        assert_matches_type(ExecuteInputResponse, execute, path=["response"])

    @parametrize
    async def test_raw_response_input(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.tools.execute.with_raw_response.input(
            action_name="actionName",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = await response.parse()
        assert_matches_type(ExecuteInputResponse, execute, path=["response"])

    @parametrize
    async def test_streaming_response_input(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.tools.execute.with_streaming_response.input(
            action_name="actionName",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = await response.parse()
            assert_matches_type(ExecuteInputResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_input(self, async_client: AsyncComposioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_name` but received ''"):
            await async_client.tools.execute.with_raw_response.input(
                action_name="",
                text="text",
            )

    @parametrize
    async def test_method_proxy(self, async_client: AsyncComposioSDK) -> None:
        execute = await async_client.tools.execute.proxy(
            endpoint="endpoint",
            method="GET",
        )
        assert_matches_type(ExecuteProxyResponse, execute, path=["response"])

    @parametrize
    async def test_method_proxy_with_all_params(self, async_client: AsyncComposioSDK) -> None:
        execute = await async_client.tools.execute.proxy(
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
        assert_matches_type(ExecuteProxyResponse, execute, path=["response"])

    @parametrize
    async def test_raw_response_proxy(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.tools.execute.with_raw_response.proxy(
            endpoint="endpoint",
            method="GET",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = await response.parse()
        assert_matches_type(ExecuteProxyResponse, execute, path=["response"])

    @parametrize
    async def test_streaming_response_proxy(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.tools.execute.with_streaming_response.proxy(
            endpoint="endpoint",
            method="GET",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = await response.parse()
            assert_matches_type(ExecuteProxyResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True
