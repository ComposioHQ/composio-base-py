// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../core/resource';
import * as APIKeysAPI from './api-keys';
import {
  APIKeyCreateAPIKeyResponse,
  APIKeyCreateParams,
  APIKeyCreateResponse,
  APIKeyDeleteParams,
  APIKeyDeleteResponse,
  APIKeyListResponse,
  APIKeys,
} from './api-keys';
import * as TriggerAPI from './trigger';
import { Trigger, TriggerListResponse, TriggerUpdateParams, TriggerUpdateResponse } from './trigger';
import * as WebhookAPI from './webhook';
import {
  Webhook,
  WebhookDeleteParams,
  WebhookDeleteResponse,
  WebhookRefreshResponse,
  WebhookRetrieveParams,
  WebhookRetrieveResponse,
  WebhookUpdateParams,
  WebhookUpdateResponse,
} from './webhook';
import { APIPromise } from '../../../core/api-promise';
import { RequestOptions } from '../../../internal/request-options';
import { path } from '../../../internal/utils/path';

export class Project extends APIResource {
  apiKeys: APIKeysAPI.APIKeys = new APIKeysAPI.APIKeys(this._client);
  webhook: WebhookAPI.Webhook = new WebhookAPI.Webhook(this._client);
  trigger: TriggerAPI.Trigger = new TriggerAPI.Trigger(this._client);

  create(body: ProjectCreateParams, options?: RequestOptions): APIPromise<ProjectCreateResponse> {
    return this._client.post('/api/v3/org/project/new', { body, ...options });
  }

  retrieve(projectID: string, options?: RequestOptions): APIPromise<ProjectRetrieveResponse> {
    return this._client.get(path`/api/v3/org/project/${projectID}`, options);
  }

  list(options?: RequestOptions): APIPromise<ProjectListResponse> {
    return this._client.get('/api/v3/org/project/list', options);
  }

  delete(projectID: string, options?: RequestOptions): APIPromise<ProjectDeleteResponse> {
    return this._client.delete(path`/api/v3/org/project/delete/${projectID}`, options);
  }
}

export interface ProjectCreateResponse {
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

export interface ProjectRetrieveResponse {
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

export interface ProjectListResponse {
  data: Array<ProjectListResponse.Data>;
}

export namespace ProjectListResponse {
  export interface Data {
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
}

export interface ProjectDeleteResponse {
  status: string;
}

export interface ProjectCreateParams {
  /**
   * Name of the project
   */
  name: string;
}

Project.APIKeys = APIKeys;
Project.Webhook = Webhook;
Project.Trigger = Trigger;

export declare namespace Project {
  export {
    type ProjectCreateResponse as ProjectCreateResponse,
    type ProjectRetrieveResponse as ProjectRetrieveResponse,
    type ProjectListResponse as ProjectListResponse,
    type ProjectDeleteResponse as ProjectDeleteResponse,
    type ProjectCreateParams as ProjectCreateParams,
  };

  export {
    APIKeys as APIKeys,
    type APIKeyCreateResponse as APIKeyCreateResponse,
    type APIKeyListResponse as APIKeyListResponse,
    type APIKeyDeleteResponse as APIKeyDeleteResponse,
    type APIKeyCreateAPIKeyResponse as APIKeyCreateAPIKeyResponse,
    type APIKeyCreateParams as APIKeyCreateParams,
    type APIKeyDeleteParams as APIKeyDeleteParams,
  };

  export {
    Webhook as Webhook,
    type WebhookRetrieveResponse as WebhookRetrieveResponse,
    type WebhookUpdateResponse as WebhookUpdateResponse,
    type WebhookDeleteResponse as WebhookDeleteResponse,
    type WebhookRefreshResponse as WebhookRefreshResponse,
    type WebhookRetrieveParams as WebhookRetrieveParams,
    type WebhookUpdateParams as WebhookUpdateParams,
    type WebhookDeleteParams as WebhookDeleteParams,
  };

  export {
    Trigger as Trigger,
    type TriggerUpdateResponse as TriggerUpdateResponse,
    type TriggerListResponse as TriggerListResponse,
    type TriggerUpdateParams as TriggerUpdateParams,
  };
}
