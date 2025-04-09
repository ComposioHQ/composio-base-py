// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../core/resource';
import * as HandleAPI from './handle';
import {
  Handle,
  HandleExecuteParams,
  HandleExecuteResponse,
  HandleRetrieveParams,
  HandleRetrieveResponse,
} from './handle';
import { APIPromise } from '../../../core/api-promise';
import { RequestOptions } from '../../../internal/request-options';
import { path } from '../../../internal/utils/path';

export class TriggerInstances extends APIResource {
  handle: HandleAPI.Handle = new HandleAPI.Handle(this._client);

  listActive(
    query: TriggerInstanceListActiveParams | null | undefined = {},
    options?: RequestOptions,
  ): APIPromise<TriggerInstanceListActiveResponse> {
    return this._client.get('/api/v3/trigger_instances/active', { query, ...options });
  }

  removeUpsert(slug: string, options?: RequestOptions): APIPromise<TriggerInstanceRemoveUpsertResponse> {
    return this._client.delete(path`/api/v3/trigger_instances/${slug}/upsert`, options);
  }

  updateStatus(
    status: 'enable' | 'disable',
    params: TriggerInstanceUpdateStatusParams,
    options?: RequestOptions,
  ): APIPromise<TriggerInstanceUpdateStatusResponse> {
    const { slug } = params;
    return this._client.patch(path`/api/v3/trigger_instances/${slug}/status/${status}`, options);
  }

  upsert(
    slug: string,
    body: TriggerInstanceUpsertParams,
    options?: RequestOptions,
  ): APIPromise<TriggerInstanceUpsertResponse> {
    return this._client.post(path`/api/v3/trigger_instances/${slug}/upsert`, { body, ...options });
  }
}

export interface TriggerInstanceListActiveResponse {
  items: Array<TriggerInstanceListActiveResponse.Item>;

  next_cursor: string | null;

  total_pages: number;
}

export namespace TriggerInstanceListActiveResponse {
  export interface Item {
    /**
     * Nano ID of the trigger instance
     */
    id: string;

    /**
     * ID of the connected account this trigger is associated with
     */
    connectedAccountId: string;

    /**
     * ISO 8601 timestamp when the trigger instance was disabled, if applicable
     */
    disabledAt: string | null;

    /**
     * State of the trigger instance
     */
    state: Record<string, unknown>;

    /**
     * Configuration for the trigger
     */
    triggerConfig: Record<string, unknown>;

    /**
     * Name of the trigger
     */
    triggerName: string;

    /**
     * ISO 8601 timestamp when the trigger instance was updated
     */
    updatedAt: string;

    /**
     * Additional data associated with the trigger instance
     */
    triggerData?: string;

    /**
     * Unique identifier of the trigger instance
     */
    uuid?: string;
  }
}

export interface TriggerInstanceRemoveUpsertResponse {
  /**
   * ID of the updated trigger
   */
  triggerId: string;
}

export interface TriggerInstanceUpdateStatusResponse {
  /**
   * Status of the operation
   */
  status: 'success';
}

export interface TriggerInstanceUpsertResponse {
  /**
   * ID of the updated trigger
   */
  triggerId: string;
}

export interface TriggerInstanceListActiveParams {
  /**
   * Comma-separated list of auth config IDs to filter triggers by
   */
  authConfigIds?: string;

  /**
   * Comma-separated list of connected account IDs to filter triggers by
   */
  connectedAccountIds?: string;

  /**
   * Number of items to return per page.
   */
  limit?: number;

  /**
   * Page number for pagination. Starts from 1.
   */
  page?: number;

  /**
   * When set to true, includes disabled triggers in the response.
   */
  showDisabled?: boolean | null;

  /**
   * Comma-separated list of trigger IDs to filter triggers by
   */
  triggerIds?: string;

  /**
   * Comma-separated list of trigger names to filter triggers by
   */
  triggerNames?: string;
}

export interface TriggerInstanceUpdateStatusParams {
  /**
   * The slug of the trigger instance
   */
  slug: string;
}

export interface TriggerInstanceUpsertParams {
  /**
   * Connection ID
   */
  connectedAuthId: string;

  /**
   * Trigger configuration
   */
  triggerConfig: Record<string, unknown>;
}

TriggerInstances.Handle = Handle;

export declare namespace TriggerInstances {
  export {
    type TriggerInstanceListActiveResponse as TriggerInstanceListActiveResponse,
    type TriggerInstanceRemoveUpsertResponse as TriggerInstanceRemoveUpsertResponse,
    type TriggerInstanceUpdateStatusResponse as TriggerInstanceUpdateStatusResponse,
    type TriggerInstanceUpsertResponse as TriggerInstanceUpsertResponse,
    type TriggerInstanceListActiveParams as TriggerInstanceListActiveParams,
    type TriggerInstanceUpdateStatusParams as TriggerInstanceUpdateStatusParams,
    type TriggerInstanceUpsertParams as TriggerInstanceUpsertParams,
  };

  export {
    Handle as Handle,
    type HandleRetrieveResponse as HandleRetrieveResponse,
    type HandleExecuteResponse as HandleExecuteResponse,
    type HandleRetrieveParams as HandleRetrieveParams,
    type HandleExecuteParams as HandleExecuteParams,
  };
}
