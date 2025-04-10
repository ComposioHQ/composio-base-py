// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';
import { path } from '../internal/utils/path';

export class TriggersTypes extends APIResource {
  retrieve(slug: string, options?: RequestOptions): APIPromise<TriggersTypeRetrieveResponse> {
    return this._client.get(path`/api/v3/triggers_types/${slug}`, options);
  }

  list(
    query: TriggersTypeListParams | null | undefined = {},
    options?: RequestOptions,
  ): APIPromise<TriggersTypeListResponse> {
    return this._client.get('/api/v3/triggers_types', { query, ...options });
  }

  retrieveEnum(options?: RequestOptions): APIPromise<string> {
    return this._client.get('/api/v3/triggers_types/list/enum', options);
  }
}

export interface TriggersTypeRetrieveResponse {
  config: Record<string, unknown>;

  description: string;

  instructions: string;

  name: string;

  payload: Record<string, unknown>;

  slug: string;

  toolkit: TriggersTypeRetrieveResponse.Toolkit;
}

export namespace TriggersTypeRetrieveResponse {
  export interface Toolkit {
    logo: string;

    name: string;

    uuid: string;
  }
}

export interface TriggersTypeListResponse {
  items: Array<TriggersTypeListResponse.Item>;

  next_cursor: string | null;

  total_pages: number;
}

export namespace TriggersTypeListResponse {
  export interface Item {
    description: string;

    name: string;

    slug: string;

    toolkit: Item.Toolkit;

    type: 'webhook' | 'poll';
  }

  export namespace Item {
    export interface Toolkit {
      name: string;

      slug: string;
    }
  }
}

export type TriggersTypeRetrieveEnumResponse = string;

export interface TriggersTypeListParams {
  auth_config_id?: string;

  connected_account_id?: string;

  cursor?: string;

  limit?: number | null;

  /**
   * Comma separated list of toolkit slugs
   */
  toolkit_slugs?: string;
}

export declare namespace TriggersTypes {
  export {
    type TriggersTypeRetrieveResponse as TriggersTypeRetrieveResponse,
    type TriggersTypeListResponse as TriggersTypeListResponse,
    type TriggersTypeRetrieveEnumResponse as TriggersTypeRetrieveEnumResponse,
    type TriggersTypeListParams as TriggersTypeListParams,
  };
}
