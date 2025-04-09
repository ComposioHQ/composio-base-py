// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import { APIPromise } from '../../core/api-promise';
import { RequestOptions } from '../../internal/request-options';
import { path } from '../../internal/utils/path';

export class Specs extends APIResource {
  create(body: SpecCreateParams, options?: RequestOptions): APIPromise<SpecCreateResponse> {
    return this._client.post('/api/v3/openapi/specs/create', { body, ...options });
  }

  list(options?: RequestOptions): APIPromise<SpecListResponse> {
    return this._client.get('/api/v3/openapi/specs/list', options);
  }

  delete(id: string, options?: RequestOptions): APIPromise<SpecDeleteResponse> {
    return this._client.delete(path`/api/v3/openapi/specs/${id}`, options);
  }

  retrieveStatus(id: string, options?: RequestOptions): APIPromise<SpecRetrieveStatusResponse> {
    return this._client.get(path`/api/v3/openapi/specs/status/${id}`, options);
  }
}

export interface SpecCreateResponse {
  id: string;

  name: string;

  status: string;
}

export type SpecListResponse = Array<SpecListResponse.SpecListResponseItem>;

export namespace SpecListResponse {
  export interface SpecListResponseItem {
    id: string;

    created_at: string;

    last_sync_at: string;

    logs: Array<SpecListResponseItem.Log>;

    name: string;

    progress: SpecListResponseItem.Progress;

    state: string;

    status: string;

    updated_at: string;
  }

  export namespace SpecListResponseItem {
    export interface Log {
      level: string;

      message: string;

      timestamp: string;
    }

    export interface Progress {
      message: string;
    }
  }
}

export interface SpecDeleteResponse {
  message: string;

  success: boolean;
}

export interface SpecRetrieveStatusResponse {
  message: string;

  success: boolean;
}

export interface SpecCreateParams {
  authConfig: string;

  name: string;

  openApiSpec: string;
}

export declare namespace Specs {
  export {
    type SpecCreateResponse as SpecCreateResponse,
    type SpecListResponse as SpecListResponse,
    type SpecDeleteResponse as SpecDeleteResponse,
    type SpecRetrieveStatusResponse as SpecRetrieveStatusResponse,
    type SpecCreateParams as SpecCreateParams,
  };
}
