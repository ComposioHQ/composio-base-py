// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import { APIPromise } from '../../core/api-promise';
import { RequestOptions } from '../../internal/request-options';

export class Admin extends APIResource {
  identify(body: AdminIdentifyParams, options?: RequestOptions): APIPromise<AdminIdentifyResponse> {
    return this._client.post('/api/v3/admin/identify', { body, ...options });
  }
}

export interface AdminIdentifyResponse {
  apiKey: string;

  clientId: string;

  email: string;

  orgId: string;
}

export interface AdminIdentifyParams {
  hash: string;

  adminToken?: string;
}

export declare namespace Admin {
  export {
    type AdminIdentifyResponse as AdminIdentifyResponse,
    type AdminIdentifyParams as AdminIdentifyParams,
  };
}
