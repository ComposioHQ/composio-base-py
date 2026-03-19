# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.tool_router.session import (
    file_list_params,
    file_delete_params,
    file_create_upload_url_params,
    file_create_download_url_params,
)
from ....types.tool_router.session.file_list_response import FileListResponse
from ....types.tool_router.session.file_delete_response import FileDeleteResponse
from ....types.tool_router.session.file_create_upload_url_response import FileCreateUploadURLResponse
from ....types.tool_router.session.file_create_download_url_response import FileCreateDownloadURLResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    """(Labs) Tool router endpoints"""

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
        mount_id: str,
        *,
        session_id: str,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        mount_relative_prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        Lists files in a workbench session storage mount with cursor-based pagination.
        Use the download_url endpoint with the returned mount_relative_path to get a
        presigned download URL.

        Args:
          session_id: The unique identifier of the tool router session

          mount_id: ID of the storage mount

          cursor: Pagination cursor from the previous response next_cursor field

          limit: Maximum number of files to return per page (1-500)

          mount_relative_prefix: Relative path prefix within the mount for filtering

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not mount_id:
            raise ValueError(f"Expected a non-empty value for `mount_id` but received {mount_id!r}")
        return self._get(
            path_template(
                "/api/v3/tool_router/session/{session_id}/mounts/{mount_id}/items",
                session_id=session_id,
                mount_id=mount_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "mount_relative_prefix": mount_relative_prefix,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    def delete(
        self,
        mount_id: str,
        *,
        session_id: str,
        mount_relative_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileDeleteResponse:
        """Deletes a file from a workbench session storage mount.

        S3 delete is idempotent —
        deleting a non-existent file succeeds silently.

        Args:
          session_id: The unique identifier of the tool router session

          mount_id: ID of the storage mount

          mount_relative_path: Relative file path within the mount

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not mount_id:
            raise ValueError(f"Expected a non-empty value for `mount_id` but received {mount_id!r}")
        return self._post(
            path_template(
                "/api/v3/tool_router/session/{session_id}/mounts/{mount_id}/delete",
                session_id=session_id,
                mount_id=mount_id,
            ),
            body=maybe_transform({"mount_relative_path": mount_relative_path}, file_delete_params.FileDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileDeleteResponse,
        )

    def create_download_url(
        self,
        mount_id: str,
        *,
        session_id: str,
        mount_relative_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCreateDownloadURLResponse:
        """
        Generates a presigned download URL for a file in a workbench session mount.
        Accepts a relative path within the mount.

        Args:
          session_id: The unique identifier of the tool router session

          mount_id: ID of the storage mount

          mount_relative_path: Relative file path within the mount

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not mount_id:
            raise ValueError(f"Expected a non-empty value for `mount_id` but received {mount_id!r}")
        return self._post(
            path_template(
                "/api/v3/tool_router/session/{session_id}/mounts/{mount_id}/download_url",
                session_id=session_id,
                mount_id=mount_id,
            ),
            body=maybe_transform(
                {"mount_relative_path": mount_relative_path},
                file_create_download_url_params.FileCreateDownloadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCreateDownloadURLResponse,
        )

    def create_upload_url(
        self,
        mount_id: str,
        *,
        session_id: str,
        mount_relative_path: str,
        mimetype: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCreateUploadURLResponse:
        """
        Generates a presigned upload URL for uploading a file to a workbench session
        mount. The caller should PUT the file content directly to the returned URL.

        Args:
          session_id: The unique identifier of the tool router session

          mount_id: ID of the storage mount

          mount_relative_path: Supports subdirectories (e.g. "data/output.csv", "images/charts/chart.png")

          mimetype: MIME type of the file being uploaded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not mount_id:
            raise ValueError(f"Expected a non-empty value for `mount_id` but received {mount_id!r}")
        return self._post(
            path_template(
                "/api/v3/tool_router/session/{session_id}/mounts/{mount_id}/upload_url",
                session_id=session_id,
                mount_id=mount_id,
            ),
            body=maybe_transform(
                {
                    "mount_relative_path": mount_relative_path,
                    "mimetype": mimetype,
                },
                file_create_upload_url_params.FileCreateUploadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCreateUploadURLResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    """(Labs) Tool router endpoints"""

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
        mount_id: str,
        *,
        session_id: str,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        mount_relative_prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        Lists files in a workbench session storage mount with cursor-based pagination.
        Use the download_url endpoint with the returned mount_relative_path to get a
        presigned download URL.

        Args:
          session_id: The unique identifier of the tool router session

          mount_id: ID of the storage mount

          cursor: Pagination cursor from the previous response next_cursor field

          limit: Maximum number of files to return per page (1-500)

          mount_relative_prefix: Relative path prefix within the mount for filtering

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not mount_id:
            raise ValueError(f"Expected a non-empty value for `mount_id` but received {mount_id!r}")
        return await self._get(
            path_template(
                "/api/v3/tool_router/session/{session_id}/mounts/{mount_id}/items",
                session_id=session_id,
                mount_id=mount_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "mount_relative_prefix": mount_relative_prefix,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    async def delete(
        self,
        mount_id: str,
        *,
        session_id: str,
        mount_relative_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileDeleteResponse:
        """Deletes a file from a workbench session storage mount.

        S3 delete is idempotent —
        deleting a non-existent file succeeds silently.

        Args:
          session_id: The unique identifier of the tool router session

          mount_id: ID of the storage mount

          mount_relative_path: Relative file path within the mount

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not mount_id:
            raise ValueError(f"Expected a non-empty value for `mount_id` but received {mount_id!r}")
        return await self._post(
            path_template(
                "/api/v3/tool_router/session/{session_id}/mounts/{mount_id}/delete",
                session_id=session_id,
                mount_id=mount_id,
            ),
            body=await async_maybe_transform(
                {"mount_relative_path": mount_relative_path}, file_delete_params.FileDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileDeleteResponse,
        )

    async def create_download_url(
        self,
        mount_id: str,
        *,
        session_id: str,
        mount_relative_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCreateDownloadURLResponse:
        """
        Generates a presigned download URL for a file in a workbench session mount.
        Accepts a relative path within the mount.

        Args:
          session_id: The unique identifier of the tool router session

          mount_id: ID of the storage mount

          mount_relative_path: Relative file path within the mount

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not mount_id:
            raise ValueError(f"Expected a non-empty value for `mount_id` but received {mount_id!r}")
        return await self._post(
            path_template(
                "/api/v3/tool_router/session/{session_id}/mounts/{mount_id}/download_url",
                session_id=session_id,
                mount_id=mount_id,
            ),
            body=await async_maybe_transform(
                {"mount_relative_path": mount_relative_path},
                file_create_download_url_params.FileCreateDownloadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCreateDownloadURLResponse,
        )

    async def create_upload_url(
        self,
        mount_id: str,
        *,
        session_id: str,
        mount_relative_path: str,
        mimetype: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCreateUploadURLResponse:
        """
        Generates a presigned upload URL for uploading a file to a workbench session
        mount. The caller should PUT the file content directly to the returned URL.

        Args:
          session_id: The unique identifier of the tool router session

          mount_id: ID of the storage mount

          mount_relative_path: Supports subdirectories (e.g. "data/output.csv", "images/charts/chart.png")

          mimetype: MIME type of the file being uploaded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not mount_id:
            raise ValueError(f"Expected a non-empty value for `mount_id` but received {mount_id!r}")
        return await self._post(
            path_template(
                "/api/v3/tool_router/session/{session_id}/mounts/{mount_id}/upload_url",
                session_id=session_id,
                mount_id=mount_id,
            ),
            body=await async_maybe_transform(
                {
                    "mount_relative_path": mount_relative_path,
                    "mimetype": mimetype,
                },
                file_create_upload_url_params.FileCreateUploadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCreateUploadURLResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.create_download_url = to_raw_response_wrapper(
            files.create_download_url,
        )
        self.create_upload_url = to_raw_response_wrapper(
            files.create_upload_url,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.create_download_url = async_to_raw_response_wrapper(
            files.create_download_url,
        )
        self.create_upload_url = async_to_raw_response_wrapper(
            files.create_upload_url,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.create_download_url = to_streamed_response_wrapper(
            files.create_download_url,
        )
        self.create_upload_url = to_streamed_response_wrapper(
            files.create_upload_url,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.create_download_url = async_to_streamed_response_wrapper(
            files.create_download_url,
        )
        self.create_upload_url = async_to_streamed_response_wrapper(
            files.create_upload_url,
        )
