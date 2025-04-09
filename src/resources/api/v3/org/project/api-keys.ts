// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../../../core/resource';
import { APIPromise } from '../../../../../core/api-promise';
import { RequestOptions } from '../../../../../internal/request-options';
import { path } from '../../../../../internal/utils/path';

export class APIKeys extends APIResource {
  create(
    projectID: string,
    body: APIKeyCreateParams,
    options?: RequestOptions,
  ): APIPromise<APIKeyCreateResponse> {
    return this._client.post(path`/api/v3/org/project/${projectID}/api_keys/create`, { body, ...options });
  }

  list(projectID: string, options?: RequestOptions): APIPromise<APIKeyListResponse> {
    return this._client.get(path`/api/v3/org/project/${projectID}/api_keys/list`, options);
  }

  delete(id: string, params: APIKeyDeleteParams, options?: RequestOptions): APIPromise<APIKeyDeleteResponse> {
    const { projectId } = params;
    return this._client.delete(path`/api/v3/org/project/${projectId}/api_keys/remove/${id}`, options);
  }

  createAPIKey(projectID: string, options?: RequestOptions): APIPromise<APIKeyCreateAPIKeyResponse> {
    return this._client.post(path`/api/v3/org/project/${projectID}/api_keys/create-api-key`, options);
  }
}

export interface APIKeyCreateResponse {
  /**
   * API key ID
   */
  id: string;

  /**
   * Creation timestamp
   */
  createdAt: string;

  /**
   * API key value
   */
  key: string;

  /**
   * API key name
   */
  name: string;

  /**
   * Last used timestamp
   */
  lastUsed?: string;
}

export interface APIKeyListResponse {
  /**
   * List of API keys
   */
  items: Array<APIKeyListResponse.Item>;
}

export namespace APIKeyListResponse {
  export interface Item {
    /**
     * API key ID
     */
    id: string;

    /**
     * Creation timestamp
     */
    created_at: string;

    /**
     * API key value
     */
    key: string;

    /**
     * API key name
     */
    name: string;

    /**
     * Last used timestamp
     */
    last_used?: string;
  }
}

export interface APIKeyDeleteResponse {
  /**
   * Status message
   */
  message: string;

  /**
   * Whether the operation was successful
   */
  success: boolean;
}

export interface APIKeyCreateAPIKeyResponse {
  /**
   * API key ID
   */
  id: string;

  /**
   * Creation timestamp
   */
  createdAt: string;

  /**
   * API key value
   */
  key: string;

  /**
   * API key name
   */
  name: string;

  /**
   * Last used timestamp
   */
  lastUsed?: string;
}

export interface APIKeyCreateParams {
  /**
   * API key name
   */
  name: string;
}

export interface APIKeyDeleteParams {
  /**
   * Project ID
   */
  projectId: string;
}

export declare namespace APIKeys {
  export {
    type APIKeyCreateResponse as APIKeyCreateResponse,
    type APIKeyListResponse as APIKeyListResponse,
    type APIKeyDeleteResponse as APIKeyDeleteResponse,
    type APIKeyCreateAPIKeyResponse as APIKeyCreateAPIKeyResponse,
    type APIKeyCreateParams as APIKeyCreateParams,
    type APIKeyDeleteParams as APIKeyDeleteParams,
  };
}
