// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import { APIPromise } from '../../core/api-promise';
import { RequestOptions } from '../../internal/request-options';
import { path } from '../../internal/utils/path';

export class Execute extends APIResource {
  getInput(
    actionName: string,
    body: ExecuteGetInputParams,
    options?: RequestOptions,
  ): APIPromise<ExecuteGetInputResponse> {
    return this._client.post(path`/api/v3/tools/execute/${actionName}/input`, { body, ...options });
  }

  proxy(body: ExecuteProxyParams, options?: RequestOptions): APIPromise<ExecuteProxyResponse> {
    return this._client.post('/api/v3/tools/execute/proxy', { body, ...options });
  }
}

export interface ExecuteGetInputResponse {
  /**
   * The arguments for the action needed to execute the given task.
   */
  arguments?: Record<string, unknown>;

  /**
   * The error message if the arguments were not generated successfully.
   */
  error?: string;
}

export interface ExecuteProxyResponse {
  status: number;

  data?: unknown;

  headers?: Record<string, string>;
}

export interface ExecuteGetInputParams {
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

export interface ExecuteProxyParams {
  endpoint: string;

  method: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';

  body?: unknown;

  connected_account_id?: string;

  parameters?: Array<ExecuteProxyParams.Parameter>;
}

export namespace ExecuteProxyParams {
  export interface Parameter {
    name: string;

    type: 'header' | 'query';

    value: string;
  }
}

export declare namespace Execute {
  export {
    type ExecuteGetInputResponse as ExecuteGetInputResponse,
    type ExecuteProxyResponse as ExecuteProxyResponse,
    type ExecuteGetInputParams as ExecuteGetInputParams,
    type ExecuteProxyParams as ExecuteProxyParams,
  };
}
