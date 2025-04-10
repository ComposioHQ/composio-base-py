// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';
import { path } from '../internal/utils/path';

export class AuthConfigs extends APIResource {
  create(body: AuthConfigCreateParams, options?: RequestOptions): APIPromise<AuthConfigCreateResponse> {
    return this._client.post('/api/v3/auth_configs', { body, ...options });
  }

  retrieve(nanoid: string, options?: RequestOptions): APIPromise<AuthConfigRetrieveResponse> {
    return this._client.get(path`/api/v3/auth_configs/${nanoid}`, options);
  }

  update(
    nanoid: string,
    body: AuthConfigUpdateParams,
    options?: RequestOptions,
  ): APIPromise<AuthConfigUpdateResponse> {
    return this._client.patch(path`/api/v3/auth_configs/${nanoid}`, { body, ...options });
  }

  list(
    query: AuthConfigListParams | null | undefined = {},
    options?: RequestOptions,
  ): APIPromise<AuthConfigListResponse> {
    return this._client.get('/api/v3/auth_configs', { query, ...options });
  }

  delete(nanoid: string, options?: RequestOptions): APIPromise<AuthConfigDeleteResponse> {
    return this._client.delete(path`/api/v3/auth_configs/${nanoid}`, options);
  }

  updateStatus(
    status: 'ENABLED' | 'DISABLED',
    params: AuthConfigUpdateStatusParams,
    options?: RequestOptions,
  ): APIPromise<AuthConfigUpdateStatusResponse> {
    const { nanoid } = params;
    return this._client.patch(path`/api/v3/auth_configs/${nanoid}/${status}`, options);
  }
}

export interface AuthConfigCreateResponse {
  auth_config: AuthConfigCreateResponse.AuthConfig;

  toolkit: AuthConfigCreateResponse.Toolkit;
}

export namespace AuthConfigCreateResponse {
  export interface AuthConfig {
    /**
     * The auth config id of the app (must be a valid auth config id)
     */
    id: string;

    /**
     * The authentication mode of the app
     */
    auth_scheme: string;

    /**
     * Whether the auth config is managed by Composio
     */
    is_composio_managed: boolean;
  }

  export interface Toolkit {
    /**
     * The unique key of the toolkit
     */
    slug: string;
  }
}

export interface AuthConfigRetrieveResponse {
  /**
   * The unique id of the auth config
   */
  id: string;

  /**
   * The name of the auth config
   */
  name: string;

  /**
   * The number of connections for the auth config
   */
  no_of_connections: number;

  status: 'ENABLED' | 'DISABLED';

  toolkit: AuthConfigRetrieveResponse.Toolkit;

  /**
   * The unique id of the auth config
   */
  uuid: string;

  auth_scheme?:
    | 'OAUTH2'
    | 'OAUTH1'
    | 'OAUTH1A'
    | 'API_KEY'
    | 'BASIC'
    | 'BILLCOM_AUTH'
    | 'BEARER_TOKEN'
    | 'GOOGLE_SERVICE_ACCOUNT'
    | 'NO_AUTH'
    | 'BASIC_WITH_JWT'
    | 'COMPOSIO_LINK'
    | 'CALCOM_AUTH'
    | 'SNOWFLAKE';

  /**
   * The date and time the auth config was created
   */
  created_at?: string;

  /**
   * The user who created the auth config
   */
  created_by?: string;

  credentials?: Record<string, unknown>;

  expected_input_fields?: Array<unknown>;

  is_composio_managed?: boolean;

  /**
   * The date and time the auth config was last updated
   */
  last_updated_at?: string;
}

export namespace AuthConfigRetrieveResponse {
  export interface Toolkit {
    /**
     * The logo of the app
     */
    logo: string;

    /**
     * The unique key of the app
     */
    slug: string;
  }
}

export interface AuthConfigUpdateResponse {
  message: string;

  success: boolean;
}

export interface AuthConfigListResponse {
  items: Array<AuthConfigListResponse.Item>;

  next_cursor: string | null;

  total_pages: number;
}

export namespace AuthConfigListResponse {
  export interface Item {
    /**
     * The unique id of the auth config
     */
    id: string;

    /**
     * The name of the auth config
     */
    name: string;

    /**
     * The number of connections for the auth config
     */
    no_of_connections: number;

