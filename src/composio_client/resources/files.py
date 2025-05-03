# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..types import file_list_params, file_create_presigned_url_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.file_list_response import FileListResponse
from ..types.file_create_presigned_url_response import FileCreatePresignedURLResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        tool_slug: str | NotGiven = NOT_GIVEN,
        toolkit_slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListResponse:
        """
        List files with optional app and action filters

        Args:
          tool_slug: Name of the action where this file belongs to.

          toolkit_slug: Slug of the app where this file belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v3/files/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tool_slug": tool_slug,
                        "toolkit_slug": toolkit_slug,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    def create_presigned_url(
        self,
        file_type: Literal["request", "response"],
        *,
        filename: str,
        md5: str,
        mimetype: str,
        tool_slug: str,
        toolkit_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileCreatePresignedURLResponse:
        """
        Create presigned URL for file upload to S3

        Args:
          filename: Name of the original file.

          md5: MD5 of a file.

          mimetype: Mime type of the original file.

          tool_slug: Slug of the action where this file belongs to.

          toolkit_slug: Slug of the app where this file belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_type:
            raise ValueError(f"Expected a non-empty value for `file_type` but received {file_type!r}")
        return cast(
            FileCreatePresignedURLResponse,
            self._post(
                f"/api/v3/files/upload/{file_type}",
                body=maybe_transform(
                    {
                        "filename": filename,
                        "md5": md5,
                        "mimetype": mimetype,
                        "tool_slug": tool_slug,
                        "toolkit_slug": toolkit_slug,
                    },
                    file_create_presigned_url_params.FileCreatePresignedURLParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, FileCreatePresignedURLResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ComposioHQ/composio-base-py#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        tool_slug: str | NotGiven = NOT_GIVEN,
        toolkit_slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListResponse:
        """
        List files with optional app and action filters

        Args:
          tool_slug: Name of the action where this file belongs to.

          toolkit_slug: Slug of the app where this file belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v3/files/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tool_slug": tool_slug,
                        "toolkit_slug": toolkit_slug,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    async def create_presigned_url(
        self,
        file_type: Literal["request", "response"],
        *,
        filename: str,
        md5: str,
        mimetype: str,
        tool_slug: str,
        toolkit_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileCreatePresignedURLResponse:
        """
        Create presigned URL for file upload to S3

        Args:
          filename: Name of the original file.

          md5: MD5 of a file.

          mimetype: Mime type of the original file.

          tool_slug: Slug of the action where this file belongs to.

          toolkit_slug: Slug of the app where this file belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_type:
            raise ValueError(f"Expected a non-empty value for `file_type` but received {file_type!r}")
        return cast(
            FileCreatePresignedURLResponse,
            await self._post(
                f"/api/v3/files/upload/{file_type}",
                body=await async_maybe_transform(
                    {
                        "filename": filename,
                        "md5": md5,
                        "mimetype": mimetype,
                        "tool_slug": tool_slug,
                        "toolkit_slug": toolkit_slug,
                    },
                    file_create_presigned_url_params.FileCreatePresignedURLParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, FileCreatePresignedURLResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.create_presigned_url = to_raw_response_wrapper(
            files.create_presigned_url,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.create_presigned_url = async_to_raw_response_wrapper(
            files.create_presigned_url,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.create_presigned_url = to_streamed_response_wrapper(
            files.create_presigned_url,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.create_presigned_url = async_to_streamed_response_wrapper(
            files.create_presigned_url,
        )
