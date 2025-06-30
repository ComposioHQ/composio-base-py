# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

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
        cursor: str | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        tool_slug: str | NotGiven = NOT_GIVEN,
        toolkit_slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListResponse:
        """Retrieves a list of files associated with the authenticated project.

        Results can
        be filtered by toolkit and tool slugs.

        Args:
          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          limit: Number of items per page

          tool_slug: Filter files by action slug. Example: "convert-to-pdf"

          toolkit_slug: Filter files by app slug. Example: "file-converter"

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
                        "cursor": cursor,
                        "limit": limit,
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
        """Generates a presigned URL for uploading a file to S3.

        This endpoint handles
        deduplication by checking if a file with the same MD5 hash already exists.

        Args:
          filename: Name of the original file. Example: "photo.jpg"

          md5:
              MD5 hash of the file for deduplication and integrity verification. Example:
              "d41d8cd98f00b204e9800998ecf8427e"

          mimetype: Mime type of the original file. Example: "image/jpeg"

          tool_slug: Slug of the action where this file belongs to. Example: "resize-image"

          toolkit_slug: Slug of the app where this file belongs to. Example: "image-processing"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            FileCreatePresignedURLResponse,
            self._post(
                "/api/v3/files/upload/request",
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
        cursor: str | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        tool_slug: str | NotGiven = NOT_GIVEN,
        toolkit_slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListResponse:
        """Retrieves a list of files associated with the authenticated project.

        Results can
        be filtered by toolkit and tool slugs.

        Args:
          cursor: Cursor for pagination. The cursor is a base64 encoded string of the page and
              limit. The page is the page number and the limit is the number of items per
              page. The cursor is used to paginate through the items. The cursor is not
              required for the first page.

          limit: Number of items per page

          tool_slug: Filter files by action slug. Example: "convert-to-pdf"

          toolkit_slug: Filter files by app slug. Example: "file-converter"

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
                        "cursor": cursor,
                        "limit": limit,
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
        """Generates a presigned URL for uploading a file to S3.

        This endpoint handles
        deduplication by checking if a file with the same MD5 hash already exists.

        Args:
          filename: Name of the original file. Example: "photo.jpg"

          md5:
              MD5 hash of the file for deduplication and integrity verification. Example:
              "d41d8cd98f00b204e9800998ecf8427e"

          mimetype: Mime type of the original file. Example: "image/jpeg"

          tool_slug: Slug of the action where this file belongs to. Example: "resize-image"

          toolkit_slug: Slug of the app where this file belongs to. Example: "image-processing"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            FileCreatePresignedURLResponse,
            await self._post(
                "/api/v3/files/upload/request",
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
