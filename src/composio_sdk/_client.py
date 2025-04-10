# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    admin,
    trigger,
    payments,
    toolkits,
    auth_configs,
    team_members,
    triggers_types,
    action_execution,
    connected_accounts,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.org import org
from .resources.auth import auth
from .resources.tools import tools
from .resources.trigger_instances import trigger_instances

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "ComposioSDK",
    "AsyncComposioSDK",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://backend.composio.dev",
    "staging": "https://staging-backend.composio.dev",
    "local": "http://localhost:9901",
}


class ComposioSDK(SyncAPIClient):
    auth: auth.AuthResource
    admin: admin.AdminResource
    auth_configs: auth_configs.AuthConfigsResource
    connected_accounts: connected_accounts.ConnectedAccountsResource
    trigger: trigger.TriggerResource
    action_execution: action_execution.ActionExecutionResource
    org: org.OrgResource
    team_members: team_members.TeamMembersResource
    toolkits: toolkits.ToolkitsResource
    tools: tools.ToolsResource
    trigger_instances: trigger_instances.TriggerInstancesResource
    triggers_types: triggers_types.TriggersTypesResource
    payments: payments.PaymentsResource
    with_raw_response: ComposioSDKWithRawResponse
    with_streaming_response: ComposioSDKWithStreamedResponse

    # client options
    api_key: str | None

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous ComposioSDK client instance.

        This automatically infers the `api_key` argument from the `COMPOSIO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COMPOSIO_API_KEY")
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("COMPOSIO_SDK_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `COMPOSIO_SDK_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.auth = auth.AuthResource(self)
        self.admin = admin.AdminResource(self)
        self.auth_configs = auth_configs.AuthConfigsResource(self)
        self.connected_accounts = connected_accounts.ConnectedAccountsResource(self)
        self.trigger = trigger.TriggerResource(self)
        self.action_execution = action_execution.ActionExecutionResource(self)
        self.org = org.OrgResource(self)
        self.team_members = team_members.TeamMembersResource(self)
        self.toolkits = toolkits.ToolkitsResource(self)
        self.tools = tools.ToolsResource(self)
        self.trigger_instances = trigger_instances.TriggerInstancesResource(self)
        self.triggers_types = triggers_types.TriggersTypesResource(self)
        self.payments = payments.PaymentsResource(self)
        self.with_raw_response = ComposioSDKWithRawResponse(self)
        self.with_streaming_response = ComposioSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncComposioSDK(AsyncAPIClient):
    auth: auth.AsyncAuthResource
    admin: admin.AsyncAdminResource
    auth_configs: auth_configs.AsyncAuthConfigsResource
    connected_accounts: connected_accounts.AsyncConnectedAccountsResource
    trigger: trigger.AsyncTriggerResource
    action_execution: action_execution.AsyncActionExecutionResource
    org: org.AsyncOrgResource
    team_members: team_members.AsyncTeamMembersResource
    toolkits: toolkits.AsyncToolkitsResource
    tools: tools.AsyncToolsResource
    trigger_instances: trigger_instances.AsyncTriggerInstancesResource
    triggers_types: triggers_types.AsyncTriggersTypesResource
    payments: payments.AsyncPaymentsResource
    with_raw_response: AsyncComposioSDKWithRawResponse
    with_streaming_response: AsyncComposioSDKWithStreamedResponse

    # client options
    api_key: str | None

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncComposioSDK client instance.

        This automatically infers the `api_key` argument from the `COMPOSIO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COMPOSIO_API_KEY")
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("COMPOSIO_SDK_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `COMPOSIO_SDK_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.auth = auth.AsyncAuthResource(self)
        self.admin = admin.AsyncAdminResource(self)
        self.auth_configs = auth_configs.AsyncAuthConfigsResource(self)
        self.connected_accounts = connected_accounts.AsyncConnectedAccountsResource(self)
        self.trigger = trigger.AsyncTriggerResource(self)
        self.action_execution = action_execution.AsyncActionExecutionResource(self)
        self.org = org.AsyncOrgResource(self)
        self.team_members = team_members.AsyncTeamMembersResource(self)
        self.toolkits = toolkits.AsyncToolkitsResource(self)
        self.tools = tools.AsyncToolsResource(self)
        self.trigger_instances = trigger_instances.AsyncTriggerInstancesResource(self)
        self.triggers_types = triggers_types.AsyncTriggersTypesResource(self)
        self.payments = payments.AsyncPaymentsResource(self)
        self.with_raw_response = AsyncComposioSDKWithRawResponse(self)
        self.with_streaming_response = AsyncComposioSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ComposioSDKWithRawResponse:
    def __init__(self, client: ComposioSDK) -> None:
        self.auth = auth.AuthResourceWithRawResponse(client.auth)
        self.admin = admin.AdminResourceWithRawResponse(client.admin)
        self.auth_configs = auth_configs.AuthConfigsResourceWithRawResponse(client.auth_configs)
        self.connected_accounts = connected_accounts.ConnectedAccountsResourceWithRawResponse(client.connected_accounts)
        self.trigger = trigger.TriggerResourceWithRawResponse(client.trigger)
        self.action_execution = action_execution.ActionExecutionResourceWithRawResponse(client.action_execution)
        self.org = org.OrgResourceWithRawResponse(client.org)
        self.team_members = team_members.TeamMembersResourceWithRawResponse(client.team_members)
        self.toolkits = toolkits.ToolkitsResourceWithRawResponse(client.toolkits)
        self.tools = tools.ToolsResourceWithRawResponse(client.tools)
        self.trigger_instances = trigger_instances.TriggerInstancesResourceWithRawResponse(client.trigger_instances)
        self.triggers_types = triggers_types.TriggersTypesResourceWithRawResponse(client.triggers_types)
        self.payments = payments.PaymentsResourceWithRawResponse(client.payments)


