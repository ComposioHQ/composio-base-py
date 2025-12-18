# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        cli,
        mcp,
        link,
        files,
        tools,
        toolkits,
        migration,
        tool_router,
        auth_configs,
        triggers_types,
        trigger_instances,
        connected_accounts,
    )
    from .resources.cli import CliResource, AsyncCliResource
    from .resources.link import LinkResource, AsyncLinkResource
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.tools import ToolsResource, AsyncToolsResource
    from .resources.mcp.mcp import McpResource, AsyncMcpResource
    from .resources.toolkits import ToolkitsResource, AsyncToolkitsResource
    from .resources.migration import MigrationResource, AsyncMigrationResource
    from .resources.auth_configs import AuthConfigsResource, AsyncAuthConfigsResource
    from .resources.triggers_types import TriggersTypesResource, AsyncTriggersTypesResource
    from .resources.connected_accounts import ConnectedAccountsResource, AsyncConnectedAccountsResource
    from .resources.tool_router.tool_router import ToolRouterResource, AsyncToolRouterResource
    from .resources.trigger_instances.trigger_instances import TriggerInstancesResource, AsyncTriggerInstancesResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Composio",
    "AsyncComposio",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://backend.composio.dev",
    "staging": "https://staging-backend.composio.dev",
    "local": "http://localhost:9900",
}


class Composio(SyncAPIClient):
    # client options
    api_key: str | None

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new synchronous Composio client instance.

        This automatically infers the `api_key` argument from the `COMPOSIO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COMPOSIO_API_KEY")
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("COMPOSIO_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `COMPOSIO_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
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

    @cached_property
    def auth_configs(self) -> AuthConfigsResource:
        from .resources.auth_configs import AuthConfigsResource

        return AuthConfigsResource(self)

    @cached_property
    def connected_accounts(self) -> ConnectedAccountsResource:
        from .resources.connected_accounts import ConnectedAccountsResource

        return ConnectedAccountsResource(self)

    @cached_property
    def link(self) -> LinkResource:
        from .resources.link import LinkResource

        return LinkResource(self)

    @cached_property
    def toolkits(self) -> ToolkitsResource:
        from .resources.toolkits import ToolkitsResource

        return ToolkitsResource(self)

    @cached_property
    def tools(self) -> ToolsResource:
        from .resources.tools import ToolsResource

        return ToolsResource(self)

    @cached_property
    def trigger_instances(self) -> TriggerInstancesResource:
        from .resources.trigger_instances import TriggerInstancesResource

        return TriggerInstancesResource(self)

    @cached_property
    def triggers_types(self) -> TriggersTypesResource:
        from .resources.triggers_types import TriggersTypesResource

        return TriggersTypesResource(self)

    @cached_property
    def mcp(self) -> McpResource:
        from .resources.mcp import McpResource

        return McpResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def migration(self) -> MigrationResource:
        from .resources.migration import MigrationResource

        return MigrationResource(self)

    @cached_property
    def cli(self) -> CliResource:
        from .resources.cli import CliResource

        return CliResource(self)

    @cached_property
    def tool_router(self) -> ToolRouterResource:
        from .resources.tool_router import ToolRouterResource

        return ToolRouterResource(self)

    @cached_property
    def with_raw_response(self) -> ComposioWithRawResponse:
        return ComposioWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComposioWithStreamedResponse:
        return ComposioWithStreamedResponse(self)

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
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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


