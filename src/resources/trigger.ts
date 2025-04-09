// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';

export class Trigger extends APIResource {
  log(body: TriggerLogParams, options?: RequestOptions): APIPromise<TriggerLogResponse> {
    return this._client.post('/api/v3/internal/trigger/logs', { body, ...options });
  }
}

export interface TriggerLogResponse {
  nextCursor: string | null;

  data?: Array<TriggerLogResponse.Data>;
}

export namespace TriggerLogResponse {
  export interface Data {
    id: string;

    appName: string;

    clientId: string;

    connectionId: string;

    createdAt: string;

    entityId: string;

    meta: Data.Meta;

    status: string;

    /**
     * Log entity type (trigger or action)
     */
    type: 'trigger' | 'action';
  }

  export namespace Data {
    export interface Meta {
      id: string;

      clientId: string;

      connectionId: string;

      createdAt: string;

      provider: string;

      /**
       * Log entity type (trigger or action)
       */
      type: 'trigger' | 'action';

      updatedAt: string;

      triggerClientError?: string;

      triggerClientPayload?: string;

      triggerClientResponse?: string;

      triggerName?: string;

      triggerProviderPayload?: string;
    }
  }
}

export interface TriggerLogParams {
  /**
   * cursor that can be used to paginate through the logs
   */
  cursor: string | null;

  entityId?: string;

  integrationId?: string;

  /**
   * number of logs to return
   */
  limit?: number;

  /**
   * Search term to filter logs
   */
  search?: string;

  /**
   * Filter logs by their status level
   */
  status?: 'all' | 'success' | 'error';

  /**
   * Return logs from the last N time units
   */
  time?: '5m' | '30m' | '6h' | '1d' | '1w' | '1month' | '1y';
}

export declare namespace Trigger {
  export { type TriggerLogResponse as TriggerLogResponse, type TriggerLogParams as TriggerLogParams };
}