class AsyncComposioSDKWithRawResponse:
    def __init__(self, client: AsyncComposioSDK) -> None:
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)
        self.admin = admin.AsyncAdminResourceWithRawResponse(client.admin)
        self.auth_configs = auth_configs.AsyncAuthConfigsResourceWithRawResponse(client.auth_configs)
        self.connected_accounts = connected_accounts.AsyncConnectedAccountsResourceWithRawResponse(
            client.connected_accounts
        )
        self.trigger = trigger.AsyncTriggerResourceWithRawResponse(client.trigger)
        self.action_execution = action_execution.AsyncActionExecutionResourceWithRawResponse(client.action_execution)
        self.org = org.AsyncOrgResourceWithRawResponse(client.org)
        self.team_members = team_members.AsyncTeamMembersResourceWithRawResponse(client.team_members)
        self.toolkits = toolkits.AsyncToolkitsResourceWithRawResponse(client.toolkits)
        self.tools = tools.AsyncToolsResourceWithRawResponse(client.tools)
        self.trigger_instances = trigger_instances.AsyncTriggerInstancesResourceWithRawResponse(
            client.trigger_instances
        )
        self.triggers_types = triggers_types.AsyncTriggersTypesResourceWithRawResponse(client.triggers_types)
        self.payments = payments.AsyncPaymentsResourceWithRawResponse(client.payments)


class ComposioSDKWithStreamedResponse:
    def __init__(self, client: ComposioSDK) -> None:
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)
        self.admin = admin.AdminResourceWithStreamingResponse(client.admin)
        self.auth_configs = auth_configs.AuthConfigsResourceWithStreamingResponse(client.auth_configs)
        self.connected_accounts = connected_accounts.ConnectedAccountsResourceWithStreamingResponse(
            client.connected_accounts
        )
        self.trigger = trigger.TriggerResourceWithStreamingResponse(client.trigger)
        self.action_execution = action_execution.ActionExecutionResourceWithStreamingResponse(client.action_execution)
        self.org = org.OrgResourceWithStreamingResponse(client.org)
        self.team_members = team_members.TeamMembersResourceWithStreamingResponse(client.team_members)
        self.toolkits = toolkits.ToolkitsResourceWithStreamingResponse(client.toolkits)
        self.tools = tools.ToolsResourceWithStreamingResponse(client.tools)
        self.trigger_instances = trigger_instances.TriggerInstancesResourceWithStreamingResponse(
            client.trigger_instances
        )
        self.triggers_types = triggers_types.TriggersTypesResourceWithStreamingResponse(client.triggers_types)
        self.payments = payments.PaymentsResourceWithStreamingResponse(client.payments)


class AsyncComposioSDKWithStreamedResponse:
    def __init__(self, client: AsyncComposioSDK) -> None:
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.admin = admin.AsyncAdminResourceWithStreamingResponse(client.admin)
        self.auth_configs = auth_configs.AsyncAuthConfigsResourceWithStreamingResponse(client.auth_configs)
        self.connected_accounts = connected_accounts.AsyncConnectedAccountsResourceWithStreamingResponse(
            client.connected_accounts
        )
        self.trigger = trigger.AsyncTriggerResourceWithStreamingResponse(client.trigger)
        self.action_execution = action_execution.AsyncActionExecutionResourceWithStreamingResponse(
            client.action_execution
        )
        self.org = org.AsyncOrgResourceWithStreamingResponse(client.org)
        self.team_members = team_members.AsyncTeamMembersResourceWithStreamingResponse(client.team_members)
        self.toolkits = toolkits.AsyncToolkitsResourceWithStreamingResponse(client.toolkits)
        self.tools = tools.AsyncToolsResourceWithStreamingResponse(client.tools)
        self.trigger_instances = trigger_instances.AsyncTriggerInstancesResourceWithStreamingResponse(
            client.trigger_instances
        )
        self.triggers_types = triggers_types.AsyncTriggersTypesResourceWithStreamingResponse(client.triggers_types)
        self.payments = payments.AsyncPaymentsResourceWithStreamingResponse(client.payments)


Client = ComposioSDK

AsyncClient = AsyncComposioSDK
