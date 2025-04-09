// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';
import { path } from '../internal/utils/path';

export class ConnectedAccounts extends APIResource {
  create(
    body: ConnectedAccountCreateParams,
    options?: RequestOptions,
  ): APIPromise<ConnectedAccountCreateResponse> {
    return this._client.post('/api/v3/connected_accounts', { body, ...options });
  }

  retrieve(nanoid: string, options?: RequestOptions): APIPromise<ConnectedAccountRetrieveResponse> {
    return this._client.get(path`/api/v3/connected_accounts/${nanoid}`, options);
  }

  list(
    query: ConnectedAccountListParams | null | undefined = {},
    options?: RequestOptions,
  ): APIPromise<ConnectedAccountListResponse> {
    return this._client.get('/api/v3/connected_accounts', { query, ...options });
  }

  delete(nanoid: string, options?: RequestOptions): APIPromise<ConnectedAccountDeleteResponse> {
    return this._client.delete(path`/api/v3/connected_accounts/${nanoid}`, options);
  }

  refresh(nanoid: string, options?: RequestOptions): APIPromise<ConnectedAccountRefreshResponse> {
    return this._client.post(path`/api/v3/connected_accounts/${nanoid}/refresh`, options);
  }

  updateStatus(
    nanoID: string,
    body: ConnectedAccountUpdateStatusParams,
    options?: RequestOptions,
  ): APIPromise<ConnectedAccountUpdateStatusResponse> {
    return this._client.patch(path`/api/v3/connected_accounts/${nanoID}/status`, { body, ...options });
  }
}

export interface ConnectedAccountCreateResponse {
  /**
   * The id of the connected account
   */
  id: string;

  /**
   * The redirect uri of the app
   */
  redirect_uri: string | null;

  /**
   * The status of the connected account
   */
  status: 'ACTIVE' | 'INACTIVE' | 'DELETED' | 'INITIATED' | 'EXPIRED' | 'FAILED';
}

export interface ConnectedAccountRetrieveResponse {
  /**
   * The id of the connection
   */
  id: string;

  auth_config: ConnectedAccountRetrieveResponse.AuthConfig;

  /**
   * The created at of the connection
   */
  created_at: string;

  /**
   * The data of the connection
   */
  data: Record<string, unknown>;

  /**
   * Whether the connected account is disabled
   */
  is_disabled: boolean;

  /**
   * The init data of the connection
   */
  params: Record<string, unknown>;

  /**
   * The status of the connection
   */
  status: 'ACTIVE' | 'INACTIVE' | 'DELETED' | 'INITIATED' | 'EXPIRED' | 'FAILED';

  /**
   * The reason the connected account is disabled
   */
  status_reason: string | null;

  toolkit: ConnectedAccountRetrieveResponse.Toolkit;

  /**
   * The updated at of the connection
   */
  updated_at: string;

  /**
   * The user id of the connection
   */
  user_id: string;

  /**
   * The uuid of the connection
   */
  uuid: string;

  /**
   * The endpoint to make test request for verification
   */
  test_request_endpoint?: string;
}

export namespace ConnectedAccountRetrieveResponse {
  export interface AuthConfig {
    /**
     * The id of the auth config
     */
    id: string;

    /**
     * The auth scheme of the auth config
     */
    auth_scheme:
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
     * Whether the auth config is managed by Composio
     */
    is_composio_managed: boolean;

    /**
     * Whether the auth config is disabled
     */
    is_disabled: boolean;
  }

  export interface Toolkit {
    /**
     * The slug of the toolkit
     */
    slug: string;
  }
}

export interface ConnectedAccountListResponse {
  items: Array<ConnectedAccountListResponse.Item>;

  next_cursor: string | null;

  total_pages: number;
}

export namespace ConnectedAccountListResponse {
  export interface Item {
    /**
     * The id of the connection
     */
    id: string;

    auth_config: Item.AuthConfig;

    /**
     * The created at of the connection
     */
    created_at: string;

    /**
     * The data of the connection
     */
    data: Record<string, unknown>;

