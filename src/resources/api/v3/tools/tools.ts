// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../../core/resource';
import * as ExecuteAPI from './execute';
import {
  Execute,
  ExecuteInputParams,
  ExecuteInputResponse,
  ExecuteProxyParams,
  ExecuteProxyResponse,
  ExecuteRunParams,
  ExecuteRunResponse,
} from './execute';
import { APIPromise } from '../../../../core/api-promise';
import { RequestOptions } from '../../../../internal/request-options';
import { path } from '../../../../internal/utils/path';

export class Tools extends APIResource {
  execute: ExecuteAPI.Execute = new ExecuteAPI.Execute(this._client);

  retrieve(toolSlug: string, options?: RequestOptions): APIPromise<ToolRetrieveResponse> {
    return this._client.get(path`/api/v3/tools/${toolSlug}`, options);
  }

  list(
    query: ToolListParams | null | undefined = {},
    options?: RequestOptions,
  ): APIPromise<ToolListResponse> {
    return this._client.get('/api/v3/tools', { query, ...options });
  }

  retrieveEnum(options?: RequestOptions): APIPromise<string> {
    return this._client.get('/api/v3/tools/enum', options);
  }
}

export interface ToolRetrieveResponse {
  available_versions: Array<string>;

  description: string;

  input_parameters: Record<string, unknown>;

  name: string;

  output_parameters: Record<string, unknown>;

  slug: string;

  tags: Array<string>;

  toolkit: ToolRetrieveResponse.Toolkit;

  version: string;
}

export namespace ToolRetrieveResponse {
  export interface Toolkit {
    logo: string;

    name: string;

    slug: string;
  }
}

export interface ToolListResponse {
  items: Array<ToolListResponse.Item>;

  next_cursor: string | null;

  total_pages: number;
}

export namespace ToolListResponse {
  export interface Item {
    /**
     * The description of the tool
     */
    description: string;

    /**
     * The input parameters of the tool
     */
    input_parameters: Record<string, unknown>;

    /**
     * The name of the tool
     */
    name: string;

    /**
     * The output parameters of the tool
     */
    output_parameters: Record<string, unknown>;

    /**
     * The slug of the tool
     */
    slug: string;

    /**
     * The tags of the tool
     */
    tags: Array<string>;

    toolkit: Item.Toolkit;
  }

  export namespace Item {
    export interface Toolkit {
      /**
       * The name of the toolkit
       */
      name: string;

      /**
       * The slug of the toolkit
       */
      slug: string;
    }
  }
}

export type ToolRetrieveEnumResponse = string;

export interface ToolListParams {
  /**
   * The cursor to paginate through the results
   */
  cursor?: string;

  /**
   * Whether to filter by important tools
   */
  important?: string;

  /**
   * The number of results to return
   */
  limit?: string;

  /**
   * The search query to filter by
   */
  search?: string;

  /**
   * The slug of the toolkit to filter by
   */
  toolkit_slug?: string;
}

Tools.Execute = Execute;

export declare namespace Tools {
  export {
    type ToolRetrieveResponse as ToolRetrieveResponse,
    type ToolListResponse as ToolListResponse,
    type ToolRetrieveEnumResponse as ToolRetrieveEnumResponse,
    type ToolListParams as ToolListParams,
  };

  export {
    Execute as Execute,
    type ExecuteInputResponse as ExecuteInputResponse,
    type ExecuteProxyResponse as ExecuteProxyResponse,
    type ExecuteRunResponse as ExecuteRunResponse,
    type ExecuteInputParams as ExecuteInputParams,
    type ExecuteProxyParams as ExecuteProxyParams,
    type ExecuteRunParams as ExecuteRunParams,
  };
}
