// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../../core/resource';
import { APIPromise } from '../../../../core/api-promise';
import { RequestOptions } from '../../../../internal/request-options';
import { path } from '../../../../internal/utils/path';

export class Execute extends APIResource {
  input(
    actionName: string,
    body: ExecuteInputParams,
    options?: RequestOptions,
  ): APIPromise<ExecuteInputResponse> {
    return this._client.post(path`/api/v3/tools/execute/${actionName}/input`, { body, ...options });
  }

  proxy(body: ExecuteProxyParams, options?: RequestOptions): APIPromise<ExecuteProxyResponse> {
    return this._client.post('/api/v3/tools/execute/proxy', { body, ...options });
  }

  run(
    action: string,
    body: ExecuteRunParams | null | undefined = {},
    options?: RequestOptions,
  ): APIPromise<ExecuteRunResponse> {
    return this._client.post(path`/api/v3/tools/execute/${action}`, { body, ...options });
  }
}

export interface ExecuteInputResponse {
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

export interface ExecuteRunResponse {
  data: Record<string, unknown>;

  error: string | null;

  successful: boolean;

  log_id?: string;

  session_info?: unknown;
}

export interface ExecuteInputParams {
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

export interface ExecuteRunParams {
  allow_tracing?: boolean;

  arguments?: Record<string, unknown>;

  connected_account_id?: string;

  entity_id?: string;

  text?: string;

  version?: string;
}

export declare namespace Execute {
  export {
    type ExecuteInputResponse as ExecuteInputResponse,
    type ExecuteProxyResponse as ExecuteProxyResponse,
    type ExecuteRunResponse as ExecuteRunResponse,
    type ExecuteInputParams as ExecuteInputParams,
    type ExecuteProxyParams as ExecuteProxyParams,
    type ExecuteRunParams as ExecuteRunParams,
  };
}
