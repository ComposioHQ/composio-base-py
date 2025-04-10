// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import { APIPromise } from '../../core/api-promise';
import { RequestOptions } from '../../internal/request-options';

export class APIKey extends APIResource {
  retrieve(options?: RequestOptions): APIPromise<APIKeyRetrieveResponse> {
    return this._client.get('/api/v3/org/api_key', options);
  }

  regenerate(options?: RequestOptions): APIPromise<APIKeyRegenerateResponse> {
    return this._client.post('/api/v3/org/api_key/regenerate', options);
  }
}

export interface APIKeyRetrieveResponse {
  org_api_key: string;
}

export interface APIKeyRegenerateResponse {
  org_api_key: string;
}

export declare namespace APIKey {
  export {
    type APIKeyRetrieveResponse as APIKeyRetrieveResponse,
    type APIKeyRegenerateResponse as APIKeyRegenerateResponse,
  };
}
