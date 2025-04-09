// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../../../core/resource';
import { APIPromise } from '../../../../../core/api-promise';
import { RequestOptions } from '../../../../../internal/request-options';

export class Trigger extends APIResource {
  update(params: TriggerUpdateParams, options?: RequestOptions): APIPromise<TriggerUpdateResponse> {
    const { enabled } = params;
    return this._client.patch('/api/v3/org/project/trigger', { query: { enabled }, ...options });
  }

  list(options?: RequestOptions): APIPromise<TriggerListResponse> {
    return this._client.get('/api/v3/org/project/trigger', options);
  }
}

export interface TriggerUpdateResponse {
  id: string;

  auto_id: number;

  created_at: string;

  deleted: boolean;

  email: string;

  event_webhook_url: string | null;

  name: string;

  nano_id: string | null;

  org_id: string;

  updated_at: string;

  webhook_secret: string | null;

  webhook_url: string | null;

  is_new_webhook?: boolean;

  last_subscribed_at?: string | null;

  triggers_enabled?: boolean;
}

export interface TriggerListResponse {
  id: string;

  auto_id: number;

  created_at: string;

  deleted: boolean;

  email: string;

  event_webhook_url: string | null;

  name: string;

  nano_id: string | null;

  org_id: string;

  updated_at: string;

  webhook_secret: string | null;

  webhook_url: string | null;

  is_new_webhook?: boolean;

  last_subscribed_at?: string | null;

  triggers_enabled?: boolean;
}

export interface TriggerUpdateParams {
  /**
   * Enabled
   */
  enabled: boolean;
}

export declare namespace Trigger {
  export {
    type TriggerUpdateResponse as TriggerUpdateResponse,
    type TriggerListResponse as TriggerListResponse,
    type TriggerUpdateParams as TriggerUpdateParams,
  };
}
