# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .trigger import (
    TriggerResource,
    AsyncTriggerResource,
    TriggerResourceWithRawResponse,
    AsyncTriggerResourceWithRawResponse,
    TriggerResourceWithStreamingResponse,
    AsyncTriggerResourceWithStreamingResponse,
)
from .webhook import (
    WebhookResource,
    AsyncWebhookResource,
    WebhookResourceWithRawResponse,
    AsyncWebhookResourceWithRawResponse,
    WebhookResourceWithStreamingResponse,
    AsyncWebhookResourceWithStreamingResponse,
)
from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.org import project_create_params
from ...._base_client import make_request_options
from ....types.org.project_list_response import ProjectListResponse
from ....types.org.project_create_response import ProjectCreateResponse
from ....types.org.project_delete_response import ProjectDeleteResponse
from ....types.org.project_retrieve_response import ProjectRetrieveResponse

__all__ = ["ProjectResource", "AsyncProjectResource"]


class ProjectResource(SyncAPIResource):
    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def webhook(self) -> WebhookResource:
        return WebhookResource(self._client)

    @cached_property
    def trigger(self) -> TriggerResource:
        return TriggerResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return ProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return ProjectResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectCreateResponse:
        """
        Creates a new project within the authenticated user's organization using the
        specified name. Projects are isolated environments within your organization,
        each with their own API keys, webhook configurations, and resources. Use this
        endpoint to create additional projects for different environments (e.g.,
        development, staging, production) or for separate applications.

        Args:
          name: A unique name for your project that follows the required format rules

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v3/org/project/new",
            body=maybe_transform({"name": name}, project_create_params.ProjectCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
        )

    def retrieve(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectRetrieveResponse:
        """
        Retrieves detailed information about a specific project using its unique
        identifier. This endpoint provides complete project configuration including
        webhook URLs, creation and update timestamps, and webhook secrets. Use this
        endpoint to inspect project settings or verify project configuration.

        Args:
          project_id: Unique identifier (Nano ID) of the project to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/api/v3/org/project/{project_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectListResponse:
        """
        Retrieves all projects belonging to the authenticated user's organization.
        Projects are returned in descending order of creation date (newest first). This
        endpoint is useful for displaying project selection in dashboards or for
        integrations that need to list all available projects.
        """
        return self._get(
            "/api/v3/org/project/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectListResponse,
        )

    def delete(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectDeleteResponse:
        """Soft-deletes a project within the organization by its unique identifier.

        When a
        project is deleted, it is marked as deleted but not immediately removed from the
        database. This operation affects all resources associated with the project
        including API keys, webhook configurations, and connected services. This action
        cannot be undone through the API.

        Args:
          project_id: Unique identifier (Nano ID) of the project to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._delete(
            f"/api/v3/org/project/delete/{project_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDeleteResponse,
        )


class AsyncProjectResource(AsyncAPIResource):
    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def webhook(self) -> AsyncWebhookResource:
        return AsyncWebhookResource(self._client)

    @cached_property
    def trigger(self) -> AsyncTriggerResource:
        return AsyncTriggerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncProjectResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectCreateResponse:
        """
        Creates a new project within the authenticated user's organization using the
        specified name. Projects are isolated environments within your organization,
        each with their own API keys, webhook configurations, and resources. Use this
        endpoint to create additional projects for different environments (e.g.,
        development, staging, production) or for separate applications.

        Args:
          name: A unique name for your project that follows the required format rules

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v3/org/project/new",
            body=await async_maybe_transform({"name": name}, project_create_params.ProjectCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
        )

    async def retrieve(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectRetrieveResponse:
        """
        Retrieves detailed information about a specific project using its unique
        identifier. This endpoint provides complete project configuration including
        webhook URLs, creation and update timestamps, and webhook secrets. Use this
        endpoint to inspect project settings or verify project configuration.

        Args:
          project_id: Unique identifier (Nano ID) of the project to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/api/v3/org/project/{project_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectListResponse:
        """
        Retrieves all projects belonging to the authenticated user's organization.
        Projects are returned in descending order of creation date (newest first). This
        endpoint is useful for displaying project selection in dashboards or for
        integrations that need to list all available projects.
        """
        return await self._get(
            "/api/v3/org/project/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectListResponse,
        )

    async def delete(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectDeleteResponse:
        """Soft-deletes a project within the organization by its unique identifier.

        When a
        project is deleted, it is marked as deleted but not immediately removed from the
        database. This operation affects all resources associated with the project
        including API keys, webhook configurations, and connected services. This action
        cannot be undone through the API.

        Args:
          project_id: Unique identifier (Nano ID) of the project to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._delete(
            f"/api/v3/org/project/delete/{project_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDeleteResponse,
        )


class ProjectResourceWithRawResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.create = to_raw_response_wrapper(
            project.create,
        )
        self.retrieve = to_raw_response_wrapper(
            project.retrieve,
        )
        self.list = to_raw_response_wrapper(
            project.list,
        )
        self.delete = to_raw_response_wrapper(
            project.delete,
        )

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._project.api_keys)

    @cached_property
    def webhook(self) -> WebhookResourceWithRawResponse:
        return WebhookResourceWithRawResponse(self._project.webhook)

    @cached_property
    def trigger(self) -> TriggerResourceWithRawResponse:
        return TriggerResourceWithRawResponse(self._project.trigger)


class AsyncProjectResourceWithRawResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.create = async_to_raw_response_wrapper(
            project.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            project.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            project.list,
        )
        self.delete = async_to_raw_response_wrapper(
            project.delete,
        )

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._project.api_keys)

    @cached_property
    def webhook(self) -> AsyncWebhookResourceWithRawResponse:
        return AsyncWebhookResourceWithRawResponse(self._project.webhook)

    @cached_property
    def trigger(self) -> AsyncTriggerResourceWithRawResponse:
        return AsyncTriggerResourceWithRawResponse(self._project.trigger)


class ProjectResourceWithStreamingResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.create = to_streamed_response_wrapper(
            project.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            project.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            project.list,
        )
        self.delete = to_streamed_response_wrapper(
            project.delete,
        )

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._project.api_keys)

    @cached_property
    def webhook(self) -> WebhookResourceWithStreamingResponse:
        return WebhookResourceWithStreamingResponse(self._project.webhook)

    @cached_property
    def trigger(self) -> TriggerResourceWithStreamingResponse:
        return TriggerResourceWithStreamingResponse(self._project.trigger)


class AsyncProjectResourceWithStreamingResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.create = async_to_streamed_response_wrapper(
            project.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            project.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            project.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            project.delete,
        )

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._project.api_keys)

    @cached_property
    def webhook(self) -> AsyncWebhookResourceWithStreamingResponse:
        return AsyncWebhookResourceWithStreamingResponse(self._project.webhook)

    @cached_property
    def trigger(self) -> AsyncTriggerResourceWithStreamingResponse:
        return AsyncTriggerResourceWithStreamingResponse(self._project.trigger)