    /**
     * Whether the connection is disabled
     */
    is_disabled: boolean;

    /**
     * The status of the connection
     */
    status: 'ACTIVE' | 'INACTIVE' | 'DELETED' | 'INITIATED' | 'EXPIRED' | 'FAILED';

    /**
     * The reason the connection is disabled
     */
    status_reason: string | null;

    toolkit: Item.Toolkit;

    /**
     * The updated at of the connection
     */
    updated_at: string;

    /**
     * The user id of the connection
     */
    user_id: string;

    /**
     * The endpoint to make test request for verification
     */
    test_request_endpoint?: string;

    /**
     * The uuid of the connected account
     */
    uuid?: string;
  }

  export namespace Item {
    export interface AuthConfig {
      /**
       * The id of the auth config
       */
      id: string;

      /**
       * The auth scheme of the auth config
       */
      auth_scheme:
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
       * Whether the auth config is managed by Composio
       */
      is_composio_managed: boolean;

      /**
       * Whether the auth config is disabled
       */
      is_disabled: boolean;
    }

    export interface Toolkit {
      /**
       * The slug of the toolkit
       */
      slug: string;
    }
  }
}

export interface ConnectedAccountDeleteResponse {
  /**
   * The id of the connection
   */
  id: string;

  auth_config: ConnectedAccountDeleteResponse.AuthConfig;

  /**
   * The created at of the connection
   */
  created_at: string;

  /**
   * The data of the connection
   */
  data: Record<string, unknown>;

  /**
   * Whether the connection is disabled
   */
  is_disabled: boolean;

  /**
   * The status of the connection
   */
  status: 'ACTIVE' | 'INACTIVE' | 'DELETED' | 'INITIATED' | 'EXPIRED' | 'FAILED';

  /**
   * The reason the connection is disabled
   */
  status_reason: string | null;

  toolkit: ConnectedAccountDeleteResponse.Toolkit;

  /**
   * The updated at of the connection
   */
  updated_at: string;

  /**
   * The user id of the connection
   */
  user_id: string;

  /**
   * The uuid of the connection
   */
  uuid: string;

  /**
   * The endpoint to make test request for verification
   */
  test_request_endpoint?: string;
}

export namespace ConnectedAccountDeleteResponse {
  export interface AuthConfig {
    /**
     * The id of the auth config
     */
    id: string;

    /**
     * The auth scheme of the auth config
     */
    auth_scheme:
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
     * Whether the auth config is managed by Composio
     */
    is_composio_managed: boolean;

    /**
     * Whether the auth config is disabled
     */
    is_disabled: boolean;
  }

  export interface Toolkit {
    /**
     * The slug of the toolkit
     */
    slug: string;
  }
}

export interface ConnectedAccountRefreshResponse {
  /**
   * The id of the connection
   */
  id: string;

  auth_config: ConnectedAccountRefreshResponse.AuthConfig;

  /**
   * The created at of the connection
   */
  created_at: string;

  /**
   * The data of the connection
   */
  data: Record<string, unknown>;

  /**
   * Whether the connection is disabled
   */
  is_disabled: boolean;

  /**
   * The status of the connection
   */
  status: 'ACTIVE' | 'INACTIVE' | 'DELETED' | 'INITIATED' | 'EXPIRED' | 'FAILED';

  /**
   * The reason the connection is disabled
   */
  status_reason: string | null;

  toolkit: ConnectedAccountRefreshResponse.Toolkit;

  /**
   * The updated at of the connection
   */
  updated_at: string;

  /**
   * The user id of the connection
   */
  user_id: string;

  /**
   * The uuid of the connection
   */
  uuid: string;

  /**
   * The endpoint to make test request for verification
   */
  test_request_endpoint?: string;
}

export namespace ConnectedAccountRefreshResponse {
  export interface AuthConfig {
    /**
     * The id of the auth config
     */
    id: string;

    /**
     * The auth scheme of the auth config
     */
    auth_scheme:
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
     * Whether the auth config is managed by Composio
     */
    is_composio_managed: boolean;

