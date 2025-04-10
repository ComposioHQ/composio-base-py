// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import { APIPromise } from '../../core/api-promise';
import { RequestOptions } from '../../internal/request-options';
import { path } from '../../internal/utils/path';

export class Handle extends APIResource {
  retrieve(projectID: string, params: HandleRetrieveParams, options?: RequestOptions): APIPromise<string> {
    const { slug } = params;
    return this._client.get(path`/api/v3/trigger_instances/${slug}/${projectID}/handle`, options);
  }

  execute(projectID: string, params: HandleExecuteParams, options?: RequestOptions): APIPromise<string> {
    const { slug } = params;
    return this._client.post(path`/api/v3/trigger_instances/${slug}/${projectID}/handle`, options);
  }
}

export type HandleRetrieveResponse = string;

export type HandleExecuteResponse = string;

export interface HandleRetrieveParams {
  /**
   * The slug of the trigger instance
   */
  slug: string;
}

export interface HandleExecuteParams {
  /**
   * The slug of the trigger instance
   */
  slug: string;
}

export declare namespace Handle {
  export {
    type HandleRetrieveResponse as HandleRetrieveResponse,
    type HandleExecuteResponse as HandleExecuteResponse,
    type HandleRetrieveParams as HandleRetrieveParams,
    type HandleExecuteParams as HandleExecuteParams,
  };
}
