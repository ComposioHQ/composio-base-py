# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    TeamMemberListResponse,
    TeamMemberInviteResponse,
    TeamMemberRemoveResponse,
    TeamMemberUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeamMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Composio) -> None:
        team_member = client.team_members.update(
            id="tm_123456",
            email="dev@stainless.com",
            name="name",
            role="role",
        )
        assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Composio) -> None:
        response = client.team_members.with_raw_response.update(
            id="tm_123456",
            email="dev@stainless.com",
            name="name",
            role="role",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Composio) -> None:
        with client.team_members.with_streaming_response.update(
            id="tm_123456",
            email="dev@stainless.com",
            name="name",
            role="role",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.team_members.with_raw_response.update(
                id="",
                email="dev@stainless.com",
                name="name",
                role="role",
            )

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        team_member = client.team_members.list()
        assert_matches_type(TeamMemberListResponse, team_member, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.team_members.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert_matches_type(TeamMemberListResponse, team_member, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.team_members.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert_matches_type(TeamMemberListResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_invite(self, client: Composio) -> None:
        team_member = client.team_members.invite(
            email="dev@stainless.com",
            name="name",
            role="role",
        )
        assert_matches_type(TeamMemberInviteResponse, team_member, path=["response"])

    @parametrize
    def test_method_invite_with_all_params(self, client: Composio) -> None:
        team_member = client.team_members.invite(
            email="dev@stainless.com",
            name="name",
            role="role",
            verify_host="verifyHost",
        )
        assert_matches_type(TeamMemberInviteResponse, team_member, path=["response"])

    @parametrize
    def test_raw_response_invite(self, client: Composio) -> None:
        response = client.team_members.with_raw_response.invite(
            email="dev@stainless.com",
            name="name",
            role="role",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert_matches_type(TeamMemberInviteResponse, team_member, path=["response"])

    @parametrize
    def test_streaming_response_invite(self, client: Composio) -> None:
        with client.team_members.with_streaming_response.invite(
            email="dev@stainless.com",
            name="name",
            role="role",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert_matches_type(TeamMemberInviteResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove(self, client: Composio) -> None:
        team_member = client.team_members.remove(
            "tm_123456",
        )
        assert_matches_type(TeamMemberRemoveResponse, team_member, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Composio) -> None:
        response = client.team_members.with_raw_response.remove(
            "tm_123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert_matches_type(TeamMemberRemoveResponse, team_member, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Composio) -> None:
        with client.team_members.with_streaming_response.remove(
            "tm_123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert_matches_type(TeamMemberRemoveResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.team_members.with_raw_response.remove(
                "",
            )


class TestAsyncTeamMembers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncComposio) -> None:
        team_member = await async_client.team_members.update(
            id="tm_123456",
            email="dev@stainless.com",
            name="name",
            role="role",
        )
        assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncComposio) -> None:
        response = await async_client.team_members.with_raw_response.update(
            id="tm_123456",
            email="dev@stainless.com",
            name="name",
            role="role",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncComposio) -> None:
        async with async_client.team_members.with_streaming_response.update(
            id="tm_123456",
            email="dev@stainless.com",
            name="name",
            role="role",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.team_members.with_raw_response.update(
                id="",
                email="dev@stainless.com",
                name="name",
                role="role",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        team_member = await async_client.team_members.list()
        assert_matches_type(TeamMemberListResponse, team_member, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.team_members.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert_matches_type(TeamMemberListResponse, team_member, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.team_members.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert_matches_type(TeamMemberListResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_invite(self, async_client: AsyncComposio) -> None:
        team_member = await async_client.team_members.invite(
            email="dev@stainless.com",
            name="name",
            role="role",
        )
        assert_matches_type(TeamMemberInviteResponse, team_member, path=["response"])

    @parametrize
    async def test_method_invite_with_all_params(self, async_client: AsyncComposio) -> None:
        team_member = await async_client.team_members.invite(
            email="dev@stainless.com",
            name="name",
            role="role",
            verify_host="verifyHost",
        )
        assert_matches_type(TeamMemberInviteResponse, team_member, path=["response"])

    @parametrize
    async def test_raw_response_invite(self, async_client: AsyncComposio) -> None:
        response = await async_client.team_members.with_raw_response.invite(
            email="dev@stainless.com",
            name="name",
            role="role",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert_matches_type(TeamMemberInviteResponse, team_member, path=["response"])

    @parametrize
    async def test_streaming_response_invite(self, async_client: AsyncComposio) -> None:
        async with async_client.team_members.with_streaming_response.invite(
            email="dev@stainless.com",
            name="name",
            role="role",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert_matches_type(TeamMemberInviteResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove(self, async_client: AsyncComposio) -> None:
        team_member = await async_client.team_members.remove(
            "tm_123456",
        )
        assert_matches_type(TeamMemberRemoveResponse, team_member, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncComposio) -> None:
        response = await async_client.team_members.with_raw_response.remove(
            "tm_123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert_matches_type(TeamMemberRemoveResponse, team_member, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncComposio) -> None:
        async with async_client.team_members.with_streaming_response.remove(
            "tm_123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert_matches_type(TeamMemberRemoveResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.team_members.with_raw_response.remove(
                "",
            )