class AsyncComposio(AsyncAPIClient):
    # client options
    api_key: str | None

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new async AsyncComposio client instance.

        This automatically infers the `api_key` argument from the `COMPOSIO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COMPOSIO_API_KEY")
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("COMPOSIO_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `COMPOSIO_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
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

    @cached_property
    def auth_configs(self) -> AsyncAuthConfigsResource:
        from .resources.auth_configs import AsyncAuthConfigsResource

        return AsyncAuthConfigsResource(self)

    @cached_property
    def connected_accounts(self) -> AsyncConnectedAccountsResource:
        from .resources.connected_accounts import AsyncConnectedAccountsResource

        return AsyncConnectedAccountsResource(self)

    @cached_property
    def link(self) -> AsyncLinkResource:
        from .resources.link import AsyncLinkResource

        return AsyncLinkResource(self)

    @cached_property
    def toolkits(self) -> AsyncToolkitsResource:
        from .resources.toolkits import AsyncToolkitsResource

        return AsyncToolkitsResource(self)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        from .resources.tools import AsyncToolsResource

        return AsyncToolsResource(self)

    @cached_property
    def trigger_instances(self) -> AsyncTriggerInstancesResource:
        from .resources.trigger_instances import AsyncTriggerInstancesResource

        return AsyncTriggerInstancesResource(self)

    @cached_property
    def triggers_types(self) -> AsyncTriggersTypesResource:
        from .resources.triggers_types import AsyncTriggersTypesResource

        return AsyncTriggersTypesResource(self)

    @cached_property
    def mcp(self) -> AsyncMcpResource:
        from .resources.mcp import AsyncMcpResource

        return AsyncMcpResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def migration(self) -> AsyncMigrationResource:
        from .resources.migration import AsyncMigrationResource

        return AsyncMigrationResource(self)

    @cached_property
    def cli(self) -> AsyncCliResource:
        from .resources.cli import AsyncCliResource

        return AsyncCliResource(self)

    @cached_property
    def tool_router(self) -> AsyncToolRouterResource:
        from .resources.tool_router import AsyncToolRouterResource

        return AsyncToolRouterResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncComposioWithRawResponse:
        return AsyncComposioWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComposioWithStreamedResponse:
        return AsyncComposioWithStreamedResponse(self)

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
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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


class ComposioWithRawResponse:
    _client: Composio

    def __init__(self, client: Composio) -> None:
        self._client = client

    @cached_property
    def auth_configs(self) -> auth_configs.AuthConfigsResourceWithRawResponse:
        from .resources.auth_configs import AuthConfigsResourceWithRawResponse

        return AuthConfigsResourceWithRawResponse(self._client.auth_configs)

    @cached_property
    def connected_accounts(self) -> connected_accounts.ConnectedAccountsResourceWithRawResponse:
        from .resources.connected_accounts import ConnectedAccountsResourceWithRawResponse

        return ConnectedAccountsResourceWithRawResponse(self._client.connected_accounts)

    @cached_property
    def link(self) -> link.LinkResourceWithRawResponse:
        from .resources.link import LinkResourceWithRawResponse

        return LinkResourceWithRawResponse(self._client.link)

    @cached_property
    def toolkits(self) -> toolkits.ToolkitsResourceWithRawResponse:
        from .resources.toolkits import ToolkitsResourceWithRawResponse

        return ToolkitsResourceWithRawResponse(self._client.toolkits)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithRawResponse:
        from .resources.tools import ToolsResourceWithRawResponse

        return ToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def trigger_instances(self) -> trigger_instances.TriggerInstancesResourceWithRawResponse:
        from .resources.trigger_instances import TriggerInstancesResourceWithRawResponse

        return TriggerInstancesResourceWithRawResponse(self._client.trigger_instances)

    @cached_property
    def triggers_types(self) -> triggers_types.TriggersTypesResourceWithRawResponse:
        from .resources.triggers_types import TriggersTypesResourceWithRawResponse

        return TriggersTypesResourceWithRawResponse(self._client.triggers_types)

    @cached_property
    def mcp(self) -> mcp.McpResourceWithRawResponse:
        from .resources.mcp import McpResourceWithRawResponse

        return McpResourceWithRawResponse(self._client.mcp)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def migration(self) -> migration.MigrationResourceWithRawResponse:
        from .resources.migration import MigrationResourceWithRawResponse

        return MigrationResourceWithRawResponse(self._client.migration)

    @cached_property
    def cli(self) -> cli.CliResourceWithRawResponse:
        from .resources.cli import CliResourceWithRawResponse

        return CliResourceWithRawResponse(self._client.cli)

    @cached_property
    def tool_router(self) -> tool_router.ToolRouterResourceWithRawResponse:
        from .resources.tool_router import ToolRouterResourceWithRawResponse

        return ToolRouterResourceWithRawResponse(self._client.tool_router)


