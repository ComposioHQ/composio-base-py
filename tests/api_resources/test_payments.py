# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_sdk import ComposioSDK, AsyncComposioSDK
from composio_sdk.types import (
    PaymentCreateSessionResponse,
    PaymentManageSubscriptionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_session(self, client: ComposioSDK) -> None:
        payment = client.payments.create_session(
            apply_discount=True,
            plan="HOBBY",
        )
        assert_matches_type(PaymentCreateSessionResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_create_session(self, client: ComposioSDK) -> None:
        response = client.payments.with_raw_response.create_session(
            apply_discount=True,
            plan="HOBBY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreateSessionResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_create_session(self, client: ComposioSDK) -> None:
        with client.payments.with_streaming_response.create_session(
            apply_discount=True,
            plan="HOBBY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentCreateSessionResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_manage_subscription(self, client: ComposioSDK) -> None:
        payment = client.payments.manage_subscription()
        assert_matches_type(PaymentManageSubscriptionResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_manage_subscription(self, client: ComposioSDK) -> None:
        response = client.payments.with_raw_response.manage_subscription()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentManageSubscriptionResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_manage_subscription(self, client: ComposioSDK) -> None:
        with client.payments.with_streaming_response.manage_subscription() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentManageSubscriptionResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_session(self, async_client: AsyncComposioSDK) -> None:
        payment = await async_client.payments.create_session(
            apply_discount=True,
            plan="HOBBY",
        )
        assert_matches_type(PaymentCreateSessionResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.payments.with_raw_response.create_session(
            apply_discount=True,
            plan="HOBBY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentCreateSessionResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.payments.with_streaming_response.create_session(
            apply_discount=True,
            plan="HOBBY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentCreateSessionResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_manage_subscription(self, async_client: AsyncComposioSDK) -> None:
        payment = await async_client.payments.manage_subscription()
        assert_matches_type(PaymentManageSubscriptionResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_manage_subscription(self, async_client: AsyncComposioSDK) -> None:
        response = await async_client.payments.with_raw_response.manage_subscription()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentManageSubscriptionResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_manage_subscription(self, async_client: AsyncComposioSDK) -> None:
        async with async_client.payments.with_streaming_response.manage_subscription() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentManageSubscriptionResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
