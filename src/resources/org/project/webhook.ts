// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../core/resource';
import { APIPromise } from '../../../core/api-promise';
import { RequestOptions } from '../../../internal/request-options';

export class Webhook extends APIResource {
  /**
   * Get the webhook URL for a project
   */
  retrieve(query: WebhookRetrieveParams, options?: RequestOptions): APIPromise<WebhookRetrieveResponse> {
    return this._client.get('/api/v3/org/project/webhook', { query, ...options });
  }

  update(body: WebhookUpdateParams, options?: RequestOptions): APIPromise<WebhookUpdateResponse> {
    return this._client.post('/api/v3/org/project/webhook/update', { body, ...options });
  }

  delete(body: WebhookDeleteParams, options?: RequestOptions): APIPromise<WebhookDeleteResponse> {
    return this._client.delete('/api/v3/org/project/webhook', { body, ...options });
  }

  refresh(options?: RequestOptions): APIPromise<WebhookRefreshResponse> {
    return this._client.post('/api/v3/org/project/webhook/refresh', options);
  }
}

export interface WebhookRetrieveResponse {
  /**
   * Status of the webhook
   */
  status: 'success' | 'not found';

  url: WebhookRetrieveResponse.UnionMember0 | WebhookRetrieveResponse.UnionMember1;

  /**
   * Webhook secret
   */
  webhook_secret: string;
}

export namespace WebhookRetrieveResponse {
  export interface UnionMember0 {
    type: 'trigger';

    /**
     * Webhook URL
     */
    webhook_url?: string;
  }

  export interface UnionMember1 {
    type: 'event';

    /**
     * Event webhook URL
     */
    event_webhook_url?: string;
  }
}

export interface WebhookUpdateResponse {
  /**
   * Status message
   */
  message: string;

  /**
   * Whether the operation was successful
   */
  success: boolean;
}

export interface WebhookDeleteResponse {
  status: 'success';
}

export interface WebhookRefreshResponse {
  /**
   * Status message
   */
  message: string;

  /**
   * Whether the operation was successful
   */
  success: boolean;

  /**
   * Webhook secret
   */
  webhook_secret: string;
}

export interface WebhookRetrieveParams {
  /**
   * Type of the webhook
   */
  type: 'trigger' | 'event';
}

export interface WebhookUpdateParams {
  /**
   * Type of the webhook
   */
  type: 'trigger' | 'event';

  /**
   * Webhook URL
   */
  webhook_url: string;
}

export interface WebhookDeleteParams {
  /**
   * Type of the webhook
   */
  type: 'trigger' | 'event';
}

export declare namespace Webhook {
  export {
    type WebhookRetrieveResponse as WebhookRetrieveResponse,
    type WebhookUpdateResponse as WebhookUpdateResponse,
    type WebhookDeleteResponse as WebhookDeleteResponse,
    type WebhookRefreshResponse as WebhookRefreshResponse,
    type WebhookRetrieveParams as WebhookRetrieveParams,
    type WebhookUpdateParams as WebhookUpdateParams,
    type WebhookDeleteParams as WebhookDeleteParams,
  };
}