    status: 'ENABLED' | 'DISABLED';

    toolkit: Item.Toolkit;

    /**
     * The unique id of the auth config
     */
    uuid: string;

    auth_scheme?:
      | 'OAUTH2'
      | 'OAUTH1'
      | 'OAUTH1A'
      | 'API_KEY'
      | 'BASIC'
      | 'BILLCOM_AUTH'
      | 'BEARER_TOKEN'
      | 'GOOGLE_SERVICE_ACCOUNT'
      | 'NO_AUTH'
      | 'BASIC_WITH_JWT'
      | 'COMPOSIO_LINK'
      | 'CALCOM_AUTH'
      | 'SNOWFLAKE';

    /**
     * The date and time the auth config was created
     */
    created_at?: string;

    /**
     * The user who created the auth config
     */
    created_by?: string;

    credentials?: Record<string, unknown>;

    expected_input_fields?: Array<unknown>;

    is_composio_managed?: boolean;

    /**
     * The date and time the auth config was last updated
     */
    last_updated_at?: string;
  }

  export namespace Item {
    export interface Toolkit {
      /**
       * The logo of the app
       */
      logo: string;

      /**
       * The unique key of the app
       */
      slug: string;
    }
  }
}

export interface AuthConfigDeleteResponse {
  message: string;

  success: boolean;
}

export interface AuthConfigUpdateStatusResponse {
  message: string;

  success: boolean;
}

export interface AuthConfigCreateParams {
  toolkit: AuthConfigCreateParams.Toolkit;

  auth_config?: AuthConfigCreateParams.UnionMember0 | AuthConfigCreateParams.UnionMember1;
}

export namespace AuthConfigCreateParams {
  export interface Toolkit {
    /**
     * List of app unique keys to filter by
     */
    slug: string;
  }

  export interface UnionMember0 {
    type: 'use_composio_managed_auth';

    credentials?: Record<string, string | boolean | number>;

    /**
     * The name of the integration
     */
    name?: string;
  }

  export interface UnionMember1 {
    authScheme:
      | 'OAUTH2'
      | 'OAUTH1'
      | 'OAUTH1A'
      | 'API_KEY'
      | 'BASIC'
      | 'BILLCOM_AUTH'
      | 'BEARER_TOKEN'
      | 'GOOGLE_SERVICE_ACCOUNT'
      | 'NO_AUTH'
      | 'BASIC_WITH_JWT'
      | 'COMPOSIO_LINK'
      | 'CALCOM_AUTH'
      | 'SNOWFLAKE';

    credentials: Record<string, string | boolean | number>;

    type: 'use_custom_auth';

    /**
     * The name of the integration
     */
    name?: string;
  }
}

export interface AuthConfigUpdateParams {
  auth_config: AuthConfigUpdateParams.AuthConfig;
}

export namespace AuthConfigUpdateParams {
  export interface AuthConfig {
    /**
     * Authentication configuration
     */
    credentials?: Record<string, unknown>;
  }
}

export interface AuthConfigListParams {
  /**
   * The cursor to paginate through the auth configs
   */
  cursor?: string;

  /**
   * Whether to filter by composio managed auth configs
   */
  is_composio_managed?: string | boolean;

  /**
   * The number of auth configs to return
   */
  limit?: string;

  /**
   * The slug of the toolkit to filter by
   */
  toolkit_slug?: string;
}

export interface AuthConfigUpdateStatusParams {
  nanoid: string;
}

export declare namespace AuthConfigs {
  export {
    type AuthConfigCreateResponse as AuthConfigCreateResponse,
    type AuthConfigRetrieveResponse as AuthConfigRetrieveResponse,
    type AuthConfigUpdateResponse as AuthConfigUpdateResponse,
    type AuthConfigListResponse as AuthConfigListResponse,
    type AuthConfigDeleteResponse as AuthConfigDeleteResponse,
    type AuthConfigUpdateStatusResponse as AuthConfigUpdateStatusResponse,
    type AuthConfigCreateParams as AuthConfigCreateParams,
    type AuthConfigUpdateParams as AuthConfigUpdateParams,
    type AuthConfigListParams as AuthConfigListParams,
    type AuthConfigUpdateStatusParams as AuthConfigUpdateStatusParams,
  };
}
