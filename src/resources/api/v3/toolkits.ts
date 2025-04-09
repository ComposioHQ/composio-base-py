// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../core/resource';
import { APIPromise } from '../../../core/api-promise';
import { RequestOptions } from '../../../internal/request-options';
import { path } from '../../../internal/utils/path';

export class Toolkits extends APIResource {
  retrieve(slug: string, options?: RequestOptions): APIPromise<ToolkitRetrieveResponse> {
    return this._client.get(path`/api/v3/toolkits/${slug}`, options);
  }

  list(
    query: ToolkitListParams | null | undefined = {},
    options?: RequestOptions,
  ): APIPromise<ToolkitListResponse> {
    return this._client.get('/api/v3/toolkits', { query, ...options });
  }

  retrieveCategories(options?: RequestOptions): APIPromise<ToolkitRetrieveCategoriesResponse> {
    return this._client.get('/api/v3/toolkits/categories', options);
  }
}

export interface ToolkitRetrieveResponse {
  enabled: boolean;

  is_local_toolkit: boolean;

  meta: ToolkitRetrieveResponse.Meta;

  name: string;

  slug: string;

  auth_config_details?: Array<ToolkitRetrieveResponse.AuthConfigDetail>;

  composio_managed_auth_schemes?: Array<string>;
}

export namespace ToolkitRetrieveResponse {
  export interface Meta {
    categories: Array<Meta.Category>;

    created_at: string;

    description: string;

    logo: string;

    tools_count: number;

    triggers_count: number;

    updated_at: string;
  }

  export namespace Meta {
    export interface Category {
      name: string;

      slug: string;
    }
  }

  export interface AuthConfigDetail {
    fields: AuthConfigDetail.Fields;

    mode: string;

    name: string;

    proxy?: AuthConfigDetail.Proxy;
  }

  export namespace AuthConfigDetail {
    export interface Fields {
      auth_config_creation: Fields.AuthConfigCreation;

      connected_account_initiation: Fields.ConnectedAccountInitiation;
    }

    export namespace Fields {
      export interface AuthConfigCreation {
        optional: Array<AuthConfigCreation.Optional>;

        required: Array<AuthConfigCreation.Required>;
      }

      export namespace AuthConfigCreation {
        export interface Optional {
          displayName: string;

          name: string;

          type: string;

          default?: string | null;
        }

        export interface Required {
          displayName: string;

          name: string;

          type: string;

          default?: string | null;
        }
      }

      export interface ConnectedAccountInitiation {
        optional: Array<ConnectedAccountInitiation.Optional>;

        required: Array<ConnectedAccountInitiation.Required>;
      }

      export namespace ConnectedAccountInitiation {
        export interface Optional {
          displayName: string;

          name: string;

          type: string;

          default?: string | null;
        }

        export interface Required {
          displayName: string;

          name: string;

          type: string;

          default?: string | null;
        }
      }
    }

    export interface Proxy {
      base_url: string;
    }
  }
}

export interface ToolkitListResponse {
  items: Array<ToolkitListResponse.Item>;

  next_cursor: string | null;

  total_pages: number;
}

export namespace ToolkitListResponse {
  export interface Item {
    is_local_toolkit: boolean;

    meta: Item.Meta;

    name: string;

    slug: string;

    auth_schemes?: Array<string>;

    composio_managed_auth_schemes?: Array<string>;

    no_auth?: boolean;
  }

  export namespace Item {
    export interface Meta {
      categories: Array<Meta.Category>;

      created_at: string;

      description: string;

      logo: string;

      tools_count: number;

      triggers_count: number;

      updated_at: string;
    }

    export namespace Meta {
      export interface Category {
        id: string;

        name: string;
      }
    }
  }
}

export interface ToolkitRetrieveCategoriesResponse {
  items: Array<ToolkitRetrieveCategoriesResponse.Item>;

  next_cursor: string | null;

  total_pages: number;
}

export namespace ToolkitRetrieveCategoriesResponse {
  export interface Item {
    id: string;

    name: string;
  }
}

export interface ToolkitListParams {
  category?: string;

  is_local?: boolean;

  managed_by?: 'all' | 'composio_managed' | 'project_managed';

  sort_by?: 'usage' | 'alphabetically';
}

export declare namespace Toolkits {
  export {
    type ToolkitRetrieveResponse as ToolkitRetrieveResponse,
    type ToolkitListResponse as ToolkitListResponse,
    type ToolkitRetrieveCategoriesResponse as ToolkitRetrieveCategoriesResponse,
    type ToolkitListParams as ToolkitListParams,
  };
}
