// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../../core/resource';
import { APIPromise } from '../../../../core/api-promise';
import { RequestOptions } from '../../../../internal/request-options';
import { path } from '../../../../internal/utils/path';

export class ActionExecution extends APIResource {
  log(body: ActionExecutionLogParams, options?: RequestOptions): APIPromise<ActionExecutionLogResponse> {
    return this._client.post('/api/v3/internal/action_execution/logs', { body, ...options });
  }

  retrieveFields(options?: RequestOptions): APIPromise<ActionExecutionRetrieveFieldsResponse> {
    return this._client.get('/api/v3/internal/action_execution/fields', options);
  }

  retrieveLog(id: string, options?: RequestOptions): APIPromise<ActionExecutionRetrieveLogResponse> {
    return this._client.get(path`/api/v3/internal/action_execution/log/${id}`, options);
  }
}

export interface ActionExecutionLogResponse {
  data: Array<ActionExecutionLogResponse.Data>;

  nextCursor: number | null;
}

export namespace ActionExecutionLogResponse {
  export interface Data {
    id: string;

    actionKey: string;

    app: Data.App;

    appKey: string;

    connectedAccountId: string;

    createdAt: number;

    entityId: string;

    executionTime: number;

    minimalResponse: string;

    status: 'success' | 'failed';
  }

  export namespace Data {
    export interface App {
      icon: string;

      name: string;
    }
  }
}

export interface ActionExecutionRetrieveFieldsResponse {
  fields: Record<string, Array<ActionExecutionRetrieveFieldsResponse.Field>>;
}

export namespace ActionExecutionRetrieveFieldsResponse {
  export interface Field {
    /**
     * The id of the field
     */
    id: string;

    /**
     * The display name of the field
     */
    displayName: string;

    /**
     * The type of the field
     */
    type: string;

    /**
     * The regex of the field
     */
    regex?: string;
  }
}

export interface ActionExecutionRetrieveLogResponse {
  actionId: string;

  actionLogId: string;

  app: ActionExecutionRetrieveLogResponse.App;

  connection: ActionExecutionRetrieveLogResponse.Connection;

  endTime: number;

  error: Record<string, unknown>;

  executionMetadata: Record<string, unknown>;

  payloadReceived: Record<string, unknown>;

  response: Record<string, unknown>;

  session: Record<string, unknown>;

  startTime: number;

  status: 'success' | 'error' | 'warning' | 'info';

  steps: Array<ActionExecutionRetrieveLogResponse.Step>;

  totalDuration: string;

  version: string;
}

export namespace ActionExecutionRetrieveLogResponse {
  export interface App {
    icon: string;

    name: string;

    uniqueId: string;
  }

  export interface Connection {
    entity: string;

    id?: string;
  }

  export interface Step {
    endTime: number;

    message: string;

    startTime: number;

    status: 'success' | 'error';

    totalDuration: number;

    type: 'tool_execution' | 'fetch_connection_details';

    logs?: Array<Step.Log>;

    metadata?: Step.Metadata;
  }

  export namespace Step {
    export interface Log {
      level: string;

      message: string;

      request: Log.Request;

      requestId: string;

      response: Log.Response;

      time: number;

      type: 'network' | 'system';
    }

    export namespace Log {
      export interface Request {
        method: string;

        url: string;

        headers?: Record<string, string>;

        json?: Record<string, unknown>;

        params?: Record<string, unknown>;

        timeout?: number;
      }

      export interface Response {
        status: number;

        time: string;
      }
    }

    export interface Metadata {
      encryption?: string;
    }
  }
}

export interface ActionExecutionLogParams {
  /**
   * cursor_that_can_be_used_to_paginate_through_the_logs
   */
  cursor: number | null;

  /**
   * whether_the_search_is_case_sensitive_or_not
   */
  case_sensitive?: boolean;

  /**
   * start_time_of_the_logs_in_epoch_time
   */
  from?: number;

  /**
   * number_of_logs_to_return
   */
  limit?: number;

  search_params?: Array<ActionExecutionLogParams.SearchParam>;

  /**
   * end_time_of_the_logs_in_epoch_time
   */
  to?: number;
}

export namespace ActionExecutionLogParams {
  export interface SearchParam {
    field?: string;

    operation?: string;

    value?: string;
  }
}

export declare namespace ActionExecution {
  export {
    type ActionExecutionLogResponse as ActionExecutionLogResponse,
    type ActionExecutionRetrieveFieldsResponse as ActionExecutionRetrieveFieldsResponse,
    type ActionExecutionRetrieveLogResponse as ActionExecutionRetrieveLogResponse,
    type ActionExecutionLogParams as ActionExecutionLogParams,
  };
}