class AsyncComposioWithRawResponse:
    _client: AsyncComposio

    def __init__(self, client: AsyncComposio) -> None:
        self._client = client

    @cached_property
    def auth_configs(self) -> auth_configs.AsyncAuthConfigsResourceWithRawResponse:
        from .resources.auth_configs import AsyncAuthConfigsResourceWithRawResponse

        return AsyncAuthConfigsResourceWithRawResponse(self._client.auth_configs)

    @cached_property
    def connected_accounts(self) -> connected_accounts.AsyncConnectedAccountsResourceWithRawResponse:
        from .resources.connected_accounts import AsyncConnectedAccountsResourceWithRawResponse

        return AsyncConnectedAccountsResourceWithRawResponse(self._client.connected_accounts)

    @cached_property
    def link(self) -> link.AsyncLinkResourceWithRawResponse:
        from .resources.link import AsyncLinkResourceWithRawResponse

        return AsyncLinkResourceWithRawResponse(self._client.link)

    @cached_property
    def toolkits(self) -> toolkits.AsyncToolkitsResourceWithRawResponse:
        from .resources.toolkits import AsyncToolkitsResourceWithRawResponse

        return AsyncToolkitsResourceWithRawResponse(self._client.toolkits)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithRawResponse:
        from .resources.tools import AsyncToolsResourceWithRawResponse

        return AsyncToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def trigger_instances(self) -> trigger_instances.AsyncTriggerInstancesResourceWithRawResponse:
        from .resources.trigger_instances import AsyncTriggerInstancesResourceWithRawResponse

        return AsyncTriggerInstancesResourceWithRawResponse(self._client.trigger_instances)

    @cached_property
    def triggers_types(self) -> triggers_types.AsyncTriggersTypesResourceWithRawResponse:
        from .resources.triggers_types import AsyncTriggersTypesResourceWithRawResponse

        return AsyncTriggersTypesResourceWithRawResponse(self._client.triggers_types)

    @cached_property
    def mcp(self) -> mcp.AsyncMcpResourceWithRawResponse:
        from .resources.mcp import AsyncMcpResourceWithRawResponse

        return AsyncMcpResourceWithRawResponse(self._client.mcp)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def migration(self) -> migration.AsyncMigrationResourceWithRawResponse:
        from .resources.migration import AsyncMigrationResourceWithRawResponse

        return AsyncMigrationResourceWithRawResponse(self._client.migration)

    @cached_property
    def cli(self) -> cli.AsyncCliResourceWithRawResponse:
        from .resources.cli import AsyncCliResourceWithRawResponse

        return AsyncCliResourceWithRawResponse(self._client.cli)

    @cached_property
    def tool_router(self) -> tool_router.AsyncToolRouterResourceWithRawResponse:
        from .resources.tool_router import AsyncToolRouterResourceWithRawResponse

        return AsyncToolRouterResourceWithRawResponse(self._client.tool_router)


class ComposioWithStreamedResponse:
    _client: Composio

    def __init__(self, client: Composio) -> None:
        self._client = client

    @cached_property
    def auth_configs(self) -> auth_configs.AuthConfigsResourceWithStreamingResponse:
        from .resources.auth_configs import AuthConfigsResourceWithStreamingResponse

        return AuthConfigsResourceWithStreamingResponse(self._client.auth_configs)

    @cached_property
    def connected_accounts(self) -> connected_accounts.ConnectedAccountsResourceWithStreamingResponse:
        from .resources.connected_accounts import ConnectedAccountsResourceWithStreamingResponse

        return ConnectedAccountsResourceWithStreamingResponse(self._client.connected_accounts)

    @cached_property
    def link(self) -> link.LinkResourceWithStreamingResponse:
        from .resources.link import LinkResourceWithStreamingResponse

        return LinkResourceWithStreamingResponse(self._client.link)

    @cached_property
    def toolkits(self) -> toolkits.ToolkitsResourceWithStreamingResponse:
        from .resources.toolkits import ToolkitsResourceWithStreamingResponse

        return ToolkitsResourceWithStreamingResponse(self._client.toolkits)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithStreamingResponse:
        from .resources.tools import ToolsResourceWithStreamingResponse

        return ToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def trigger_instances(self) -> trigger_instances.TriggerInstancesResourceWithStreamingResponse:
        from .resources.trigger_instances import TriggerInstancesResourceWithStreamingResponse

        return TriggerInstancesResourceWithStreamingResponse(self._client.trigger_instances)

    @cached_property
    def triggers_types(self) -> triggers_types.TriggersTypesResourceWithStreamingResponse:
        from .resources.triggers_types import TriggersTypesResourceWithStreamingResponse

        return TriggersTypesResourceWithStreamingResponse(self._client.triggers_types)

    @cached_property
    def mcp(self) -> mcp.McpResourceWithStreamingResponse:
        from .resources.mcp import McpResourceWithStreamingResponse

        return McpResourceWithStreamingResponse(self._client.mcp)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def migration(self) -> migration.MigrationResourceWithStreamingResponse:
        from .resources.migration import MigrationResourceWithStreamingResponse

        return MigrationResourceWithStreamingResponse(self._client.migration)

    @cached_property
    def cli(self) -> cli.CliResourceWithStreamingResponse:
        from .resources.cli import CliResourceWithStreamingResponse

        return CliResourceWithStreamingResponse(self._client.cli)

    @cached_property
    def tool_router(self) -> tool_router.ToolRouterResourceWithStreamingResponse:
        from .resources.tool_router import ToolRouterResourceWithStreamingResponse

        return ToolRouterResourceWithStreamingResponse(self._client.tool_router)