    /**
     * Whether the auth config is disabled
     */
    is_disabled: boolean;
  }

  export interface Toolkit {
    /**
     * The slug of the toolkit
     */
    slug: string;
  }
}

export interface ConnectedAccountUpdateStatusResponse {
  /**
   * The id of the connection
   */
  id: string;

  auth_config: ConnectedAccountUpdateStatusResponse.AuthConfig;

  /**
   * The created at of the connection
   */
  created_at: string;

  /**
   * The data of the connection
   */
  data: Record<string, unknown>;

  /**
   * Whether the connection is disabled
   */
  is_disabled: boolean;

  /**
   * The status of the connection
   */
  status: 'ACTIVE' | 'INACTIVE' | 'DELETED' | 'INITIATED' | 'EXPIRED' | 'FAILED';

  /**
   * The reason the connection is disabled
   */
  status_reason: string | null;

  toolkit: ConnectedAccountUpdateStatusResponse.Toolkit;

  /**
   * The updated at of the connection
   */
  updated_at: string;

  /**
   * The user id of the connection
   */
  user_id: string;

  /**
   * The uuid of the connection
   */
  uuid: string;

  /**
   * The endpoint to make test request for verification
   */
  test_request_endpoint?: string;
}

export namespace ConnectedAccountUpdateStatusResponse {
  export interface AuthConfig {
    /**
     * The id of the auth config
     */
    id: string;

    /**
     * The auth scheme of the auth config
     */
    auth_scheme:
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
     * Whether the auth config is managed by Composio
     */
    is_composio_managed: boolean;

    /**
     * Whether the auth config is disabled
     */
    is_disabled: boolean;
  }

  export interface Toolkit {
    /**
     * The slug of the toolkit
     */
    slug: string;
  }
}

export interface ConnectedAccountCreateParams {
  auth_config: ConnectedAccountCreateParams.AuthConfig;

  connection: ConnectedAccountCreateParams.Connection;
}

export namespace ConnectedAccountCreateParams {
  export interface AuthConfig {
    /**
     * The auth config id of the app (must be a valid auth config id)
     */
    id: string;
  }

  export interface Connection {
    /**
     * Initial data to pass to the connected account
     */
    data?: Record<string, unknown>;

    /**
     * The URL to redirect to after connection completion
     */
    redirect_uri?: string;

    /**
     * The user id of the connected account
     */
    user_id?: string;
  }
}

export interface ConnectedAccountListParams {
  /**
   * The auth config id of the connected account
   */
  auth_config_id?: string;

  /**
   * The cursor to paginate through the connected accounts
   */
  cursor?: number | null;

  /**
   * The limit of the connected accounts to return
   */
  limit?: number | null;

  /**
   * The order by of the connected accounts
   */
  order_by?: 'created_at' | 'updated_at';

  /**
   * The status of the connected account
   */
  status?: 'ACTIVE' | 'INACTIVE' | 'DELETED' | 'INITIATED' | 'EXPIRED' | 'FAILED';

  /**
   * The toolkit slug of the connected account
   */
  toolkit_slug?: string;

  /**
   * The user id of the connected account
   */
  user_id?: string;
}

export interface ConnectedAccountUpdateStatusParams {
  enabled: boolean;
}

export declare namespace ConnectedAccounts {
  export {
    type ConnectedAccountCreateResponse as ConnectedAccountCreateResponse,
    type ConnectedAccountRetrieveResponse as ConnectedAccountRetrieveResponse,
    type ConnectedAccountListResponse as ConnectedAccountListResponse,
    type ConnectedAccountDeleteResponse as ConnectedAccountDeleteResponse,
    type ConnectedAccountRefreshResponse as ConnectedAccountRefreshResponse,
    type ConnectedAccountUpdateStatusResponse as ConnectedAccountUpdateStatusResponse,
    type ConnectedAccountCreateParams as ConnectedAccountCreateParams,
    type ConnectedAccountListParams as ConnectedAccountListParams,
    type ConnectedAccountUpdateStatusParams as ConnectedAccountUpdateStatusParams,
  };
}
