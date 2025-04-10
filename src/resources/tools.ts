// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';
import { path } from '../internal/utils/path';

export class Tools extends APIResource {
  retrieve(toolSlug: string, options?: RequestOptions): APIPromise<ToolRetrieveResponse> {
    return this._client.get(path`/api/v3/tools/${toolSlug}`, options);
  }

  list(
    query: ToolListParams | null | undefined = {},
    options?: RequestOptions,
  ): APIPromise<ToolListResponse> {
    return this._client.get('/api/v3/tools', { query, ...options });
  }

  execute(
    action: string,
    body: ToolExecuteParams | null | undefined = {},
    options?: RequestOptions,
  ): APIPromise<ToolExecuteResponse> {
    return this._client.post(path`/api/v3/tools/execute/${action}`, { body, ...options });
  }

  getInput(
    actionName: string,
    body: ToolGetInputParams,
    options?: RequestOptions,
  ): APIPromise<ToolGetInputResponse> {
    return this._client.post(path`/api/v3/tools/execute/${actionName}/input`, { body, ...options });
  }

  proxy(body: ToolProxyParams, options?: RequestOptions): APIPromise<ToolProxyResponse> {
    return this._client.post('/api/v3/tools/execute/proxy', { body, ...options });
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

export interface ToolExecuteResponse {
  data: Record<string, unknown>;

  error: string | null;

  successful: boolean;

  log_id?: string;

  session_info?: unknown;
}

export interface ToolGetInputResponse {
  /**
   * The arguments for the action needed to execute the given task.
   */
  arguments?: Record<string, unknown>;

  /**
   * The error message if the arguments were not generated successfully.
   */
  error?: string;
}

export interface ToolProxyResponse {
  status: number;

  data?: unknown;

  headers?: Record<string, string>;
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

export interface ToolExecuteParams {
  allow_tracing?: boolean;

  arguments?: Record<string, unknown>;

  connected_account_id?: string;

  entity_id?: string;

  text?: string;

  version?: string;
}

export interface ToolGetInputParams {
  /**
   * The use-case description for the action, this will give context to LLM to
   * generate the correct inputs for the action.
   */
  text: string;

  /**
   * The custom description for the action, use this to provide customised context
   * about the action to the LLM to suit your use-case.
   */
  customDescription?: string;

  /**
   * The system prompt to be used by LLM, use this to control and guide the behaviour
   * of the LLM.
   */
  systemPrompt?: string;

  version?: string;
}

export interface ToolProxyParams {
  endpoint: string;

  method: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';

  body?: unknown;

  connected_account_id?: string;

  parameters?: Array<ToolProxyParams.Parameter>;
}

export namespace ToolProxyParams {
  export interface Parameter {
    name: string;

    type: 'header' | 'query';

    value: string;
  }
}

export declare namespace Tools {
  export {
    type ToolRetrieveResponse as ToolRetrieveResponse,
    type ToolListResponse as ToolListResponse,
    type ToolExecuteResponse as ToolExecuteResponse,
    type ToolGetInputResponse as ToolGetInputResponse,
    type ToolProxyResponse as ToolProxyResponse,
    type ToolRetrieveEnumResponse as ToolRetrieveEnumResponse,
    type ToolListParams as ToolListParams,
    type ToolExecuteParams as ToolExecuteParams,
    type ToolGetInputParams as ToolGetInputParams,
    type ToolProxyParams as ToolProxyParams,
  };
}