class AsyncComposioWithStreamedResponse:
    _client: AsyncComposio

    def __init__(self, client: AsyncComposio) -> None:
        self._client = client

    @cached_property
    def auth_configs(self) -> auth_configs.AsyncAuthConfigsResourceWithStreamingResponse:
        from .resources.auth_configs import AsyncAuthConfigsResourceWithStreamingResponse

        return AsyncAuthConfigsResourceWithStreamingResponse(self._client.auth_configs)

    @cached_property
    def connected_accounts(self) -> connected_accounts.AsyncConnectedAccountsResourceWithStreamingResponse:
        from .resources.connected_accounts import AsyncConnectedAccountsResourceWithStreamingResponse

        return AsyncConnectedAccountsResourceWithStreamingResponse(self._client.connected_accounts)

    @cached_property
    def link(self) -> link.AsyncLinkResourceWithStreamingResponse:
        from .resources.link import AsyncLinkResourceWithStreamingResponse

        return AsyncLinkResourceWithStreamingResponse(self._client.link)

    @cached_property
    def toolkits(self) -> toolkits.AsyncToolkitsResourceWithStreamingResponse:
        from .resources.toolkits import AsyncToolkitsResourceWithStreamingResponse

        return AsyncToolkitsResourceWithStreamingResponse(self._client.toolkits)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithStreamingResponse:
        from .resources.tools import AsyncToolsResourceWithStreamingResponse

        return AsyncToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def trigger_instances(self) -> trigger_instances.AsyncTriggerInstancesResourceWithStreamingResponse:
        from .resources.trigger_instances import AsyncTriggerInstancesResourceWithStreamingResponse

        return AsyncTriggerInstancesResourceWithStreamingResponse(self._client.trigger_instances)

    @cached_property
    def triggers_types(self) -> triggers_types.AsyncTriggersTypesResourceWithStreamingResponse:
        from .resources.triggers_types import AsyncTriggersTypesResourceWithStreamingResponse

        return AsyncTriggersTypesResourceWithStreamingResponse(self._client.triggers_types)

    @cached_property
    def mcp(self) -> mcp.AsyncMcpResourceWithStreamingResponse:
        from .resources.mcp import AsyncMcpResourceWithStreamingResponse

        return AsyncMcpResourceWithStreamingResponse(self._client.mcp)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def migration(self) -> migration.AsyncMigrationResourceWithStreamingResponse:
        from .resources.migration import AsyncMigrationResourceWithStreamingResponse

        return AsyncMigrationResourceWithStreamingResponse(self._client.migration)

    @cached_property
    def cli(self) -> cli.AsyncCliResourceWithStreamingResponse:
        from .resources.cli import AsyncCliResourceWithStreamingResponse

        return AsyncCliResourceWithStreamingResponse(self._client.cli)

    @cached_property
    def tool_router(self) -> tool_router.AsyncToolRouterResourceWithStreamingResponse:
        from .resources.tool_router import AsyncToolRouterResourceWithStreamingResponse

        return AsyncToolRouterResourceWithStreamingResponse(self._client.tool_router)


Client = Composio

AsyncClient = AsyncComposio
